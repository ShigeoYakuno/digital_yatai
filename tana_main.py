#!/usr/bin/python3
# -*- coding: utf8 -*-

# ======================================================================
#       ISHIDA GO TANAHAKARI SYSTEM Auther @yaku
#       2023.11.04 Ver1.1
#       https://github.com/ShigeoYakuno
# ======================================================================

import tkinter as tk
import tkinter.ttk as ttk
from public import *
import tkinter.font as f
import subprocess
from time import sleep
from tkinter.scrolledtext import ScrolledText
from datetime import datetime
import pandas as pd
import os
import csv
import sys
import threading

from CanDrv import CanDrv
from normal_tab import create_norm_tab
from test_tab import create_test_tab
from set_tab import create_set_tab
from connect_tab import create_conn_tab
from info_tab import create_info_tab

import serial

ch = 0
data_mode = 0
unitdata = 0.00


can = CanDrv()


# ======================================================================
#      tab change func
# ======================================================================
def tab_msg(event):
    global nb

    state = nb.tabs().index(nb.select())

    if state == DISP_MODE.NORMAL:
        print("NORMAL")
        os.system("cansend can0 3F3#4D53000000000000")  # 01111110011MS
    elif state == DISP_MODE.TEST:
        print("TEST")
        os.system("cansend can0 3F3#4D54000000000000")  # 01111110011MT
    elif state == DISP_MODE.SETTING:
        print("SETTING")
        os.system("cansend can0 3F3#4D54000000000000")  # 01111110011MT
    elif state == DISP_MODE.CONNECT:
        os.system("cansend can0 3F3#4D53000000000000")  # 01111110011MS
        print("CONNECT")
    elif state == DISP_MODE.INFO:
        print("INFO")
    elif state == DISP_MODE.PAIRING:
        print("PAIRING")
    elif state == DISP_MODE.DOWNLOAD:
        print("DOWNLOAD")
    else:
        print("MODE UNKNOWN")


# ======================================================================
#      make class
# ======================================================================
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        return

    def create_widgets(self):
        global nb

        nb = ttk.Notebook(
            self,
            height=DISP_Y,
            width=DISP_X,
        )

        tab1 = tk.Frame(nb)
        tab2 = tk.Frame(nb)
        tab3 = tk.Frame(nb)
        tab4 = tk.Frame(nb)
        tab5 = tk.Frame(nb)

        nb.add(tab1, text="NORMAL", padding=3)
        nb.add(tab2, text="TEST", padding=3)
        nb.add(tab3, text="SETTING", padding=3)
        nb.add(tab4, text="CONNECT", padding=3)
        nb.add(tab5, text="INFO", padding=3)
        nb.pack(expand=2, fill="both")

        create_norm_tab(self, tab1)
        create_test_tab(self, tab2)
        create_set_tab(self, tab3)
        create_conn_tab(self, tab4)
        create_info_tab(self, tab5)

        nb.bind("<<NotebookTabChanged>>", tab_msg)  # call back


# ======================================================================
#      bottun func
# ======================================================================
def exit_exec():
    canclose()
    sleep(1)
    sys.exit()


def PON_func(ch):
    id = ch << 4
    print(format(id, "03X"))
    os.system("cansend can0 " + str(format(id, "03X")) + "#4142434445464748")


# ======================================================================
#      can rx thread
# ======================================================================


def can_rx():
    global id
    global ch
    global data_mode
    global textComm
    global unitdata

    while True:
        msg = can.receive()

        if msg is not None:
            textComm.delete(1.0, tk.END)
            textComm.insert("end", msg)

            sour = (msg.arbitration_id & 0x0400) >> 10
            ch = (msg.arbitration_id & 0x03F0) >> 4
            cmd = msg.arbitration_id & 0x000F
            print(f"self {sour} ch {ch}  cmd {cmd}")

            if cmd == 0 and sour == 1:
                if msg.data[0] == 0x30:
                    PON_func(ch)

            if cmd == 1 and sour == 1:
                if msg.data[0] & 0x40:
                    pola_data = "T"
                    data_mode = 1
                elif msg.data[0] & 0x04:
                    pola_data = "-"
                    data_mode = 0
                else:
                    pola_data = "+"
                    data_mode = 0

                digit_7 = msg.data[1] - 0x30
                digit_6 = msg.data[2] - 0x30
                digit_5 = msg.data[3] - 0x30
                digit_4 = msg.data[4] - 0x30
                digit_3 = msg.data[5] - 0x30
                digit_2 = msg.data[6] - 0x30
                digit_1 = msg.data[7] - 0x30

                wgtdata = (
                    digit_7 * 1000000
                    + digit_6 * 100000
                    + digit_5 * 10000
                    + digit_4 * 1000
                    + digit_3 * 100
                    + digit_2 * 10
                    + digit_1
                )

                # unit data
                if msg.data[0] == 117:
                    unitdata = float(wgtdata / 100)
                    UnitBox[ch - 1].delete(0, tk.END)
                    UnitBox[ch - 1].insert("end", unitdata)
                    unit_flg[ch - 1] = 1
                else:
                    ADBox[ch - 1].delete(0, tk.END)
                    ADBox[ch - 1].insert("end", pola_data)
                    ADBox[ch - 1].insert("end", wgtdata)

                    # numdata
                    if (unit_flg[ch - 1] == 1) and data_mode == 0:
                        unit_num = int((wgtdata + (unitdata / 2)) / unitdata)
                        print(f"wgt {wgtdata} unit {unitdata} num {unit_num}")
                        NumBox[ch - 1].delete(0, tk.END)
                        NumBox[ch - 1].insert("end", unit_num)

                if data_mode == 0:
                    DATE = datetime.now().strftime("%Y%m%d")
                    FILE_NAME = "/home/ishida/digi_yata/log/yatai_" + DATE + ".csv"
                    timestmp = datetime.now().strftime("%H:%M:%S")

                    with open(FILE_NAME, "a", newline="") as f:
                        writer = csv.writer(f)
                        header = [timestmp, ch, wgtdata]
                        writer.writerow(header)

                # serial send
                ser = serial.Serial("/dev/serial0", 9600)
                ch_str = str(ch)
                wgt_str = str(wgtdata)
                strData = "s" + ch_str.zfill(2) + pola_data + wgt_str.zfill(7) + "e"
                ser.write(strData.encode())
                # ser.write(wgtdata)      #
                # ser.close()             #


# ======================================================================
#      can socket api function
# ======================================================================
def canopen():
    can.open()

    return


def canclose():
    global id
    root.after_cancel(id)
    can.close()
    return


# ======================================================================
#      main thread
# ======================================================================
# main
def main():
    global app
    global root
    global textComm

    root = tk.Tk()
    root.geometry("1280x800")
    root.title("ISHIDA GO DIGITAL YATAI Ver1.0")

    app = Application(master=root)

    ADFont = f.Font(family="Lucida Console", weight="bold", size=16, slant="italic")
    UnitFont = f.Font(family="Lucida Console", weight="bold", size=10, slant="italic")
    NumFont = f.Font(family="Lucida Console", weight="bold", size=16, slant="italic")

    # UTF-8 or cp932
    df = pd.read_csv("/home/ishida/digi_yata/master.csv", encoding="cp932", header=0)
    df.head()

    for num in range(0, GOUKI_MAX):
        q, r = num // 6, num % 6

        txt_item[num] = str(df.iloc[num, 0]) + " " + str(df.iloc[num, 1])
        lbl_item[num] = tk.Label(text=txt_item[num], font=UnitFont).place(
            x=r * AXIS_X + TXT_X, y=q * AXIS_Y + TXT_Y
        )

        ADBox[num] = tk.Entry(root, width=SIZE_AD, font=ADFont)
        ADBox[num].place(x=r * AXIS_X + AD_X, y=q * AXIS_Y + AD_Y)
        ADBox[num].insert(0, "------")
        UnitBox[num] = tk.Entry(root, width=SIZE_UNIT, font=UnitFont)
        UnitBox[num].place(x=r * AXIS_X + UNIT_X, y=q * AXIS_Y + UNIT_Y)
        UnitBox[num].insert(0, "-----")
        NumBox[num] = tk.Entry(root, width=SIZE_NUM, font=NumFont)
        NumBox[num].place(x=r * AXIS_X + NUM_X, y=q * AXIS_Y + NUM_Y)
        NumBox[num].insert(0, "---")

    exibtn = tk.Button(root, text="EXIT", command=exit_exec)
    exibtn.place(x=EXIT_X, y=EXIT_Y)

    textComm = ScrolledText(root, height=2, width=SCL_WTH)
    textComm.place(x=SCL_X, y=SCL_Y)

    canopen()
    sleep(0.5)

    can_rx_tsk = threading.Thread(target=can_rx, daemon=True)
    can_rx_tsk.start()

    app.mainloop()
    pass


if __name__ == "__main__":
    main()
