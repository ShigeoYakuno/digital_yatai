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
from count_tab import create_count_tab

import serial

ch = 0
data_mode = 0
unitdata = 0.0
exit_flg = 0
selectMode = DISP_MODE.NORMAL

DATE = datetime.now().strftime("%Y%m%d")
FILE_NAME = "/home/ishida/digi_yata/log/yatai_" + DATE + ".csv"


can = CanDrv()


# ======================================================================
#      tab change func
# ======================================================================
def tab_msg(event):
    global nb
    global selectMode

    selectMode = nb.tabs().index(nb.select())

    print(f"mode change {selectMode}")

    if selectMode == DISP_MODE.NORMAL:
        os.system("cansend can0 3F3#4D53000000000000")  # 01111110011MS
    elif selectMode == DISP_MODE.TEST:
        os.system("cansend can0 3F3#4D54000000000000")  # 01111110011MT
    elif selectMode == DISP_MODE.SETTING:
        os.system("cansend can0 3F3#4D54000000000000")  # 01111110011MT
    elif selectMode == DISP_MODE.CONNECT:
        os.system("cansend can0 3F3#4D53000000000000")  # 01111110011MS
    elif selectMode == DISP_MODE.COUNT:
        os.system("cansend can0 3F3#4D43000000000000")  # 01111110011MC

    elif selectMode == DISP_MODE.INFO:
        pass
    elif selectMode == DISP_MODE.PAIRING:
        pass
    elif selectMode == DISP_MODE.DOWNLOAD:
        pass
    else:
        pass


# ======================================================================
#      make class
# ======================================================================
class Application(tk.Frame):
    # constructor
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
        tab6 = tk.Frame(nb)

        nb.add(tab1, text="NORMAL", padding=3)
        nb.add(tab2, text="TEST", padding=3)
        nb.add(tab3, text="SETTING", padding=3)
        nb.add(tab4, text="CONNECT", padding=3)
        nb.add(tab5, text="INFO", padding=3)
        nb.add(tab6, text="COUNT", padding=3)
        nb.pack(expand=2, fill="both")

        create_norm_tab(self, tab1)
        create_test_tab(self, tab2)
        create_set_tab(self, tab3)
        create_conn_tab(self, tab4)
        create_info_tab(self, tab5)
        create_count_tab(self, tab6)

        nb.bind("<<NotebookTabChanged>>", tab_msg)  # call back


# ======================================================================
#      bottun func
# ======================================================================
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
#      power on func
# ======================================================================
def PON_func(ch):
    id = ch << 4
    print(format(id, "03X"))
    os.system("cansend can0 " + str(format(id, "03X")) + "#4142434445464748")


# ======================================================================
#      ad data analysis
# ======================================================================
def wgtDataFunc(msg):
    global DATE
    global FILE_NAME
    global unitdata
    local_data = [0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30]
    err_flg = 0

    if msg.data[0] & 0x40:
        pola_data = "T"
        data_mode = 1
    elif msg.data[0] & 0x04:
        pola_data = "-"
        data_mode = 0
    else:
        pola_data = "+"
        data_mode = 0

    for i in range(1, 8):  # 23.12.12 index err supprt
        try:
            local_data[i] = msg.data[i] - 0x30
        except:
            print(f"index err {i}")
            err_flg = 1
            break

    wgtdata = (
        local_data[1] * 1000000
        + local_data[2] * 100000
        + local_data[3] * 10000
        + local_data[4] * 1000
        + local_data[5] * 100
        + local_data[6] * 10
        + local_data[7]
    )

    if err_flg == 1:
        data_mode = 1
    elif msg.data[0] == 117:  # unit data
        unitdata = float(wgtdata / UNIT_DATA)
        UnitBox[ch - 1].delete(0, tk.END)
        UnitBox[ch - 1].insert("end", unitdata)
        unit_flg[ch - 1] = 1
    else:
        ADBox[ch - 1].delete(0, tk.END)
        ADBox[ch - 1].insert("end", pola_data)

        if msg.data[0] & 0x10:
            wgtdatafloat = float(wgtdata / 10)
        ADBox[ch - 1].insert("end", wgtdatafloat)

    # numdata
    if (unit_flg[ch - 1] == 1) and data_mode == 0:
        unit_num = int((wgtdata + (unitdata / 2)) / unitdata)
        print(f"wgt {wgtdata} unit {unitdata} num {unit_num}")
        NumBox[ch - 1].delete(0, tk.END)
        NumBox[ch - 1].insert("end", unit_num)

    # log normal mode only
    if data_mode == 0:
        DATE = datetime.now().strftime("%Y%m%d")
        FILE_NAME = "/home/ishida/digi_yata/log/yatai_" + DATE + ".csv"
        timestmp = datetime.now().strftime("%H:%M:%S")

        with open(FILE_NAME, "a", newline="") as f:
            try:
                writer = csv.writer(f)
                header = [timestmp, ch, wgtdata]
                writer.writerow(header)
            except:
                print("Log Write err")

        # serial send normal mode only
        ser = serial.Serial("/dev/serial0", 9600)
        ch_str = str(ch)
        wgt_str = str(wgtdata)
        strData = "s" + ch_str.zfill(2) + pola_data + wgt_str.zfill(7) + "e"
        ser.write(strData.encode())
        # ser.write(wgtdata)      #
        # ser.close()             #


# ======================================================================
#      information analysis
# ======================================================================
def infoFunc(msg, ch):
    # adjust value information
    if chr(msg.data[0]) == "Y":
        # print(
        #    f"{msg.data[1]} | {msg.data[2]} | {msg.data[3]} | {msg.data[4]} | {msg.data[5]} | {msg.data[6]} | {msg.data[7]} "
        # )
        local_txt = f"{msg.data[1]}|{msg.data[2]}|{msg.data[3]}|{msg.data[4]}|{msg.data[5]}|{msg.data[6]}|{msg.data[7]} "
        info_adj[ch - 1]["text"] = local_txt

    # soft version information
    else:
        softVer = (
            chr(msg.data[0])
            + chr(msg.data[1])
            + chr(msg.data[2])
            + chr(msg.data[3])
            + chr(msg.data[4])
            + chr(msg.data[5])
            + chr(msg.data[6])
            + chr(msg.data[7])
        )
        # print(softVer)
        info_soft[ch - 1]["text"] = softVer


# ======================================================================
#      can rx thread
# ======================================================================
def can_rx():
    global id
    global ch
    global data_mode
    global textComm
    global unitdata
    global exit_flg

    while True:
        msg = can.receive()

        if exit_flg == 1:
            canclose()
            return

        if msg is not None:
            textComm.delete(1.0, tk.END)
            textComm.insert("end", msg)

            sour = (msg.arbitration_id & 0x0400) >> 10
            ch = (msg.arbitration_id & 0x03F0) >> 4
            cmd = msg.arbitration_id & 0x000F
            # print(f"self {sour} ch {ch}  cmd {cmd}")

            # echo back
            if sour == SOUR_SELF:
                pass

            # PON
            elif cmd == BIT_PON and sour == SOUR_SCALE:
                PON_func(ch)

            # DATA
            elif cmd == BIT_DATA and sour == SOUR_SCALE:
                wgtDataFunc(msg)

            # VERSION
            elif cmd == BIT_INFO and sour == SOUR_SCALE:
                infoFunc(msg, ch)


# ======================================================================
#      can socket api function
# ======================================================================
def canopen():
    can.open()

    return


def canclose():
    global id
    root.after_cancel(id)
    sleep(1)
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
    root.title("ISHIDA GO DIGITAL YATAI Ver3.0")

    app = Application(master=root)

    ADFont = f.Font(family="Lucida Console", weight="bold", size=16, slant="italic")
    UnitFont = f.Font(family="Lucida Console", weight="bold", size=10, slant="italic")
    InfoFont = f.Font(family="Lucida Console", weight="bold", size=8, slant="italic")
    NumFont = f.Font(family="Lucida Console", weight="bold", size=16, slant="italic")

    # UTF-8 or cp932
    df = pd.read_csv("/home/ishida/digi_yata/master.csv", encoding="cp932", header=0)
    df.head()

    for num in range(0, GOUKI_MAX):
        q, r = num // 6, num % 6

        txt_item[num] = str(df.iloc[num, 0]) + " " + str(df.iloc[num, 1])

        lbl_item[num] = tk.Label(text=txt_item[num], font=UnitFont)
        lbl_item[num].place(x=r * AXIS_X + TXT_X, y=q * AXIS_Y + TXT_Y)

        info_soft[num] = tk.Label(text="soft_ver", font=InfoFont)
        info_soft[num].place(x=r * AXIS_X + TXT_X, y=q * AXIS_Y + TXT_Y2)

        info_adj[num] = tk.Label(text="FFFFFFFFFFFFFF", font=InfoFont)
        info_adj[num].place(x=r * AXIS_X + TXT_X2, y=q * AXIS_Y + TXT_Y2)

        ADBox[num] = tk.Entry(root, width=SIZE_AD, font=ADFont)
        ADBox[num].place(x=r * AXIS_X + AD_X, y=q * AXIS_Y + AD_Y)
        ADBox[num].insert(0, "------")
        UnitBox[num] = tk.Entry(root, width=SIZE_UNIT, font=UnitFont)
        UnitBox[num].place(x=r * AXIS_X + UNIT_X, y=q * AXIS_Y + UNIT_Y)
        UnitBox[num].insert(0, "-----")
        NumBox[num] = tk.Entry(root, width=SIZE_NUM, font=NumFont)
        NumBox[num].place(x=r * AXIS_X + NUM_X, y=q * AXIS_Y + NUM_Y)
        NumBox[num].insert(0, "---")

    exibtn = tk.Button(root, text="EXIT", command=exit_exec2)
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
