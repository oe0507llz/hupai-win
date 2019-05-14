#import numpy as np
import pyautogui
import time
import os
from PIL import Image
import pytesseract
#import pandas as pd
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime
from dateutil import tz

from_zone = tz.gettz('UTC')

to_zone = tz.gettz('Asia/Shanghai')

utc = datetime.utcnow()

utc = utc.replace(tzinfo=from_zone)

local = utc.astimezone(to_zone)

initial_time = datetime.strftime(local, "%H:%M:%S")

print(initial_time)

#url = 'http://moni.51hupai.com/'

url1 = 'https://paimai.alltobid.com/'

#url2='https://paimai.alltobid.com/bid/2018091501/bid.htm'

url='https://paimai2.alltobid.com/bid/9a7c073cfdc24e11b31ee9a54bb696ad/bid.htm'

y_shift = 0

x_shift = 0

#y_shift = -150

#x_shift = -150

driver = webdriver.Ie("D:\\IEDriverServer.exe")
#driver = webdriver.Ie()
driver.set_window_position(60,20)
driver.set_window_size(1500,1200)
driver.get(url)

#print(str(datetime.now())[11:19])

if initial_time>'09:20:00':
    # pyautogui.click(1151,428)
    pyautogui.keyDown('ctrl')
    time.sleep(1)
    print('ctrl pressed')
    pyautogui.press('=')
    time.sleep(1)
    pyautogui.press('=')
    pyautogui.press('=')
    time.sleep(1)
    pyautogui.keyUp('ctrl')
    
    time.sleep(2)
    
    #websize = [1500,800]
    #websize = [1080,680]
    
    
    
    
    
    lowest = []
    timeNow = []
    highest = []
    
    month = '201902'
    
    directory = 'C:\Hupai\screenshot_{}/'.format(month)
    if not os.path.exists(directory):
    	os.makedirs(directory)
    
    	
    i = 0
    while i<900:
        fn = "screen_{}".format(i)
        new_dir = directory + fn
        pyautogui.screenshot("{}.png".format(new_dir))
        img = Image.open(new_dir + '.png')
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)

        area1 = (1144 + x_shift, 435 + y_shift, 1232 + x_shift, 465 + y_shift) # Lowest acceptable price
        cropped_img1 = img.crop(area1)
        cropped_img1.save('{}\{}_cropped1.png'.format(new_dir, fn))
#        im = cropped_img1.convert('RGBA')
#        data = np.array(im)
#        rgb = data[:,:,:3]
#        color1 = [251,237,227]
#        color2 = [251,237,226]
#        black = [0,0,0,255]
#        white = [255,255,255,255]
#        mask1 = np.all(rgb == color1, axis = -1)
#        data[mask1] = white
#        mask2 = np.all(rgb == color2, axis = -1)
#        data[mask2] = white
#        new_im = Image.fromarray(data)
#        new_im.save('{}\{}_new_file.tif'.format(new_dir, fn))
#        text1 = pytesseract.image_to_string(new_im, lang='eng', config = '-c tessedit_char_whitelist=0123456789')
        text1 = pytesseract.image_to_string(cropped_img1, lang='eng', config = '-c tessedit_char_whitelist=0123456789')
		if len(text1.replace(" ", "")) == 4:
			int_text1 = int(text1.replace(" ", ""))*10
		else:
			int_text1 = int(text1)
        lowest.append(text1)
        #print(text1)
        utc = datetime.utcnow()
        print(utc)
        utc = utc.replace(tzinfo=from_zone)
        local = utc.astimezone(to_zone)
        text2 = datetime.strftime(local, "%H:%M:%S")
        #timeNow.append(text2)
        print(text2)
        print(text1)
    	
        if text2 == "11:29:44" or text2 == "11:29:45":
    	#if text2 == "11:29:44" or text2 == "11:29:45":
            number_int = int_text1 +900
            number = str(number_int)
            
            pyautogui.moveTo(1204 + x_shift, 704 + y_shift)
            #pyautogui.moveTo(802, 369)
            pyautogui.click()
            pyautogui.doubleClick()
            time.sleep(0.5)
            pyautogui.doubleClick()
            pyautogui.press('del')
            time.sleep(0.5)
            pyautogui.typewrite(number)
            
            time.sleep(0.2)
            pyautogui.moveTo(1422 + x_shift, 709 + y_shift)
            #pyautogui.moveTo(920, 368)		
            pyautogui.click()
    	


        if (text2 >= "11:29:55"):
            #print("Number is defined, and click the button") 
            pyautogui.moveTo(992 + x_shift, 855 + y_shift)
            #pyautogui.moveTo(673, 455)
            pyautogui.click()
    	
        i +=1	
