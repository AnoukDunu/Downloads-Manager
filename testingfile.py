#importing library to access files in windows desktop
import os

#defining the 'Downloads' folder directory
source_directory = "/Users/anouk/Downloads"

#for loop for entries list
with os.scandir(source_directory) as entires:
    for entry in entires:
        print(entry.name)

#install watchdog library to listen to changes in folders

import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()