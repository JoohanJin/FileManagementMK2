from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import datetime, os, time, logging

folder_to_track = f"/home/joshep/Desktop/myFolder"
folder_destination = f"/home/joshep/Desktop/testFolder"

# Patterns of the files to watch
WATCH_PATTERN = '.txt,.pdf,.doc,.docx,.csv,.xml'

LOG_FILES_EXTENSION = {
    '.txt', '.pdf', '.doc', '.docx', '.csv', '.xml'
}

class myHandler(FileSystemEventHandler):
    # inheritance from the FileSystemEventHandler
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            now = (datetime.datetime.now()).strftime("%Y_%m_%d %H_%M_%S")
            src = f"{folder_to_track}/{filename}"
            dest = f"{folder_destination}/{now}_{filename}"
            # add the time information for easier file management
            os.rename(src, dest)
            logging.info(f"{src} has been moved to {dest}!")
        # os.rename-> renames the file or directory from src to new_destination.
        # does it also move the location as well?
        # it is like the changing the information of the file

event_handler = myHandler()
observer = Observer()
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s-%(message)s",
                    datefmt="%Y-%m-%d %H-%M-%S")
# schedule(event_handler, path, recursive = False)
'''
watching a path and calls appropriate methods specified in the given event handler in response
to file system events.
'''

observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()