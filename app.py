import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt','r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        # strip off all of the empty spaces
        apps = [x for x in tempApps if x.strip()]

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()


    filename = filedialog.askopenfilename(initialdir="/", title="Select File", 
    filetypes=(("executables","*.exe"), ("all files", "*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height=700, width=700, bg="#ADD8E6")
# attach it to root with canvas.pack()
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, 
                    pady=5, fg="white", bg="#ADD8E6", command=addApp)
# relx and rely will center it

openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, 
                    pady=5, fg="white", bg="#ADD8E6", command=runApps)

runApps.pack()

root.mainloop()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

# save a file so that we can save the apps we want to open
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
        # write the text file as f