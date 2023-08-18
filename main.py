# echo-server.py
import socket
import pyautogui
import subprocess


def recognize(MyText):
    if (MyText == "chrome"):
        subprocess.Popen(
            'C:\Program Files\Google\Chrome\Application\chrome.exe')

    elif (MyText.find('tap') >= 0):
        pyautogui.doubleClick()

    elif (MyText.find('select line') >= 0):
        pyautogui.keyDown('shiftleft')  # hold down the shift key
        pyautogui.keyDown('shiftright')

        pyautogui.press('end')

        pyautogui.keyUp('shiftright')
        pyautogui.keyUp('shiftleft')

    elif (MyText.find('down') >= 0):
        pyautogui.keyDown('shiftleft')  # hold down the shift key
        pyautogui.keyDown('shiftright')

        pyautogui.press('down', presses=5, interval=0.1)

        pyautogui.keyUp('shiftleft')
        pyautogui.keyUp('shiftright')

    elif (MyText.find('copy') >= 0):
        pyautogui.hotkey('ctrl', 'c')

    elif (MyText.find('best') >= 0):
        pyautogui.hotkey('ctrl', 'v')

    elif (MyText.find('back') >= 0):
        pyautogui.hotkey('ctrl', 'z')

    elif (MyText.find('cut') >= 0):
        pyautogui.hotkey('del')


HOST = "192.168.1.6"  # Standard loopback interface address (localhost)
PORT = 8000  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            print(data)
            data = data.decode('utf-8')

            splitdata = data.split('\r\n')
            print(splitdata)

            if( len(splitdata[-1]) > 0 ):
                extractedEquation = splitdata[-1].split('=')
                commandText = extractedEquation[1].replace("+", " ")
                recognize(commandText)
