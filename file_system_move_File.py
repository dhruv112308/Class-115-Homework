import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source = r"C:\Users\dhruv\Downloads"
dest = r"C:\Users\dhruv\OneDrive\Desktop\Python Coding\Class 115 Homework"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    #Student Activity1

    

    def on_created(self, event):
        name,extention=os.path.splitext(event.src_path)
        for key, value in dir_tree.items():
            if extention in value:
                file_name=os.path.basename(event.src_path)
                path1 = source+"/"+file_name
                path2 = dest+"/"+key
                path3 = dest+"/"+key+"/"+file_name
                time.sleep(3)
                if os.path.exists(path2):
                    print("Directory already exists")
                    time.sleep(1)
                    if os.path.exists(path3):
                        print("File already exists")
                        print("Renaming the file")    
                        new_file_name=os.path.splitext(file_name)[0]+str(random.randint(0,999))+os.path.splitext(file_name)[1]
                        path4=dest+"/"+key+"/"+new_file_name
                        print("Source path renamed to destination path successfully")
                        shutil.move(path1, path4)
                    else:     
                        print("Moving"+file_name)
                        shutil.move(path1,path3)
                        time.sleep(1)
                else: 
                    os.makedirs(path2)
                    print("Moving"+file_name)    
                    shutil.move(path1,path3)
                    time.sleep(1)
        print(event)
        print(event.src_path)


# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, source, recursive=True)


# Start the Observer
observer.start()

#Student Activity2
try:    
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped")        
    observer.stop()

    