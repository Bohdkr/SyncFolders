import os
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger(__name__)


def copy_file(source, replica):
    with open(source, 'rb') as source_file:
        with open(replica, 'wb') as replica_file:
            replica_file.write(source_file.read())

    logger.info(f"Copied file {source} in {replica_folder}")


def sync_folders(source, replica):
    for item in os.listdir(source):
        source_item = os.path.join(source, item)
        replica_item = os.path.join(replica, item)

        if os.path.isdir(source_item):
            if not os.path.exists(replica_item):
                os.makedirs(replica_item)
                logger.info(f"Created folder: {replica_item}")
            sync_folders(source_item, replica_item)
        else:
            copy_file(source_item, replica_item)


if __name__ == "__main__":
    source_folder = input("Enter source folder: ")
    replica_folder = input("Enter replica folder: ")
    logger_file = input("Enter path to logging file: ")

    file_handler = logging.FileHandler(logger_file)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
    logger.addHandler(file_handler)

    sync_folders(source_folder, replica_folder)
