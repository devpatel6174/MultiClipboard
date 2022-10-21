# Made by Dev Patel (devpatel@gatech.edu)


import pyperclip
from pynput import keyboard

clipboard = [0 for i in range(10)]

def copy_0():
    clipboard[0] = pyperclip.paste()
    
def copy_1():
    clipboard[1] = pyperclip.paste()
    
def copy_2():
    clipboard[2] = pyperclip.paste()
    
def copy_3():
    clipboard[3] = pyperclip.paste()
    
def copy_4():
    clipboard[4] = pyperclip.paste()
    
def copy_5():
    clipboard[5] = pyperclip.paste()
    
def copy_6():
    clipboard[6] = pyperclip.paste()
    
def copy_7():
    clipboard[7] = pyperclip.paste()
    
def copy_8():
    clipboard[8] = pyperclip.paste()
    
def copy_9():
    clipboard[9] = pyperclip.paste()

def paste_0():
    pyperclip.copy(clipboard[0])
    
def paste_1():
    pyperclip.copy(clipboard[1])
    
def paste_2():
    pyperclip.copy(clipboard[2])
    
def paste_3():
    pyperclip.copy(clipboard[3])
    
def paste_4():
    pyperclip.copy(clipboard[4])
    
def paste_5():
    pyperclip.copy(clipboard[5])
    
def paste_6():
    pyperclip.copy(clipboard[6])
    
def paste_7():
    pyperclip.copy(clipboard[7])
    
def paste_8():
    pyperclip.copy(clipboard[8])
    
def paste_9():
    pyperclip.copy(clipboard[9])
    

with keyboard.GlobalHotKeys({
'<cmd>+<ctrl>+0' : copy_0,
'<cmd>+<ctrl>+1' : copy_1,
'<cmd>+<ctrl>+2' : copy_2,
'<cmd>+<ctrl>+3' : copy_3,
'<cmd>+<ctrl>+4' : copy_4,
'<cmd>+<ctrl>+5' : copy_5,
'<cmd>+<ctrl>+6' : copy_6,
'<cmd>+<ctrl>+7' : copy_7,
'<cmd>+<ctrl>+8' : copy_8,
'<cmd>+<ctrl>+9' : copy_9,
'<cmd>+0' : paste_0,
'<cmd>+1' : paste_1,
'<cmd>+2' : paste_2,
'<cmd>+3' : paste_3,
'<cmd>+4' : paste_4,
'<cmd>+5' : paste_5,
'<cmd>+6' : paste_6,
'<cmd>+7' : paste_7,
'<cmd>+8' : paste_8,
'<cmd>+9' : paste_9}) as h:
    h.join()



