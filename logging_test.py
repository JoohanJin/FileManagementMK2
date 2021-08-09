import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler


# make the logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s-%(message)s',
                    # log format -> asctime
                    datefmt="%Y-%m-%d %H:%M:%S"
                    #    time format, year-month-day hour-min-sec
                    )

WATCH_FILE = "/home/joshep/Desktop/myFolder"
logging_handler = LoggingEventHandler()
observer = Observer()  # observer for the file to watch
# can override the settings by inheritance by making sub-class
observer.schedule(logging_handler, WATCH_FILE, recursive=False)
# recursive = True: also track the changes in the sub-directory in the watching directory
# recursive = False: does not track the changes in the sub-directory in the watching directory
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()