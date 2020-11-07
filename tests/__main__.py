import unittest
import filecmp
import os
import shutil

import mediumbackup as mb


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
        return
        
        
if __name__ == "__main__":
    unittest.main()
