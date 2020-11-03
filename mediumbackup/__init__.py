import os
import logging

import medium
from markdownify import markdownify as md
from bs4 import BeautifulSoup as bs
import requests

MAX_FILENAME_LENGTH = 30 # Ignores date and extension, e.g. 2020-10-31<-- 30 characthers -->.md
FORBIDDEN_FILENAME_CHARS = "*?"

def backup_stories(username, backup_dir=None, format=None, download_images=False):
    """ Download all the public stories by username.
    
    Keyword arguments:
    backup_dir      -- destination directory name, default "backup"
    format          -- "html" or "md" for markdown, defualt "html"
    download_images -- True to download images and adjust the source, default False
    """
    
    # Check user input
    backup_dir = "backup" if backup_dir is None else backup_dir
    format = "html" if format is None else format
    if format not in ["html", "md"]:
        logging.warning("Format {} not recognized, html will be used instead.".format(format))
        
    # Create backup directroy if not existent
    if not os.path.exists(backup_dir):
        os.mkdir(backup_dir)
    
    # Get the stories list through a medium client, 
    # authentication is not required in this case 
    mclient = medium.Client()
    list_stories = mclient.list_articles(username=username)
    
    # For each story, crate a backup file
    for story in list_stories:
        
        # Retrieve story information
        pub_date = story["pubDate"][:len("yyyy-mm-dd")]
        title = story["title"]
        link = story["link"]
        content = story["content"]
        
        # If requested, download all images
        if download_images:
            
            images_dir = "images"
            if not os.path.isdir(os.path.join(backup_dir, images_dir)):
                os.mkdir(os.path.join(backup_dir,images_dir))
            
            soup = bs(content, "html.parser")
            img_sources = [img["src"] for img in soup.find_all("img")]
            
            for img_src in img_sources:
                
                # Ignore placeholder images for stats
                if img_src.startswith("https://medium.com/_/stat"):
                    continue
                
                # Download the image
                r = requests.get(img_src)
                
                #Build the filename of the image
                filename = img_src.split("/")[-1]
                for char in FORBIDDEN_FILENAME_CHARS:
                    filename = filename.replace(char, "")
                # Content type is e.g. "image/gif"
                img_suffix = "." + r.headers["Content-Type"].split("/")[-1]
                # Add the suffix if necessary, some redirect urls do not include it
                if not filename.endswith(img_suffix):
                    filename += img_suffix
                
                # Save the image
                file_path = os.path.join(backup_dir, images_dir, filename)
                with open(file_path, "wb") as f:
                    f.write(r.content)
                    logging.info("Downloaded \"{}\" to \"{}\".".format(img_src, file_path))
                
                #Replace src attributes to point to the downloaded image
                new_src = "/".join((images_dir, filename))
                content = content.replace("src=\"" + img_src  + "\"",
                                          "src=\"" + new_src + "\"")        
        
        # Add story title to the content
        content = "<h1>{}</h1>{}".format(title, content)
        if format == "md":
            content = md(content, heading_style="ATX")
        
        # Find the url path portion of the story url 
        # (i.e. whatever comes after the last /)
        # and remove invalid filename characthers
        url_path = link.split("/")[-1]
        for char in FORBIDDEN_FILENAME_CHARS:
            url_path = url_path.replace(char, "")
        
        # Build the filename and save the file
        filename = "".join([pub_date, " ", url_path[:MAX_FILENAME_LENGTH], ".", format])
        with open(os.path.join(backup_dir, filename), "wt", encoding="utf8") as f:
            f.write(content)
    return
    
    