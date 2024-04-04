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
from tkinter import ttk
import zipfile

#Change dir to "Downloads"
os.chdir("C:\\Users\\beni_\\Downloads")

root = Tk()
root.title("Mass File Mover")
root.resizable(FALSE, FALSE)
root.configure(bg="#5ea6ee")

# displayContent = " "

# startDir = Entry(root, width=40)
# startDir.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# endDir = Entry(root, width=40)
# endDir.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# moveBtn = Button(root, text="Move Files", padx=20, pady=1, command=fileMove())
# moveBtn.grid(row=2)

# def dolphin_emu():
#     with zipfile.ZipFile(file, 'r') as zip_file:
#             file_list = zip_file.namelist()
#             print("The file list is:", file_list)
#             for rom_name in file_list:
#                 file_name, ext = os.path.splitext(rom_name)
#                 #if rom_name.endswith(".gba"):
#                 os.chdir("D:\\#Python File Organiser")
#                 #Remove extension period, capitalises it, and makes a new folder with the capitalised name
#                 remove_stop = ext.replace(".", "")
#                 folder_name = remove_stop.upper()
#                 Path(folder_name).mkdir(exist_ok=True)
#                 #Create variable "new_dir", which concatinates our desired final directory with the folder name created earluer
#                 new_dir = ("D:\\#Python File Organiser\\" + folder_name)
#                 os.chdir("C:\\Users\\beni_\\Downloads")
#                 print(file)
#                 print("Function Called")
#                 try:
#                     shutil.move(file, new_dir)
#                     #os.remove(file + ".zip")
#                 except WindowsError:
#                     pass

#Loops through directory
for file in os.listdir():
    file_name, ext = os.path.splitext(file)

    def fileMove():
        #Checks for specific extension
        # if ext == ".webp":
            #os.chdir("D:\\#Python File Organiser")
            global startDir
            global endDir
            #print(startDir.get())
            # fixed_start = startDir.get().replace("\\", "\\\\")
            # fixed_end = endDir.get().replace("\\", "\\\\")
            os.chdir(startDir.get())
            #Remove extension period, capitalises it, and makes a new folder with the capitalised name
            remove_stop = ext.replace(".", "")
            folder_name = remove_stop.upper()
            Path(folder_name).mkdir(exist_ok=True)
            #Create variable "new_dir", which concatinates our desired final directory with the folder name created earluer
            # new_dir = ("D:\\#Python File Organiser\\" + folder_name) 
            new_dir = (endDir.get() + "\\" + folder_name) 
            #Change dir back to "Downloads"
            # os.chdir("C:\\Users\\beni_\\Downloads")
            os.chdir(startDir.get())
            print("File: " + file + " has been moved to: " + new_dir + " from " + startDir.get())
            #Move files from "Downloads" to our new folder named after the files extension
            shutil.move(file, new_dir)
            
    # def printTest():
    #     print("Hello World")

    # if ext == ".zip":
    #     with zipfile.ZipFile(file, 'r') as zip_file:
    #         file_list = zip_file.namelist()
    #         print("The file list is:", file_list)
    #         for rom_name in file_list:
    #             file_name, ext = os.path.splitext(rom_name)
    #             #if rom_name.endswith(".gba"):
    #             os.chdir("D:\\#Python File Organiser")
    #             #Remove extension period, capitalises it, and makes a new folder with the capitalised name
    #             remove_stop = ext.replace(".", "")
    #             folder_name = remove_stop.upper()
    #             Path(folder_name).mkdir(exist_ok=True)
    #             #Create variable "new_dir", which concatinates our desired final directory with the folder name created earluer
    #             new_dir = ("D:\\#Python File Organiser\\" + folder_name)
    #             os.chdir("C:\\Users\\beni_\\Downloads")
    #             #print(file)
    #             try:
    #                 shutil.move(file, new_dir)
    #                 #os.remove(file + ".zip")
    #             except WindowsError:
    #                 pass
        
    # if ext == ".zip":
    #     dolphin_emu()

# if ext == ".png":
    # os.chdir("D:\\#Python File Organiser")
    # #Remove extension period, capitalises it, and makes a new folder with the capitalised name
    # remove_stop = ext.replace(".", "")
    # folder_name = remove_stop.upper()
    # Path(folder_name).mkdir(exist_ok=True)
    # #Create variable "new_dir", which concatinates our desired final directory with the folder name created earluer
    # new_dir = ("D:\\#Python File Organiser\\" + folder_name) 
    # #Change dir back to "Downloads"
    # os.chdir("C:\\Users\\beni_\\Downloads")
    # print("File: " + file + " has been moved to: " + new_dir)
    # #Move files from "Downloads" to our new folder named after the files extension
    # try:
    #     shutil.move(file, new_dir)
    # except: 
    #     print("Directory already exists")
displayContent = " "
textIn = StringVar()

# def temp_text_start(e):
#    startDir.delete(0,"end")

# def temp_text_end(e):
#    endDir.delete(0,"end")

startDir = Entry(root, textvariable=textIn, width=40)
startDir.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
startDir.insert(0, "Enter starting directory...")
# startDir.bind("<FocusIn>", temp_text_start)

endDir = Entry(root, width=40)
endDir.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
endDir.insert(0, "Enter end directory...")
# endDir.bind("<FocusIn>", temp_text_end)

moveBtn = Button(root, text="Move Files", padx=20, pady=1, command=fileMove)
moveBtn.grid(row=2)

root.mainloop()