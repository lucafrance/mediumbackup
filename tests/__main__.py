import unittest
import filecmp
import os
import shutil

import mediumbackup as mb


def dummy_medium_story():
    dummy_raw = {
        "title": "Lorem Ipsum Dolor sit Amet",
        "pubDate": "2020-11-07 11:12:13",
        "link": "https://medium.com/@johndoe/some-title-and-random-charachters-abcdef123456",
        "guid": "https://medium.com/p/abcdef123456",
        "author": "Jon Doe",
        "thumbnail": "https://cdn-images-1.medium.com/max/1024/abcdef123456.png",
        "description": "",
        "content": "",
        "enclosure": "",
        "categories": ["tagA", "tagB", "tagC"],
    }
    return mb.MediumStory(dummy_raw)

class MediumStoriesTest(unittest.TestCase):
    
    def test_backup_stories_wo_images(self):
        test_backup_dir = os.path.join("tests","backup")
        for format in ("html", "md"):
            mb.backup_stories(username="lucafrance", backup_dir=test_backup_dir, format=format)
            file_extension = "." + format
            reference_story_name = "2020-10-05 come-aggiungere-i-caratteri-ma"
            test_file = os.path.join(test_backup_dir, reference_story_name) + file_extension
            reference_file = os.path.join("tests", reference_story_name) + file_extension
            self.assertTrue(os.path.exists(test_file))
        shutil.rmtree(test_backup_dir)
    
    
    def test_title(self):
        story = dummy_medium_story()
        story.title = "Lorem Ipsum"
        story.content = "<p>Dolor sit amet</p>"
        self.assertEqual(story.html(), "<h1>Lorem Ipsum</h1><p>Dolor sit amet</p>")
    
        
if __name__ == "__main__":
    unittest.main()
