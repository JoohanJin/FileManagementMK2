from watchdog.observers import Observer
# download watchdog module in the python virtual env by the command
# python3 -m pip install watchdong

from watchdog.events import FileSystemEventHandler
# import File system event handler from watchdog.events
# it can be used to see the file status

import os
import sys
import json
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # for each file in the file passed to the "os.listdir()"
        for file in os.listdir(folder_to_track):
            return


folder_to_track = "/home/joshep/Downloads"
folder_destination = "/home/joshep/Documents/PDFs"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive = True)
observer.start()