#!/usr/bin/python3
# -*- coding: utf8 -*-

# ======================================================================
#       ISHIDA GO TANAHAKARI Download for P-1192 Auther @yaku
#       2023.11.26 Ver1.0
#       https://github.com/ShigeoYakuno
# ======================================================================

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
from threading import Event

from public import *
from tkinter import filedialog
from time import sleep
from CanDrv import CanDrv
import os
import sys

con_ch = 0
sta_ch = 0
data_ch = 0
retry_cnt = 0
send_cnt = 0
exit_flg = 0
finish_flg = 0
tgl_val = 1
data_cnt = 0

can = CanDrv()
event = Event()


# ======================================================================
#      Button func
# ======================================================================
def canopen():
    can.open()
    return


def canclose():
    can.close()
    return


def exit_exec():
    canclose()
    sleep(1)
    sys.exit()


# ======================================================================
#      can recieve thread
# ======================================================================
def can_rx():
    global sta_ch
    global con_ch
    global data_ch
    global finish_flg

    global retry_cnt
    global tgl_val
    global data_cnt

    while True:
        msg = can.receive()

        if msg is not None:
            # if((msg.arbitration_id & 0xFFFF0000) == 0x10000000):
            #    id = root.after(100, ResponseCheck)
            #    return

            sour = (msg.arbitration_id & 0x0400) >> 10
            ch = (msg.arbitration_id & 0x03F0) >> 4
            cmd = msg.arbitration_id & 0x000F

            if sour == 1:
                can_txt = f"{hex(msg.arbitration_id)}:{hex(msg.data[7])}:{hex(msg.data[6])}:{hex(msg.data[5])}:{hex(msg.data[4])}:{hex(msg.data[3])}:{hex(msg.data[2])}:{hex(msg.data[1])}:{hex(msg.data[0])}"
                print(can_txt)

                # connect ack
                if cmd == 0x000A:
                    debug1_exec(ch)
                    temp_ch = 1 << (ch - 1)
                    con_ch |= temp_ch
                    print(f"connect ch {bin(con_ch)}")

                # start ack
                if cmd == 0x000B:
                    debug2_exec(ch)
                    temp_ch = 1 << (ch - 1)
                    sta_ch |= temp_ch

                    # Unwait task on match
                    if con_ch == sta_ch:
                        messagebox.showinfo(
                            "Info", "Downloading start! Do not turn off the system! "
                        )
                        event.set()
                    else:
                        print(f"FWUP WAIT...connect{bin(con_ch)} respose{bin(sta_ch)}")

                # data ack
                if cmd == 0x000C:
                    debug_tgl_exec(ch)
                    temp_ch = 1 << (ch - 1)
                    data_ch |= temp_ch

                    # Unwait task on match
                    if con_ch == data_ch:
                        data_ch = 0  # clear
                        tgl_val = tgl_val + 1
                        tgl_val = tgl_val % 2
                        data_cnt = data_cnt + 1
                        event.set()

                # fin ack
                if cmd == 0x000F:
                    debug3_exec(ch)
                    temp_ch = 1 << (ch - 1)
                    data_ch |= temp_ch

                    # Unwait task on match
                    if con_ch == data_ch:
                        finish_flg = 1
                        messagebox.showinfo("Info", "PROGRAM DOWNLOAD IS COMPLATE!")
                        print(f"FW UPDATE FINISH {data_cnt}")

            # can_rx thread end


# ======================================================================
#       Button func
# ======================================================================
def connect_func():
    os.system("cansend can0 3FA#3030303030303030")  # 011 1111 1010


def start_func():
    os.system("cansend can0 3FB#3030303030303030")


def finish_func():
    os.system("cansend can0 3FF#3030303030303030")


def boot_func():
    os.system("cansend can0 3F3#4D56000000000000")


# ======================================================================
#      lda thread
# ======================================================================
def lda_main():
    global num_lines
    global pb
    global exit_flg

    while True:
        print("connect check...")
        event.wait()  #
        event.clear()  # clear is important!

        typ = [("MOT", "*.mot")]
        # dir = 'D:\workspace23E\P-1192\Z1192\P1192_CS+\output'
        dir = "/home/ishida/digi_yata/program"
        fle = filedialog.askopenfilename(filetypes=typ, initialdir=dir)

        num_lines = len(open(fle).readlines())
        # print(num_lines)

        print("connect OK")

        with open(fle) as f:
            for line in f:
                # print(line)

                if line.find("S0", 0, 2) != -1:
                    pass

                elif line.find("S7", 0, 2) != -1:
                    pass

                elif (line.find("S3", 0, 2) != -1) and (line.find("FFFFF", 4, 9) != -1):
                    pass

                elif line.find("S9", 0, 2) != -1:
                    finish_func()
                    exit_flg = 1

                elif line.find("S3", 0, 2) != -1:
                    temp_data1 = line[12:28]
                    temp_data2 = line[28:44]

                    print(temp_data1)
                    bytes.fromhex(temp_data1)  # hexstr change byte
                    os.system("cansend can0 3FC#" + temp_data1)

                    event.wait()  # CAN recv wait
                    event.clear()

                    print(temp_data2)
                    bytes.fromhex(temp_data2)
                    os.system("cansend can0 3FC#" + temp_data2)

                    event.wait()
                    event.clear()

                countUp()
                sleep(0.001)


# ======================================================================
#       debug func
# ======================================================================
def countUp():
    global var
    global num_lines
    global pb

    lines = var.get()

    pb.configure(value=lines + 1 / num_lines)
    pb.update()
    var.set(lines + 1)

    # if lines == (num_lines -1):
    #   messagebox.showinfo("Info","PROGRAM DOWNLOAD IS COMPLATE!")


def debug1_exec(num):
    if num > 30:
        return
    canvas.itemconfig(ch_obj[num - 1], fill="red")


def debug2_exec(num):
    if num > 30:
        return
    canvas.itemconfig(ch_obj[num - 1], fill="yellow")


def debug3_exec(num):
    if num > 30:
        return
    canvas.itemconfig(ch_obj[num - 1], fill="green2")


def debug_tgl_exec(num):
    global tgl_val

    if num > 30:
        return

    if tgl_val == 1:
        canvas.itemconfig(ch_obj[num - 1], fill="pink3")
    else:
        canvas.itemconfig(ch_obj[num - 1], fill="pink4")


# ======================================================================
#      main thread
# ======================================================================
def main():
    global root
    global var
    global pb

    tk.Button(root, text="START", command=start_func).place(x=100, y=200)
    tk.Button(root, text="CONNECT", command=connect_func).place(x=200, y=200)
    tk.Button(root, text="BOOT", command=boot_func).place(x=300, y=200)
    tk.Button(root, text="EXIT", command=exit_exec).place(x=800, y=200)

    # Progressbar
    pb = ttk.Progressbar(
        root, length=PROG_BAR, maximum=1800, mode="determinate", variable=var
    )
    pb.place(x=10, y=100)

    var.set(0)

    canopen()

    sleep(0.5)

    lda_tsk = threading.Thread(target=lda_main, daemon=True)
    lda_tsk.start()

    can_rx_tsk = threading.Thread(target=can_rx, daemon=True)
    can_rx_tsk.start()

    root.mainloop()

    # thread end
    lda_tsk.join()
    can_rx_tsk.join()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1280x600")
    root.title("DOWNLOAD TOOL FOR P-1192")
    var = tk.IntVar()

    canvas = tk.Canvas(root, width=1280, height=300, bg="white")
    canvas.place(x=0, y=300)

    for num in range(GOUKI_MAX):
        if num < 10:
            ch_obj[num] = canvas.create_oval(
                50 + (num * 100), 50, 100 + (num * 100), 100, fill="gray"
            )
        elif num < 20:
            ch_obj[num] = canvas.create_oval(
                50 + ((num - 10) * 100), 140, 100 + ((num - 10) * 100), 190, fill="gray"
            )
        else:
            ch_obj[num] = canvas.create_oval(
                50 + ((num - 20) * 100), 230, 100 + ((num - 20) * 100), 280, fill="gray"
            )

    main()
