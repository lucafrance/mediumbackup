import os

import medium
from markdownify import markdownify as md

MAX_FILENAME_LENGTH = 30 # Ignores date and suffix, e.g. 2020-10-31<-- 30 characthers -->.md

def backup_stories(username, backup_dir = "backup"):
    
    if not os.path.exists(backup_dir):
        os.mkdir(backup_dir)
    
    mclient = medium.Client()
    list_stories = mclient.list_articles(username=username)
    
    for story in list_stories:
        
        pub_date = story["pubDate"][:len("yyyy-mm-dd")]
        title = story["title"]
        link = story["link"]
        content = story["content"]
        
        content = "<h1>{}</h1>{}".format(title, content)
        content = md(content, heading_style="ATX")
        
        url_path = link.split("/")[-1]
        # Remove invalid filename charachters
        for char in "?":
            url_path = url_path.replace(char, "")
        filename = "".join([pub_date, " ", url_path[:MAX_FILENAME_LENGTH], ".md"])
        
        with open(os.path.join(backup_dir, filename), "wt", encoding="utf8") as f:
            f.write(content)
    return
    

if __name__ == "__main__":
    pass