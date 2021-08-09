from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging, os, time, datetime


folder_to_track = "/home/joshep/Downloads"
destination_folder = "/home/joshep/Documents"

WATCH_PATTERN = ('.pdf', '.doc', '.docx', '.csv', '.xml')

class myHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        for filename in os.listdir(folder_to_track):
            now = (datetime.datetime.now()).strftime("%Y_%m_%d %H_%M_%S")
            src = f"{folder_to_track}/{filename}"
            if src.endswith(WATCH_PATTERN):
                type = os.path.splitext(src)[1].strip(".").upper()
                dest = f"{destination_folder}/{type}/{now}_{filename}"
                os.rename(src, dest)
            else:
                dest = f"{destination_folder}/ELSE/{now}_{filename}"
                os.rename(src, dest)
            logging.info(f"{src} has been moved to {dest}!")


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