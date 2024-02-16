# ======================================================================
#       ISHIDA GO TANAHAKARI SYSTEM Test Mode Tab
# ======================================================================
import tkinter as tk
from public import *
import tkinter.font as f
import os
import time


# ======================================================================
#      button func
# ======================================================================
def cmd_z_exec(num):
    id = (num << 4) | BIT_ADJUST
    os.system("cansend can0 " + str(format(id, "03X")) + "#5A30303030303030")
    print(f"push z {num}")


def cmd_t_exec(num):
    id = (num << 4) | BIT_ADJUST
    os.system("cansend can0 " + str(format(id, "03X")) + "#5430303030303030")
    print(f"push t {num}")


def cmd_w_exec(num):
    id = (num << 4) | BIT_ADJUST

    # set the mode to normal
    os.system(
        "cansend can0 " + str(format(id, "03X")) + "#4D53000000000000"
    )  # 01111110011MS

    time.sleep(0.5)

    # command for save to flash
    os.system("cansend can0 " + str(format(id, "03X")) + "#5730303030303030")
    print(f"push w {num}")

    time.sleep(0.5)

    # set the mode to test
    os.system("cansend can0 " + str(format(id, "03X")) + "#4D54000000000000")


# ======================================================================
#      create button
# ======================================================================
def create_test_tab(self, tab):
    LabelFont = f.Font(family="Lucida Console", weight="bold", size=11)

    for num in range(0, GOUKI_MAX):
        q, r = num // 6, num % 6

        tk.Label(
            tab, relief=tk.SOLID, width=25, height=7, anchor="nw", font=LabelFont
        ).place(x=r * AXIS_X, y=q * AXIS_Y)

        if r == 0:
            if q == 0:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(1)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(1)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(1)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 1:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(7)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(7)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(7)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 2:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(13)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(13)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(13)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 3:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(19)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(19)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(19)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 4:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(25)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(25)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(25)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )

        elif r == 1:
            if q == 0:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(2)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(2)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(2)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 1:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(8)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(8)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(8)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 2:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(14)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(14)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(14)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 3:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(20)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(20)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(20)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 4:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(26)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(26)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(26)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )

        elif r == 2:
            if q == 0:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(3)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(3)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(3)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 1:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(9)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(9)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(9)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 2:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(15)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(15)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(15)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 3:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(21)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(21)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(21)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 4:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(27)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(27)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(27)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )

        elif r == 3:
            if q == 0:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(4)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(4)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(4)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 1:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(10)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(10)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(10)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 2:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(16)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(16)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(16)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 3:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(22)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(22)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(22)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 4:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(28)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(28)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(28)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )

        elif r == 4:
            if q == 0:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(5)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(5)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(5)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 1:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(11)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(11)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(11)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 2:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(17)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(17)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(17)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 3:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(23)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(23)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(23)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 4:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(29)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(29)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(29)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )

        elif r == 5:
            if q == 0:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(6)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(6)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(6)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 1:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(12)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(12)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(12)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 2:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(18)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(18)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(18)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 3:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(24)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(24)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(24)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 4:
                tk.Button(tab, text="zero", command=lambda: cmd_z_exec(30)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="span", command=lambda: cmd_t_exec(30)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="mem", command=lambda: cmd_w_exec(30)).place(
                    x=r * AXIS_X + BTN_OFS * 2, y=q * AXIS_Y + BTN_Y
                )

    return
