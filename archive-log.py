#!/usr/bin/env python3
import os
import sys
import tarfile
from datetime import datetime
import logging

def setup_logging():
    """Setup logging configuration"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        handlers=[
            logging.FileHandler('archive.log'),
            logging.StreamHandler()
        ]
    )

def create_archive(log_directory):
    """
    Create a tar.gz archive of logs from the specified directory
    
    Args:
        log_directory (str): Path to directory containing logs
    """
    if not os.path.exists(log_directory):
        logging.error(f"Directory {log_directory} does not exist!")
        sys.exit(1)

    # Create archive directory if it doesn't exist
    archive_dir = "archived_logs"
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    # Generate archive filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_name = f"logs_archive_{timestamp}.tar.gz"
    archive_path = os.path.join(archive_dir, archive_name)

    try:
        # Create tar.gz archive
        with tarfile.open(archive_path, "w:gz") as tar:
            # Add each file from log directory to archive
            for root, _, files in os.walk(log_directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, log_directory)
                    tar.add(file_path, arcname=arcname)
        
        logging.info(f"Successfully created archive: {archive_path}")
        logging.info(f"Archived {len(os.listdir(log_directory))} files from {log_directory}")
        
    except Exception as e:
        logging.error(f"Error creating archive: {str(e)}")
        sys.exit(1)

def main():
    # Check if directory argument is provided
    if len(sys.argv) != 2:
        print("Usage: log-archive <log-directory>")
        sys.exit(1)

    log_directory = sys.argv[1]
    
    # Setup logging
    setup_logging()
    
    # Create archive
    create_archive(log_directory)

if __name__ == "__main__":
    main()
