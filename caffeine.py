import time
import keyboard
import subprocess

notepadOpened = False
i = 0

def openNotepad():
    programName = "notepad.exe"
    fileName = "caffeine.txt"
    global notepadOpened
    notepadOpened = True
    subprocess.Popen([programName, fileName])

def closeNotePad():
    if (notepadOpened):
        subprocess.call(["taskkill", "/F", "/IM", "notepad.exe"])
    else:
        print("notepad not opened")

def useKeyboard():
    keyboard.press('a')
    global i
    i += 1

def main():
    openNotepad()
    while(1):
        time.sleep(60)
        useKeyboard()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        closeNotePad()
        print("you were asleep for " + str(i) + " minutes")