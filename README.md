# hupai-win

### Bootstrapping steps:
* Download http://selenium-release.storage.googleapis.com/2.39/IEDriverServer_x64_2.39.0.zip, unzip it and add its folder (such as C:\Users\xxxx\Downloads) to PATH
* IE -> Internet Options -> Security -> Make sure that all the zones have the same Protected Mode setting
* IE -> Internet Options -> Advanced -> Make sure the Enhanced Protected Mode is turned off
* Opened regedit, created HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BFCACHE and create a DWORD value named iexplore.exe with the value of 0.
* Download Python3.7 from https://www.python.org/ftp/python/3.7.2/python-3.7.2-amd64.exe, and Run as Admin to install it (Select Adding it the PATH during the installation)
* Download https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v4.0.0.20181030.exe and install it
* Add C:\Program Files (x86)\Tesseract-OCR\tessdata to two environment variables, PATH and TESSDATA_PREFIX 
* Right click CMD or Powershell, run it as Admin and then```pip3 install pyautogui Pillow pytesseract pandas selenium opencv-python python-dateutil``` or ```python3 -m pip install pyautogui Pillow pytesseract pandas selenium opencv-python python-dateutil```
* Download https://ftp.nluug.nl/pub/vim/pc/gvim81.exe and install for editing purpose. Need to add C:\Program Files (x86)\Vim\vim81to PATH. 
* To enable Adobe Flash, run As Admin: dism /online /add-package /packagepath:"C:\Windows\servicing\Packages\Adobe-Flash-For-Windows-Package~31bf3856ad364e35~amd64~~10.0.14393.0.mum" Then reboot.

### How to run?
If we would like to run it in moni, `python3 hupai_win.py`; if we would like to run it in real case, recover the line that defines url and `python3 hupai_win.py`. The other way is `python3 hupai_win.py url_xxx`
