import os
import threading

def open_notepad():
    os.system("notepad")

def open_calc():
    os.system("calc")
    
# x = threading.Thread(target=open_notepad)
# x.start()
# y = threading.Thread(target=open_calc)
# y.start()

open_calc()
open_notepad()