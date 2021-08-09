from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import os, datetime, time, logging

folder_to_track = f"/home/joshep/Desktop/myFolder"
folder_destination = f"/home/joshep/Desktop/testFolder"

WATCH_PATTERN = ["*.py"]
EXCEPTION_PATTERN = ["*.~"]

class MyHandler(PatternMatchingEventHandler):
    def __init__(self):
        super().__init__(patterns=WATCH_PATTERN, 
                        ignore_patterns=EXCEPTION_PATTERN, 
                        ignore_directories=False, 
                        case_sensitive=True)

    def on_modified(self, event):
        for filename in os.listdir(folder_to_track): # for each file in the directory being watched
            # check current time and add it to the file name
            now = (datetime.datetime.now()).strftime("%Y_%m_%d %H_%M_%S")
            src = f"{folder_to_track}/{filename}"
            dest = f"{folder_destination}/{now}_{filename}"
            os.rename(src, dest)
            logging.info(f"{src} has been changed to {dest}!")


event_handler = MyHandler()
observer = Observer()
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s-%(message)s",
                    datefmt="%Y-%m-%d %H-%M-%S")

observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()