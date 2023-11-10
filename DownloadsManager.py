#Importing the libraries
import os #Library to access files in Windows
import shutil
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#defining the directories to look in and move downloaded files to
source_dir = "/Users/anouk/Downloads"
destination_dir_images = "/Users/anouk/Downloads/DownloadedImages"
destination_dir_torrents = "/Users/anouk/Downloads/DownloadedTorrents"
destination_dir_setups = "/Users/anouk/Downloads/DownloadedSetups"

def makeUnique(path):
    filename, extension = splitext(name)
    counter = 1
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter+= 1
    return name

def move(dest, entry, name):
    file_exists = os.path.exists(dest + "/" + name)
    if file_exists:
        unique_name = makeUnique(name)
        os.rename(entry, unique_name)
    shutil.move(entry, dest)

class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                dest = source_dir
                if name.endswith('.png') or name.endswith('.jpg'):
                    dest = destination_dir_images
                    move(dest, entry, name)
                elif name.endswith('.exe') or name.endswith('.msi'):
                    dest = destination_dir_setups
                    move(dest, entry, name)
                elif name.endswith('.torrent'):
                    dest = destination_dir_torrents


#sample code to listen for the changes in the downloads folder
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()