try:
    import Image
except ImportError:
    from PIL import Image
import win32clipboard, win32con
import pyautogui
import pytesseract
import threading
import time
import locale
from datetime import datetime
from win32api import GetSystemMetrics
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract\Tesseract-OCR\tesseract'
done_trade = False
assets = ""
time_to = ""
def read_email_from_gmail(tp_value,sl_value, trade_amount, balance,file_path):
    # try:EURJPY
    print(tp_value,sl_value, trade_amount,'while', balance)
    try:
        win32clipboard.OpenClipboard()
    except Exception as e:
        raise e

    
    

    #print(win32clipboard.IsClipboardFormatAvailable(win32con.CF_UNICODETEXT))
    if win32clipboard.IsClipboardFormatAvailable(win32con.CF_UNICODETEXT):
        try:
            data = win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)#copy clipboard data
        except (TypeError, win32clipboard.error):
            try:
                data = win32clipboard.GetClipboardData(win32con.CF_TEXT)
            except Exception as e:
                data=""
        finally:
            if win32clipboard.OpenClipboard() != None:
                win32clipboard.CloseClipboard()


    #f = open("C:\\Users\\RasmerWindows\\AppData\\Roaming\\MetaQuotes\\Terminal\\76AE827A66F7801B9D79B1FD1D2103FD\\MQL4\\Files\\Data\\CobraAlert.txt", "r")
   # print(f.readline())
        #for x in data:
        print(data,'data')
        if data != "":
            global done_trade
            global assets
            global time_to
          
            
            row = data.split(",")
            #print(row)
            #try:
            time_sig = row[2].split(":")
            time_sig = time_sig[0]+":"+time_sig[1]
            date_sig = row[1].split(".")
            date_sig = date_sig[0]+"-"+date_sig[1]+"-"+date_sig[2]
            print( str(datetime.now().date())==date_sig, data)
            # time_sig = "16:23"
           # print( row[3] == assets , time_to == time_sig,time_sig,time_to, assets,done_trade,done_trade,"time check", datetime.now().time().strftime("%H:%M") == time_sig,  datetime.now().time().strftime("%H:%M") ,time_sig)
            print(done_trade and row[3] == assets and time_to == time_sig,'check')
            if done_trade and row[3] == assets and time_to == time_sig:
                pass
            else:
                print( str(datetime.now().date()), date_sig , datetime.now().time().strftime("%H:%M") , time_sig , row[7] in ['50.00%', '61.80%', '78.60%'],'before type')
                if  str(datetime.now().date()) == date_sig and datetime.now().time().strftime("%H:%M") == time_sig and row[7] in ['50.00%', '61.80%', '78.60%']:
                    #print(row[3],datetime.now().time().strftime("%H:%M") , time_sig)
                    pyautogui.click(215, 145)
                    pyautogui.typewrite(row[3], interval=0.05)
                    pyautogui.click(445, 150)
                    time.sleep(0.6)
                    pyautogui.click(x=1310, y=210)
                    pyautogui.click(x=1310, y=210)
                    pyautogui.click(x=1310, y=210)
                    pyautogui.typewrite(trade_amount, interval=0.05)
                    if row[8] != "M1":
                        pyautogui.click(x=1310, y=145)
                        time.sleep(0.2)
                        if row[8] == "M5":
                            pyautogui.click(x=999, y=360)
                        elif row[8] == "M15":
                            pyautogui.click(x=1165, y=230)
                        elif row[8] == "M30":
                            pyautogui.click(x=1165, y=260)      

                    pyautogui.click()
                    time.sleep(0.6)
                    mt4_file_path = file_path#"C:\\Users\\RasmerWindows\\AppData\\Roaming\\MetaQuotes\\Terminal\\76AE827A66F7801B9D79B1FD1D2103FD\\MQL4\\Files\\Data\\"
                    f = open(mt4_file_path+row[3]+".txt", "r")
                    price_strike = f.readline()
                    f.close()
                    print(price_strike,row[4], price_strike <= row[4], 'put', price_strike >=row[4])
                    clicked = False
                    if row[5] == "CALL":
                        if price_strike <= row[4]:
                            pyautogui.moveTo(1310, 445)
                            pyautogui.click()
                            clicked = True
                    elif row[5] == "PUT":
                        if price_strike >=row[4]:
                            pyautogui.moveTo(1310, 560)
                            pyautogui.click()
                            clicked = True
                    if clicked:
                        done_trade = True
                        assets  = row[3]
                        time_to = time_sig
                        print(done_trade, assets, time_to)
                    else:
                        done_trade = False
                        assets = ""
                        time_to = ""
            # except:
            #     pass
        

#thread.start_new_thread(read_email_from_gmail())           

class ThreadingExample(object):

    def __init__(self, tp_value,sl_value,trade_amount,file_path, interval=1):
       
        self.tp_val = trade_amount
        self.sl_val = sl_value
        self.t_amount = trade_amount
        self.file_path = file_path
        print(self.tp_val,self.sl_val,self.t_amount,self.file_path,'init')
        self.interval = interval
         # Take screenshot
        self.pic = pyautogui.screenshot(region=(980,20, 250, 70))
        # Save the image
        self.pic.save('Screenshot.tif') 
        if self.get_iq_balance() == "not_found":
             pass
        elif self.get_iq_balance() == "less_than":
            pass
        #elif self.get_iq_balance() >= 1:
        self.thread = threading.Thread(target=self.run, args=())
        self.thread.daemon = False                            # Daemonize thread
        self.thread.start()                                  # Start the execution

    def run(self):
        
       
        # pyautogui.click(x=1310, y=210)
        # pyautogui.click(x=1310, y=210)
        # pyautogui.click(x=1310, y=210)
        # pyautogui.typewrite(self.t_amount, interval=0.05)
        
        """ Method that runs forever """
        while True : 
            read_email_from_gmail(self.tp_val,self.sl_val,self.t_amount,self.get_iq_balance(),self.file_path)  

            time.sleep(self.interval)

    def end(self):
        print(self.thread.is_alive(),'asdasdasdas')
        if self.thread.is_alive():
            self.thread.abort()
        
            '''this function not yet ready,'''
    def get_iq_balance(self):
        self.pic = pyautogui.screenshot(region=(980,20, 250, 70))
        # Save the image
        self.pic.save('Screenshot.tif') 
        self.image_string=pytesseract.image_to_string(Image.open('Screenshot.tif'), lang='eng', boxes=False)
        self.image_string = self.image_string.split(" ")
        print(self.image_string,'get_balance')
        self.balance =[self.s for self.s in self.image_string if "$" in self.s]
        if self.balance:
           # print(self.balance,'sss')
            #print(balance[0].replace("$", ""), "sadasd")
            self.balance = re.sub('[^0-9]', "", self.balance[0])
            #print(self.balance)
            self.balance =  float(self.balance)/100
            
            if float(self.balance) <= 1:
                return 'less_than'
            if float(self.balance) >= 1:
                return float(self.balance)
            else:
                return "not_found"
        else:
            return "not_found"


# if GetSystemMetrics(0) == 1366 and GetSystemMetrics(1) == 768:
#     print("Width =", GetSystemMetrics(0))
#     print("Height =", GetSystemMetrics(1))
#     example = ThreadingExample() 
#     # while datetime.now().hour <= 24:
#     #     read_email_from_gmail()
# else:
#     print("Error!!! Screen Display not meet the 1366x768:"+GetSystemMetrics(0)+"x"+GetSystemMetrics(1))

