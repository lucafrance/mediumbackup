import mediumbackup
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Backup your Medium stories.')

    parser.add_argument("username", help="A Medium username")
    parser.add_argument("--backup_dir", "--bd", help="destination directory name")
    parser.add_argument("--format", "--f", help="\"html\" or \"md\" for markdown")
    parser.add_argument("--download_images", "--i", action="store_true", help="Download images locally")
    parser.set_defaults(download_images=False)
    
    arguments = parser.parse_args()
    mediumbackup.backup_stories(
        arguments.username, backup_dir=arguments.backup_dir, 
        format=arguments.format, download_images=arguments.download_images,
        )
    
    