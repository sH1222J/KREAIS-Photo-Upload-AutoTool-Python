import os
import time
import clipboard
import natsort as ns
import pyautogui as py

from tqdm import tqdm

directory = os.listdir('D:/@@동별 분류-용량 최적화/105-신대동/')

imageList = []
for file in directory:
    if file.endswith('.jpg'):
        imageList.append(file)

imageList = ns.natsorted(imageList)

totalCount = 0
for image in tqdm(imageList):
    print()
    print('Current image: ' + image)
    
    while True:
        try:
            btnPicture = py.locateOnScreen('C:/Users/user/Desktop/AutoTool_Python/picture.png')        
            point = py.center(btnPicture)  
            print('btnPicture: ' + str(point))
            py.click(point)
            break
        except:
            print('Error: btnPicture not found.')
            time.sleep(1)
            continue
        
    while True:
        try:
            btnRegister = py.locateOnScreen('C:/Users/user/Desktop/AutoTool_Python/register.png')
            point = py.center(btnRegister)
            print('btnRegister: ' + str(point))
            py.click(point)
            break
        except:
            print('Error: btnRegister not found.')
            time.sleep(1)
            continue
        
    clipboard.copy(image)
    result = clipboard.paste()
    py.hotkey('ctrl', 'v')
    py.press('Enter')
    py.press('Enter')

    while True:
        try:
            btnClose = py.locateOnScreen('C:/Users/user/Desktop/AutoTool_Python/close.png')
            point = py.center(btnClose)
            print('btnClose: ' + str(point))
            py.click(point)
            break
        except:
            print('Error: btnClose not found.')
            time.sleep(1)
            continue

    if totalCount > 2:
        while True:
            try:
                btnNext = py.locateOnScreen('C:/Users/user/Desktop/AutoTool_Python/next.png')
                point = py.center(btnNext)
                print('btnNext: ' + str(point))
                py.click(point)
                totalCount = 0
                break
            except:
                print('Error: btnNext not found.')
                time.sleep(1)
                continue
    else:
        totalCount = totalCount + 1

print('Finish !!! \^0^/')