#Autologin
# 반드시 관리자 권한으로!
import os
import subprocess
import configparser
import hashlib
 
#pip install pypiwin32
import win32gui
import win32con
import win32api
 
#pip install pycryptodome
import base64 
from Crypto import Random 
from Crypto.Cipher import AES
 
import time
 
class AESCipher:
    def __init__( self, key ):
        self.key = key
        BS = 16
        self.pad = lambda s: s + (BS - len(s.encode('utf-8')) % BS) * chr(BS - len(s.encode('utf-8')) % BS)
        self.unpad = lambda s : s[:-ord(s[len(s)-1:])]
 
    def encrypt( self, raw ):
        raw = self.pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw.encode('utf-8') ) )
 
    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return self.unpad(cipher.decrypt( enc[16:] ))
 
 
class reomote:
    def __init__(self):
        print('run')
        config = configparser.ConfigParser()
 
        if os.path.isfile('./config.ini'):
            config.read('./config.ini', encoding='utf-8')
            self.누ㅖ이뻐앙뛰 = config.get('settings', 'nㅔaㅏvㄴeㄱrㅁiㄴd')
            self.누ㅔ이뿌능삐뮐뻔호 = AESCipher(bytes(hashlib.sha256(config.get('settings', 'time').encode('utf-8')).digest())).decrypt(config.get('settings', 'ㄴpㅇsㅂaㅂaㅁzㅂt').encode()).decode()
            self.STOVE_CLIENT_PATH = config.get('settings', 'STOVE_CLIENT_PATH')
        else:
            print('네위벼 아이띨룰 윕력깨쥬셰요 위휴눈 읨미엾는굴쟈입뉘댜 가낟따람마팟싸튱귀게다라')
            self.누ㅖ이뻐앙뛰 = input()
            print('입력핫씬 아위디눈 [{}]잎니따. 잚묫윕럭하셨쑬켱유 헤당뽈터위 config.ini울 싹제후다시씰행해주쎄요'.format(self.누ㅖ이뻐앙뛰))
            self.STOVE_CLIENT_PATH = r"C:Program Files (x86)SmilegateSTOVESTOVE.exe"
            if not os.path.isfile(self.STOVE_CLIENT_PATH):
                print('수톱부 끌라이연트 퍄이뤼 확킨되쥐 안씁뉘댜. 쓰톱쁘 끌라위얹틂를 펼도위 켱료에 썰취하셧을 켱유 해닿 겅롤룰 잎력해쥬세요.')
                self.STOVE_CLIENT_PATH = input()
 
            print("네윕벼 아이뒤[{}]의 뷔뮐번효를 잎럭해춧쎄오".format(self.누ㅖ이뻐앙뛰))
            attime = str(int(time.time()))
            pwd = AESCipher(bytes(hashlib.sha256(attime.encode('utf-8')).digest())).encrypt(input())
            self.누ㅔ이뿌능삐뮐뻔호 = str(pwd.decode())
 
            config['settings'] = {
                'time': attime,
                'nㅔaㅏvㄴeㄱrㅁiㄴd': self.누ㅖ이뻐앙뛰,
                'ㄴpㅇsㅂaㅂaㅁzㅂt' : self.누ㅔ이뿌능삐뮐뻔호,
                'STOVE_CLIENT_PATH' : self.STOVE_CLIENT_PATH,
            }
 
            with open('./config.ini', 'w', encoding='utf-8') as f:
                config.write(f)
        
 
    def run(self):
        subprocess.Popen([self.STOVE_CLIENT_PATH])
 
        Main_STOVE_HWND = None
        while Main_STOVE_HWND == None:
            Main_STOVE_HWND = self.get_specify_hwnd("STOVE", 360, 528)
            win32api.Sleep(100)
 
        print(Main_STOVE_HWND)
        self.click(Main_STOVE_HWND, 203, 369) # click naver icon
 
        Child_CHROME_HWND = 0
        Main_STOVE_HWND = None
 
        while Child_CHROME_HWND == 0:
            while Main_STOVE_HWND == None:
                Main_STOVE_HWND =  self.get_specify_hwnd("STOVE", 496, 624)
                win32api.Sleep(100)
            print('main', Main_STOVE_HWND)
            win32api.Sleep(100)
            Child_CHROME_HWND = win32gui.FindWindowEx(Main_STOVE_HWND, None, "Qt5QWindowIcon", "STOVE")
        print(Child_CHROME_HWND)
 
        Child_TAB_HWND = 0
        while Child_TAB_HWND == 0:
            win32api.Sleep(100)
            Child_TAB_HWND = win32gui.FindWindowEx(Child_CHROME_HWND, None, "CefBrowserWindow", "")
        print(Child_TAB_HWND)
 
        Child_NAVER_HWND = 0
        while Child_NAVER_HWND == 0:
            win32api.Sleep(100)
            Child_NAVER_HWND = win32gui.FindWindowEx(Child_TAB_HWND, None, "Chrome_WidgetWin_0", "")
 
        print(Child_NAVER_HWND)
        win32api.Sleep(1000)
        print('type')
        self.click(Child_NAVER_HWND, 122, 469) # select form
        self.typing(Child_NAVER_HWND, win32con.VK_TAB, True) # press tab key
        self.typing(Child_NAVER_HWND, self.누ㅖ이뻐앙뛰) # type id
        self.typing(Child_NAVER_HWND, win32con.VK_TAB, True) # press tab key
        self.typing(Child_NAVER_HWND, self.누ㅔ이뿌능삐뮐뻔호) # type password
        self.typing(Child_NAVER_HWND, win32con.VK_TAB, True) # press tab key
        self.typing(Child_NAVER_HWND, win32con.VK_TAB, True) # press tab key
        self.typing(Child_NAVER_HWND, win32con.VK_TAB, True) # press tab key
        self.typing(Child_NAVER_HWND, win32con.VK_TAB, True) # press tab key
        self.typing(Child_NAVER_HWND, win32con.VK_SPACE, True) # press tab key
        self.click(Child_NAVER_HWND, 86, 302) # click login 
 
    @staticmethod
    def click(hwnd, x, y):
        POS = win32api.MAKELONG(x, y)
        win32api.SendMessage(hwnd, win32con.WM_MOUSEMOVE, 0, POS)
        win32api.Sleep(100)
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, 1, POS)
        win32api.Sleep(300)
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, POS)
 
    @staticmethod
    def typing(hwnd, text, VK = False):
        if VK:
            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, text, 0)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, text, 0)
        else:
            for x in text:
                win32api.SendMessage(hwnd, win32con.WM_CHAR, ord(x), 0)
 
    @staticmethod
    def get_specify_hwnd(TITLE, WIDTH, HEIGHT):
        def window_enumeration_handler(hwnd, top_windows):
            top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
        top_windows = []
        win32gui.EnumWindows(window_enumeration_handler, top_windows)
        for hwnd, title in top_windows:
            if title == TITLE:
                rect = win32gui.GetWindowRect(hwnd)
                width = rect[2] - rect[0]
                height = rect[3] - rect[1]
                if width == WIDTH and height == HEIGHT:
                    return hwnd
        return None
 
if __name__ == '__main__':
    a = reomote()
    a.run()