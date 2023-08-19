# echo-server.py
import socket
import pyautogui
import subprocess


def recognize(MyText):
    print(MyText)
    if( MyText[:5] == "right" ):
        wordToWrite = MyText[6:].replace(' dot ','.') 
        pyautogui.write(wordToWrite)

    if (MyText == "chrome"):
        subprocess.Popen(
            'C:\Program Files\Google\Chrome\Application\chrome.exe')

    if (MyText.find('tap') >= 0):
        pyautogui.doubleClick()

    if (MyText.find('select line') >= 0):
        pyautogui.keyDown('shiftleft')  # hold down the shift key
        pyautogui.keyDown('shiftright')

        pyautogui.press('down')

        pyautogui.keyUp('shiftright')
        pyautogui.keyUp('shiftleft')

    if (MyText.find('down') >= 0):
        pyautogui.keyDown('shiftleft')  # hold down the shift key
        pyautogui.keyDown('shiftright')

        pyautogui.press('down', presses=5, interval=0.1)

        pyautogui.keyUp('shiftleft')
        pyautogui.keyUp('shiftright')

    if (MyText.find('copy') >= 0):
        print("copy")
        pyautogui.hotkey('ctrl', 'c')

    if (MyText.find('best') >= 0):
        
        pyautogui.hotkey('ctrl', 'v')
    
    if (MyText.find('paste') >= 0):
        pyautogui.keyDown('shiftleft')  # hold down the shift key
        pyautogui.keyDown('shiftright')

        pyautogui.hotkey('ctrl', 'v')

        pyautogui.keyUp('shiftright')
        pyautogui.keyUp('shiftleft')
        

    if (MyText.find('back') >= 0):
        pyautogui.hotkey('ctrl', 'z')

    if (MyText.find('cut') >= 0):
        pyautogui.hotkey('del')


HOST = "192.168.1.6"  # Standard loopback interface address (localhost)
PORT = 8000  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    
    # with conn:
    #     print(f"Connected by {addr}")
    while True:
        conn, addr = s.accept()
        
        data = conn.recv(1024)
        print(data)
        data = data.decode('utf-8')

        splitdata = data.split('\r\n')
        print(splitdata)

        if( len(splitdata[-1]) > 0 ):
            extractedEquation = splitdata[-1].split('=')
            commandText = extractedEquation[1].replace("+", " ")
            recognize(commandText)
