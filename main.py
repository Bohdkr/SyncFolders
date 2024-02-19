import os
import logging
import sched
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger(__name__)


def copy_file(source, replica):
    if not os.path.exists(replica):
        with open(source, 'rb') as source_file:
            with open(replica, 'wb') as replica_file:
                replica_file.write(source_file.read())
        logger.info(f"Copied file {source} in {replica}")

    else:
        logger.info(f"File {source} is already synchronized")


def sync_folders(source, replica):
    for item in os.listdir(replica):
        source_item = os.path.join(source, item)
        replica_item = os.path.join(replica, item)

        if os.path.isfile(replica_item) and not os.path.exists(source_item):
            os.remove(replica_item)
            logger.info(f"File {replica_item} was removed")

        if os.path.isdir(replica_item) and not os.path.exists(source_item):
            os.removedirs(replica_item)
            logger.info(f"Folder {replica_item} was removed")

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


def sync_periodically(source, replica, interval_minutes):
    scheduler = sched.scheduler(time.time, time.sleep)

    def sync_task():
        sync_folders(source, replica)
        scheduler.enter(interval_minutes * 60, priority=1, action=sync_task)

    scheduler.enter(0, 1, sync_task)
    scheduler.run()


if __name__ == "__main__":
    source_folder = input("Enter source folder: ")
    replica_folder = input("Enter replica folder: ")
    logger_file = input("Enter path to logging file: ")
    interval_minutes = int(input("Enter sync interval in minutes: "))

    file_handler = logging.FileHandler(logger_file)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s',  datefmt='%d-%b-%y %H:%M:%S'))
    logger.addHandler(file_handler)

    sync_periodically(source_folder, replica_folder, interval_minutes)
