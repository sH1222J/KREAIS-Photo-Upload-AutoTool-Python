import os
import time
import win32gui
import clipboard
import tkinter as tk
import natsort as ns
import pyautogui as py

from tkinter import messagebox
from PIL import Image, ImageTk
from tqdm import tqdm

root = tk.Tk()

def enumHandler(hwnd, lParam):
    if win32gui.IsWindowVisible(hwnd):
        if appname in win32gui.GetWindowText(hwnd):
            win32gui.MoveWindow(hwnd, xpos, ypos, width, length, True)

def left_arrow(event, image):
    copy_and_paste(image)
    root.destroy()
    
def right_arrow(event, image):
    copy_and_paste(image)
    root.destroy()

def get_image_file_list(path):
    imageList = []
    directory = os.listdir(path)  
    for file in directory:
        if file.endswith('.jpg'):
            imageList.append(file)

    return ns.natsorted(imageList)

def copy_and_paste(data):
    clipboard.copy(data)
    clipboard.paste()
    
def on_closing():
    root.destroy()
    quit()
        
global dirPath
def set_button_Click(path):
    global dirPath
    dirPath = path + '\\'
    print('Set path: ' + dirPath)
    root.destroy()
    
def image_button_click(image):
    while True:
        try:
            time.sleep(1)
            btnImage = py.locateOnScreen(image)        
            point = py.center(btnImage)  
            print(image + ' ' + str(point))
            time.sleep(1)
            py.click(point)
            break
        except:
            print('Error: ' + image + ' not found.')
            time.sleep(1)
            continue

def choice_images(image1, image2, dirPath):
    tempImage1 = Image.open(dirPath + image1)
    pil_image1 = tempImage1.resize((400, 400))
    tempImage2 = Image.open(dirPath + image2)
    pil_image2 = tempImage2.resize((400, 400))

    width = 800 # 1200
    height = 400 # 500

    imageTk1 = ImageTk.PhotoImage(image=pil_image1)
    imgLabel1 = tk.Label(root, image=imageTk1)
    imgLabel1.grid(row=0, column=0)

    imageTk2 = ImageTk.PhotoImage(image=pil_image2)
    imgLabel2 = tk.Label(root, image=imageTk2)
    imgLabel2.grid(row=0, column=1)

    root.bind("<Left>", lambda event: left_arrow(event, dirPath + image1))
    root.bind("<Right>", lambda event: right_arrow(event, dirPath + image2))

    root.title(image1 + ' vs ' + image2)
    root.geometry(f'{width}x{height}+{1100}+{580}') #1900, 500
    root.after(1, lambda: root.focus_force())
    root.resizable(False, False)
    root.mainloop()

appname = 'py.exe'
xpos = 1000
ypos = 0
width = 1000
length = 300
win32gui.EnumWindows(enumHandler, None)

input_path = tk.Entry(root, width=100)
input_path.pack()
btnSet = tk.Button(root, text='set', command=lambda: set_button_Click(str(input_path.get())))
btnSet.pack()

root.title('Please enter the image file path: ')
root.protocol("WM_DELETE_WINDOW", on_closing)
root.resizable(False, False)
root.mainloop()

imageList = get_image_file_list(dirPath)

root = tk.Tk()

if len(imageList) % 2 != 0:
    root.withdraw()
    messagebox.showerror('Count error', 'File count mismatch.' + '\nError directory: ' + dirPath)
    root.destroy()
    quit()

btnImagePath = 'C:/Users/user/Desktop/AutoTool_Python/'
for i in tqdm(range(0, len(imageList), 2)):
    print()
    print('Current image: ' + imageList[i] + ', ' + imageList[i+1])

    image_button_click(btnImagePath + 'picture.png')
    choice_images(imageList[i], imageList[i+1], dirPath)  
    image_button_click(btnImagePath + 'register.png')
    
    py.hotkey('ctrl', 'v')
    py.press('Enter')
    py.press('Enter')

    image_button_click(btnImagePath + 'close.png')
    image_button_click(btnImagePath + 'next.png')

    root = tk.Tk()

print('Finish !!! \^0^/')
