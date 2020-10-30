"""
    Name: clearfolder.py
    Version: 0.1
    Description: This script used to move every file in a specified direcoty sored by year, month and type
        ex. /home/user/Storage/2019/09/Image/file.png
            /home/user/Storage/2019/09/Document/file.pdf
        p.s. This scripts doesn't work for downloads directory except do you used browser chrome

    Copyright (C) 2019 Luca Canali

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from time import sleep, strftime
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from os import mkdir, path, rename, stat
from ntpath import basename
from filetype import guess_extension, guess_mime
#from sys import argv
from pathlib import Path
import json
import logging

logging.basicConfig(filename=path.dirname(path.realpath(__file__)) + '/clearfolder.log', format='%(asctime)s %(levelname)s: %(message)s', level=logging.WARNING)
data = {}
try:
    # Get config parameters
    with open(path.dirname(path.realpath(__file__)) + "/config.json") as config_file:
        data =json.load(config_file)
except Exception as e:
    logging.error('Exception occurred', exc_info=True)

# Set directory_to_watch
directory_to_watch = data['directory_to_watch']
if not path.isdir(directory_to_watch) or not isinstance(directory_to_watch, str):
    logging.error("The directory_to_watch parameter isn't string or not exists")
    quit()
# Set time_to_sleep
time_to_sleep = data['time_to_sleep']
if not isinstance(time_to_sleep, int):
    logging.error("The time_to_sleep parameter isn't int")
    quit()

''' Old block to check if parameters it's good
directory_to_watch = ""
try:
    if 1 < len(argv) <= 2:
        # Check how many parameters are passed
        if path.isdir(argv[1]):
            # Check if parameter passed is a directory
            directory_to_watch = argv[1] + "/"
        else:
            print("The path isn't exist or isn't a directory")
            quit()
    else:
        print("The parameters is too much or too few")
        quit()
except IndexError:
    print("No parameters passed")
    quit()
'''


class Watcher:

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, directory_to_watch, recursive=False)
        self.observer.start()

        try:
            while True:
                sleep(time_to_sleep)
        except KeyboardInterrupt:
            logging.info('Exception occurred', exc_info=True)
            self.observer.stop()

        self.observer.join()


class Handler(FileSystemEventHandler):

    # Get only event
    @staticmethod
    def on_created(event):
        filename = event.src_path
        if not path.isfile(filename) or basename(filename).split(".")[-1] == 'crdownload':
            # This section is for directory Downloads and only work with chrome browser
            pass
        else:
            logging.debug(f"The file {filename} is get to the event created")
            # Take event created
            destination = directory_to_watch + "Storage/"
            if not path.exists(destination):
                # Make destination if not exists
                mkdir(destination)
            # Get file extension and mime
            file_guess_mime = guess_mime(filename)
            file_guess_extension = guess_extension(filename)
            if file_guess_mime is None:
                # Set filetype None if doesn't match mime
                file_type = "None"
            else:
                # Set filetype to the matched mime
                file_guess_mime_split = file_guess_mime.split("/")
                file_type = str(file_guess_mime_split[0]).capitalize()
            filename_split = basename(filename).split(".")
            try:
                # If file have extension
                if len(filename_split) > 1:
                    # If filename have multiple dot in the name get only the last
                    file_extension = filename_split[-1]
                else:
                    # Else get second
                    file_extension = filename_split[1]
            except IndexError:
                if file_guess_extension is None:
                    # If file haven't extension set to noname
                    file_extension = "noname"
                else:
                    # Else get extension from guess_extension
                    file_extension = filename_split.append(file_guess_extension)
            # Get modification time of filename
            modification_time = stat(filename).st_mtime
            # Set Year with modification time
            year = datetime.fromtimestamp(modification_time).strftime('%Y')
            # Set Month with modification time
            month = datetime.fromtimestamp(modification_time).strftime('%m')

            # Check if the directories Storage, Year and Month exists if they don't exists create them
            if not path.exists(destination + "/" + year):
                mkdir(destination + "/" + year)
            if not path.exists(destination + "/" + year + "/" + month):
                mkdir(destination + "/" + year + "/" + month)
            if not path.exists(destination + "/" + year + "/" + month + "/" + file_type):
                mkdir(destination + "/" + year + "/" + month + "/" + file_type)

            # Set final destination to the path made before
            destination = destination + "/" + year + "/" + month + "/" + file_type
            # Set final file name and destinations
            new_name = destination + "/" + filename_split[0] + "." + file_extension
            i = 0
            while path.exists(new_name):
                # If new_name is an existing file add a number at the name
                i += 1
                new_name = destination + "/" + filename_split[0] + str(i) + "." + file_extension
                print(new_name)
            # Move the file to the destinations directory
            rename(filename, new_name)
            logging.debug(f"The file {filename} is stored in {new_name}")


if __name__ == '__main__':
    try:
        w = Watcher()
        w.run()
    except Exception as e:
        logging.error('Exception occurred', exc_info=True)