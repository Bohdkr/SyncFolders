import os
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger(__name__)


def copy_file(source, replica):
    with open(source, 'r') as source_file:
        with open(replica, 'w') as replica_file:
            replica_file.write(source_file.read())

    logger.info("Copied file into replica folder")


def sync_folders(source, replica):
    for item in os.listdir(source_folder):
        source_item = os.path.join(source, item)
        replica_item = os.path.join(replica, item)

        if os.path.isdir(source_item):
            sync_folders(source_item, replica_item)
        else:
            copy_file(source_item, replica_item)

    logger.info("Created file in replica folder")


if __name__ == "__main__":
    source_folder = input("Enter source folder: ")
    replica_folder = input("Enter replica folder: ")
    logger_file = input("Enter path to logging file: ")

    log_file = logger_file
    file_handler =logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
    logger.addHandler(file_handler)

    sync_folders(source_folder, replica_folder)
