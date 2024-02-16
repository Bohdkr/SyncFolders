import os


def copy_file(source, replica):
    with open(source, 'r') as source_file:
        with open(replica, 'w') as replica_file:
            replica_file.write(source_file.read())


def sync_folders(source, replica):
    for item in os.listdir(source_folder):
        source_item = os.path.join(source, item)
        replica_item = os.path.join(replica, item)

        if os.path.isdir(source_item):
            sync_folders(source_item, replica_item)
        else:
            copy_file(source_item, replica_item)
            print("Copied")


if __name__ == "__main__":
    source_folder = input("Enter source folder: ")
    replica_folder = input("Enter replica folder: ")

    sync_folders(source_folder, replica_folder)
