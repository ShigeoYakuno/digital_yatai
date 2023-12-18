# ======================================================================
#       ISHIDA GO TANAHAKARI SYSTEM Information Mode Tab
# ======================================================================

import tkinter as tk
from public import *
import tkinter.font as f
import os


# ======================================================================
#      Button func
# ======================================================================
def cmd_y_exec(num):
    id = (num << 4) | BIT_INFO
    os.system("cansend can0 " + str(format(id, "03X")) + "#5930303030303030")  # Y
    print(f"push c {num}")


def cmd_r_exec(num):
    id = (num << 4) | BIT_INFO
    os.system("cansend can0 " + str(format(id, "03X")) + "#5230303030303030")  # R
    print(f"push s {num}")


# ======================================================================
#      Create Button
# ======================================================================
def create_info_tab(app_conn, tab):
    LabelFont = f.Font(family="Lucida Console", weight="bold", size=11)

    for num in range(GOUKI_MAX):
        q, r = num // 6, num % 6

        tk.Label(
            tab, relief=tk.SOLID, width=25, height=7, anchor="nw", font=LabelFont
        ).place(x=r * AXIS_X, y=q * AXIS_Y)

        if r == 0:
            if q == 0:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(1)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(1)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 1:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(7)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(7)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 2:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(13)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(13)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 3:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(19)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(19)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 4:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(25)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(25)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )

        elif r == 1:
            if q == 0:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(2)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(2)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 1:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(8)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(8)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 2:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(14)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(14)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 3:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(20)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(20)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 4:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(26)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(26)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )

        elif r == 2:
            if q == 0:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(3)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(3)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 1:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(9)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(9)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 2:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(15)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(15)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 3:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(21)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(21)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 4:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(27)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(27)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )

        elif r == 3:
            if q == 0:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(4)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(4)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 1:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(10)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(10)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 2:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(16)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(16)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 3:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(22)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(22)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 4:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(28)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(28)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )

        elif r == 4:
            if q == 0:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(5)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(5)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 1:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(11)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(11)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 2:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(17)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(17)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 3:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(23)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(23)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 4:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(29)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(29)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )

        elif r == 5:
            if q == 0:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(6)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(6)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 1:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(12)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(12)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 2:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(18)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(18)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 3:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(24)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(24)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )
            elif q == 4:
                tk.Button(tab, text="setting", command=lambda: cmd_y_exec(30)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="version", command=lambda: cmd_r_exec(30)).place(
                    x=r * AXIS_X + BTN_OFS2, y=q * AXIS_Y + BTN_Y
                )

    return
