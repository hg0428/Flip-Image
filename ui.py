from tkinter import *

from tkinter import filedialog
import flip
import os
from sys import exit
from pathlib import Path
from PIL import Image, ImageTk
import platform


# Function for opening the
# file explorer window
def get_folder():
    folder = filedialog.askdirectory(
        initialdir="/",
        title="Select a Directory",
    )
    output = filedialog.askdirectory(
        initialdir=Path(folder).parent, title="Where to save?"
    )
    # Change label contents
    label_file_explorer.configure(text="Folder Opened: " + folder)

    flip.flip_images(folder, output)
    os.system("open " + output)


def get_file():
    file = filedialog.askopenfilename(
        initialdir="/",
        title="Select a File",
    )
    output = filedialog.asksaveasfilename(
        initialdir=Path(file).parent, title="Where to save?"
    )

    # Change label contents
    label_file_explorer.configure(text="File Opened: " + file)

    flip.flip_image(file, output)
    os.system("open " + output)


# Create the root window
window = Tk()

# Set window title
window.title("File Flipper")

current_platform = platform.system()

if current_platform == "Windows":
    icon_path = os.path.join(os.path.dirname(__file__), "icons/icon.ico")
    window.iconbitmap(icon_path)  # Use iconbitmap for .ico files on Windows
else:
    icon_path = os.path.join(os.path.dirname(__file__), "icons/icon.png")
    icon = ImageTk.PhotoImage(file=icon_path)
    window.iconphoto(False, icon)

# Set window size
window.geometry("500x500")

# Set window background color
window.config(background="white")

# Create a File Explorer label
label_file_explorer = Label(
    window, text="File Flipper", width=100, height=4, fg="black", bg="white"
)


button_explore_folder = Button(
    window,
    text="Flip all in Folder",
    command=get_folder,
    bg="white",
    bd=0,
    highlightthickness=0,
)
button_explore_file = Button(
    window, text="Flip File", command=get_file, bg="white", bd=0, highlightthickness=0
)
button_exit = Button(
    window,
    text="Exit",
    command=exit,
    bg="white",
    bd=0,
    highlightthickness=0,
)

# Place components on the screen
label_file_explorer.pack()
button_explore_folder.pack(pady=5)
button_explore_file.pack(pady=5)
button_exit.pack(pady=5)

# Let the window wait for any events
window.mainloop()
