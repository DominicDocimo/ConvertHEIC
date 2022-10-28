from tkinter import filedialog, messagebox
import subprocess
import os

messagebox.showinfo("HEICToJPG", "On the next screen, select the directory in which your HEIC files are located. "
                                 "The time this process will take varies based on how many files need to be converted.")
path = filedialog.askdirectory()
count = 0

for file in os.listdir(path):
    if file.endswith(".HEIC") or file.endswith(".heic"):
        subprocess.run(["magick", "%s" % f"{path}/{file}", "%s" % f"{path}/{(file[0:-5] + '.jpg')}"])
        count += 1
        continue

messagebox.showinfo("Successfully Completed", f"Converted {count} files.")
