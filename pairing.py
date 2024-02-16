#!/usr/bin/python3
# -*- coding: utf8 -*-

# ======================================================================
#       ISHIDA GO TANAHAKARI pairing Scales    Auther @yaku
#       2023.11.22 Ver1.0
#       https://github.com/ShigeoYakuno
# ======================================================================

import tkinter as tk
import threading
from threading import Event
from public import *
from time import sleep
from CanDrv import CanDrv
import os
import sys

BTN_X = 55
BTN_Y = 20
Y_OFS = 90

con_ch = 0
sta_ch = 0
data_ch = 0
retry_cnt = 0
send_cnt = 0
exit_flg = 0
finish_flg = 0

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


def exit_exec2():
    global exit_flg
    exit_flg = 1

    sleep(2)
    sys.exit()


# ======================================================================
#      can recieve thread
# ======================================================================
def can_rx():
    global exit_flg

    while True:
        msg = can.receive()

        if exit_flg == 1:
            canclose()
            return

        if msg is not None:
            can_txt = f"{hex(msg.arbitration_id)}:{hex(msg.data[0])}:{hex(msg.data[1])}:{hex(msg.data[2])}:{hex(msg.data[3])}:{hex(msg.data[4])}:{hex(msg.data[5])}:{hex(msg.data[6])}:{hex(msg.data[7])}"
            print(can_txt)

            if msg.arbitration_id == 0x7F8:
                local_ch = msg.data[0]
                debug1_exec(local_ch)
                print("OK")


# ======================================================================
#      pairing func
# ======================================================================
def pairing_func(num):
    os.system("cansend can0 3F7#" + str(format(num, "02X")) + "30303030303030")
    print(f"pairing {num}")


def pairing_end_func():
    os.system("cansend can0 3F8#3030303030303030")


# ======================================================================
#      debug func
# ======================================================================
def debug1_exec(num):
    if num > 30:
        return
    print(num)
    canvas.itemconfig(ch_obj[num - 1], fill="red")


def debug2_exec(num):
    if num > 30:
        return
    canvas.itemconfig(ch_obj[num - 1], fill="yellow")


def debug_tgl_exec(num):
    if num > 30:
        return
    canvas.itemconfig(ch_obj[num - 1], fill="blue")


# ======================================================================
#      main thread
# ======================================================================
def main():
    global root
    global var
    global pb

    tk.Button(root, text="EXIT", command=exit_exec).place(x=1100, y=100)
    tk.Button(root, text="STOP", command=pairing_end_func).place(x=1100, y=200)

    canopen()

    sleep(0.5)

    can_rx_tsk = threading.Thread(target=can_rx, daemon=True)
    can_rx_tsk.start()

    root.mainloop()

    # thread end
    can_rx_tsk.join()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1280x300")
    root.title("PAIRING TOOL FOR P-1192")
    var = tk.IntVar()

    canvas = tk.Canvas(root, width=1280, height=300, bg="white")
    canvas.place(x=0, y=0)

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

    tk.Button(root, text="SET", command=lambda: pairing_func(1)).place(
        x=BTN_X + (0 * 100), y=BTN_Y
    )
    tk.Button(root, text="SET", command=lambda: pairing_func(2)).place(
        x=BTN_X + (1 * 100), y=BTN_Y
    )
    tk.Button(root, text="SET", command=lambda: pairing_func(3)).place(
        x=BTN_X + (2 * 100), y=BTN_Y
    )
    tk.Button(root, text="SET", command=lambda: pairing_func(4)).place(
        x=BTN_X + (3 * 100), y=BTN_Y
    )
    tk.Button(root, text="SET", command=lambda: pairing_func(5)).place(
        x=BTN_X + (4 * 100), y=BTN_Y
    )
    tk.Button(root, text="SET", command=lambda: pairing_func(6)).place(
        x=BTN_X + (5 * 100), y=BTN_Y
    )
    tk.Button(root, text="SET", command=lambda: pairing_func(7)).place(
        x=BTN_X + (6 * 100), y=BTN_Y
    )
    tk.Button(root, text="SET", command=lambda: pairing_func(8)).place(
        x=BTN_X + (7 * 100), y=BTN_Y
    )
    tk.Button(root, text="SET", command=lambda: pairing_func(9)).place(
        x=BTN_X + (8 * 100), y=BTN_Y
    )
    tk.Button(root, text="SET", command=lambda: pairing_func(10)).place(
        x=BTN_X + (9 * 100), y=BTN_Y
    )

    tk.Button(root, text="SET", command=lambda: pairing_func(11)).place(
        x=BTN_X + (0 * 100), y=BTN_Y + Y_OFS
    )
    tk.Button(root, text="SET", command=lambda: pairing_func(12)).place(
        x=BTN_X + (1 * 100), y=BTN_Y + Y_OFS
    )
    tk.Button(root, text="SET", command=lambda: pairing_func(13)).place(
        x=BTN_X + (2 * 100), y=BTN_Y + Y_OFS
    )
    tk.Button(root, text="SET", command=lambda: pairing_func(14)).place(
        x=BTN_X + (3 * 100), y=BTN_Y + Y_OFS
    )
    tk.Button(root, text="SET", command=lambda: pairing_func(15)).place(
        x=BTN_X + (4 * 100), y=BTN_Y + Y_OFS
    )
    tk.Button(root, text="SET", command=lambda: pairing_func(16)).place(
        x=BTN_X + (5 * 100), y=BTN_Y + Y_OFS
    )
    tk.Button(root, text="SET", command=lambda: pairing_func(17)).place(
        x=BTN_X + (6 * 100), y=BTN_Y + Y_OFS
    )
    tk.Button(root, text="SET", command=lambda: pairing_func(18)).place(
        x=BTN_X + (7 * 100), y=BTN_Y + Y_OFS
    )
    tk.Button(root, text="SET", command=lambda: pairing_func(19)).place(
        x=BTN_X + (8 * 100), y=BTN_Y + Y_OFS
    )
    tk.Button(root, text="SET", command=lambda: pairing_func(20)).place(
        x=BTN_X + (9 * 100), y=BTN_Y + Y_OFS
    )

    tk.Button(root, text="SET", command=lambda: pairing_func(21)).place(
        x=BTN_X + (0 * 100), y=BTN_Y + Y_OFS * 2
    )
    tk.Button(root, text="SET", command=lambda: pairing_func(22)).place(
        x=BTN_X + (1 * 100), y=BTN_Y + Y_OFS * 2
    )
    tk.Button(root, text="SET", command=lambda: pairing_func(23)).place(
        x=BTN_X + (2 * 100), y=BTN_Y + Y_OFS * 2
    )
    tk.Button(root, text="SET", command=lambda: pairing_func(24)).place(
        x=BTN_X + (3 * 100), y=BTN_Y + Y_OFS * 2
    )
    tk.Button(root, text="SET", command=lambda: pairing_func(25)).place(
        x=BTN_X + (4 * 100), y=BTN_Y + Y_OFS * 2
    )
    tk.Button(root, text="SET", command=lambda: pairing_func(26)).place(
        x=BTN_X + (5 * 100), y=BTN_Y + Y_OFS * 2
    )
    tk.Button(root, text="SET", command=lambda: pairing_func(27)).place(
        x=BTN_X + (6 * 100), y=BTN_Y + Y_OFS * 2
    )
    tk.Button(root, text="SET", command=lambda: pairing_func(28)).place(
        x=BTN_X + (7 * 100), y=BTN_Y + Y_OFS * 2
    )
    tk.Button(root, text="SET", command=lambda: pairing_func(29)).place(
        x=BTN_X + (8 * 100), y=BTN_Y + Y_OFS * 2
    )
    tk.Button(root, text="SET", command=lambda: pairing_func(30)).place(
        x=BTN_X + (9 * 100), y=BTN_Y + Y_OFS * 2
    )

    main()
