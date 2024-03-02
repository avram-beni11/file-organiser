"""
NOTES TO SELF WHAT TO ADD

- Add a GUI (TKinter)
    - User inputs desired starting dir
    - User inputs desired end dir
    - User chooses desired folder name(s)
    - User chooses what file extension to move
- Automatically sees the ROM extension and places it 
    where it needs to be, within the extension folder IN console 
    folder IN the correct lettered folder
"""

#Import modules
import os #Allows us to mess around with directories
from pathlib import Path #Allows us to create new directories
import shutil #Allows us to move files
from tkinter import * #GUI
import zipfile

#Change dir to "Downloads"
os.chdir("C:\\Users\\beni_\\Downloads")


#Loops through directory
for file in os.listdir():
    file_name, ext = os.path.splitext(file)

    #Checks for specific extension
    if ext == ".png":
        os.chdir("D:\\#Python File Organiser")
        #Remove extension period, capitalises it, and makes a new folder with the capitalised name
        remove_stop = ext.replace(".", "")
        folder_name = remove_stop.upper()
        Path(folder_name).mkdir(exist_ok=True)
        #Create variable "new_dir", which concatinates our desired final directory with the folder name created earluer
        new_dir = ("D:\\#Python File Organiser\\" + folder_name) 
        #Change dir back to "Downloads"
        os.chdir("C:\\Users\\beni_\\Downloads")
        print("File: " + file + " has been moved to: " + new_dir)
        #Move files from "Downloads" to our new folder named after the files extension
        shutil.move(file, new_dir)

    if ext == ".zip":
        with zipfile.ZipFile(file, 'r') as zip_file:
            file_list = zip_file.namelist()
            print("The file list is:", file_list)
            for rom_name in file_list:
                file_name, ext = os.path.splitext(rom_name)
                if rom_name.endswith(".gba"):
                    os.chdir("D:\\#Python File Organiser")
                    #Remove extension period, capitalises it, and makes a new folder with the capitalised name
                    remove_stop = ext.replace(".", "")
                    folder_name = remove_stop.upper()
                    Path(folder_name).mkdir(exist_ok=True)
                    #Create variable "new_dir", which concatinates our desired final directory with the folder name created earluer
                    new_dir = ("D:\\#Python File Organiser\\" + folder_name)
                    os.chdir("C:\\Users\\beni_\\Downloads")
                    shutil.move(file, new_dir)
                    
                    #print(f"Found .gba file: {file_name}")