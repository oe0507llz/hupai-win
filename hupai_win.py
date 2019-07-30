import numpy as np
import pyautogui
import time
import os
from PIL import Image
import pytesseract
#import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime
from dateutil import tz
import cv2
import sys
import re

def replace(string, substitutions):

    substrings = sorted(substitutions, key=len, reverse=True)
    regex = re.compile('|'.join(map(re.escape, substrings)))
    return regex.sub(lambda match: substitutions[match.group(0)], string)


try:
    mode = sys.argv[1]
except:
    mode = 'http://moni.51hupai.com/'

from_zone = tz.gettz('UTC')

to_zone = tz.gettz('Asia/Shanghai')

utc = datetime.utcnow()

utc = utc.replace(tzinfo=from_zone)

local = utc.astimezone(to_zone)

initial_time = datetime.strftime(local, "%H:%M:%S")

print(initial_time)

if mode == 'test':
    if initial_time[6:] < '40':
        press_time_1 = initial_time[:6] + '44'
        press_time_2 = initial_time[:6] + '45'
        submission_time = initial_time[:6] + '55'
    else:
        press_time_1 = initial_time[0:3] + str(int(initial_time[3:5])+1) + '44'
        press_time_2 = initial_time[0:3] + str(int(initial_time[3:5])+1) + '45'
        submission_time = initial_time[0:3] + str(int(initial_time[3:5])+1) + '55'
elif mode == 'moni':
    url = 'http://moni.51hupai.com/'
else:
    url = mode


# Specify a threshold
threshold = 0.75

def template_matching(img_gray, template_image):

    # Read the template
    template = cv2.imread(template_image,0)
 
    # Store width and heigth of template in w and h
    w, h = template.shape[::-1]
 
    # Perform match operations.
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

    # Store the coordinates of matched area in a numpy array
    loc = np.where( res >= threshold)
    #print(loc)
    if loc[0].size > 0:
        return loc[1][0], loc[0][0], w, h
    else:
        return 0, 0, w, h

def price_recognition(img_gray, template_image, relative_h, relative_w):
    loc1_x, loc1_y, w1, h1 = template_matching(img_gray, template_image)
    print("{}, {}, {}, {}".format(loc1_x, loc1_y, w1, h1))
    if loc1_x > 0:
        crop_img1 = img_gray[int(loc1_y+h1-h1*relative_h):loc1_y+h1, loc1_x+w1:int(loc1_x+w1+w1*relative_w)]
 #       cv2.imwrite('{}{}/{}_crop_{}.png'.format(my_dir, fn, fn, str(datetime.today()).replace(" ", "")), crop_img1)
        text1 = pytesseract.image_to_string(crop_img1, lang='eng', config = '-c tessedit_char_whitelist=0123456789')
        print(text1)
        text1_s = ''.join(i for i in text1 if i.isdigit())
        print(text1_s)
        for i in range(len(text1_s)):
            if text1_s[i] == "8" or text1_s[i] == "9":
                #print(i)
                text1_r = text1_s[i:]
                break
            else:
                text1_r = text1_s
        if len(text1_r) > 5:
            int_text1 = int(text1_r[0:5])
        elif len(text1_r) == 4:
            int_text1 = int(text1_r)*10
        elif len(text1_r) == 3:
            int_text1 = int(text1_r)*100
        else:
            int_text1 = int(text1_r)
        return int_text1


#url = 'http://moni.51hupai.com/'

#url1 = 'https://paimai.alltobid.com/'

#url2='https://paimai.alltobid.com/bid/2018091501/bid.htm'

url='https://paimai.alltobid.com/bid/b901b3c0ba414c3bb7c08761aedbff50/bid.htm'

y_shift = 0

x_shift = 0

#y_shift = -150

#x_shift = -150

#driver = webdriver.Ie("D:\\IEDriverServer.exe")
cap = DesiredCapabilities.INTERNETEXPLORER.copy()
cap['ignoreProtectedModeSettings'] = True
cap['ignoreZoomSetting'] = True
driver = webdriver.Ie(capabilities=cap)
driver.find_element_by_tag_name("html").send_keys(Keys.CONTROL, "0")
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

    month_today = str(datetime.today())   
    substitution = {".": "_", " ": "_", ":": "_"}
    month = replace(month_today, substitution)
#    month = month_today.replace(" ", "_")
#    month = '201905'
    directory = 'C:\Hupai\screenshot_{}/'.format(month)
    if not os.path.exists(directory):
    	os.makedirs(directory)
    
    	
    i = 0
    while i<1800:
        fn = "screen_{}".format(i)
        new_dir = directory + fn
        pyautogui.screenshot("{}.png".format(new_dir))
        img = cv2.imread(new_dir + '.png')
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)

        print("Round {}".format(i))
        # Convert it to grayscale
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #cv2.imwrite('{}_gray.png'.format(new_dir),img_gray)
    
        time.sleep(0.2)
    
        int_text1 = price_recognition(img_gray, 'template1.png', 1, 0.5)
        print(int_text1)
    
        int_text1a_pre = price_recognition(img_gray, 'template1a.png', 1, 0.3)
        if int_text1a_pre:
            int_text1a = int_text1a_pre + 300
        else:
            int_text1a = int_text1a_pre
        print(int_text1a)
    
        int_text1b = price_recognition(img_gray, 'template1b.png', 2.3, 1.5)
        print(int_text1b)
    
        if int_text1 == int_text1a or int_text1 == int_text1b:
            lowest_price = int_text1
        elif int_text1a == int_text1b:
            lowest_price = int_text1a
        elif int_text1:
            lowest_price = int_text1
        elif int_text1b:
            lowest_price = int_text1b
        else:
            lowest_price = int_text1a
    
        print("Lowest Transaction Pirce is {}".format(lowest_price))

#        area1 = (1144 + x_shift, 435 + y_shift, 1232 + x_shift, 465 + y_shift) # Lowest acceptable price
#        cropped_img1 = img.crop(area1)
#        cropped_img1.save('{}\{}_cropped1.png'.format(new_dir, fn))
#        text1 = pytesseract.image_to_string(cropped_img1, lang='eng', config = '-c tessedit_char_whitelist=0123456789')
#		if len(text1.replace(" ", "")) == 4:
#			int_text1 = int(text1.replace(" ", ""))*10
#		else:
#			int_text1 = int(text1)
#        lowest.append(text1)
#        #print(text1)
        utc = datetime.utcnow()
        print(utc)
        utc = utc.replace(tzinfo=from_zone)
        local = utc.astimezone(to_zone)
        text2 = datetime.strftime(local, "%H:%M:%S")
        #timeNow.append(text2)
        print(text2)
        print(lowest_price)
    	
        if text2 == press_time_1 or text2 == press_time_2:
    	#if text2 == "11:29:44" or text2 == "11:29:45":
            number_int = lowest_price +900
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
    	


        if (text2 >= submission_time):
            #print("Number is defined, and click the button") 
            pyautogui.moveTo(992 + x_shift, 855 + y_shift)
            pyautogui.click()
            pyautogui.moveTo(1140 + x_shift, 850 + y_shift)
            #pyautogui.moveTo(673, 455)
            pyautogui.click()
    	
        i +=1	
