import unittest
import filecmp
import os
import shutil

import medium_backup

TEST_BACKUP_DIR = os.path.join("tests","backup")
REFERENCE_STORY_MD = "2020-10-05 come-aggiungere-i-caratteri-ma.md"

class MediumStoriesTest(unittest.TestCase):
    
    def test_story_md(self):
        medium_backup.backup_stories(username="lucafrance", backup_dir=TEST_BACKUP_DIR)
        test_md_file = os.path.join(TEST_BACKUP_DIR, REFERENCE_STORY_MD)
        reference_md_file = os.path.join("tests", REFERENCE_STORY_MD)
        self.assertTrue(os.path.exists(test_md_file))
        self.assertTrue(filecmp.cmp(test_md_file, reference_md_file, shallow=False))
        shutil.rmtree(TEST_BACKUP_DIR)
        return
        
        
if __name__ == "__main__":
    unittest.main()
