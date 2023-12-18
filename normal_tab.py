# ======================================================================
#       ISHIDA GO TANAHAKARI SYSTEM Normal Mode Tab
# ======================================================================

import tkinter as tk
from public import *
import tkinter.font as f
import os


# ======================================================================
#      button func
# ======================================================================
def cmd_k_exec(num):
    id = (num << 4) | BIT_ADJUST
    os.system("cansend can0 " + str(format(id, "03X")) + "#4B30303030303030")
    print(f"push k {num}")


def cmd_u_exec(num):
    id = (num << 4) | BIT_ADJUST
    os.system("cansend can0 " + str(format(id, "03X")) + "#5530303030303030")
    print(f"push u {num}")


# ======================================================================
#      create button
# ======================================================================
def create_norm_tab(app_norm, tab):
    LabelFont = f.Font(family="Lucida Console", weight="bold", size=11)

    for num in range(GOUKI_MAX):
        q, r = num // 6, num % 6

        tk.Label(
            tab, relief=tk.SOLID, width=25, height=7, anchor="nw", font=LabelFont
        ).place(x=r * AXIS_X, y=q * AXIS_Y)

        if r == 0:
            if q == 0:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(1)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_u_exec(1)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
            elif q == 1:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(7)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_u_exec(7)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
            elif q == 2:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(13)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_u_exec(13)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
            elif q == 3:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(19)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_u_exec(19)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
            elif q == 4:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(25)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_u_exec(25)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )

        elif r == 1:
            if q == 0:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(2)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_u_exec(2)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
            elif q == 1:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(8)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_u_exec(8)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
            elif q == 2:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(14)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_u_exec(14)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
            elif q == 3:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(20)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_u_exec(20)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
            elif q == 4:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(26)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_u_exec(26)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )

        elif r == 2:
            if q == 0:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(3)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_u_exec(3)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
            elif q == 1:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(9)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_u_exec(9)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
            elif q == 2:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(15)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_u_exec(15)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
            elif q == 3:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(21)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_u_exec(21)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
            elif q == 4:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(27)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_u_exec(27)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )

        elif r == 3:
            if q == 0:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(4)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_u_exec(4)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
            elif q == 1:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(10)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_k_exec(10)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
            elif q == 2:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(16)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_u_exec(16)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
            elif q == 3:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(22)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_u_exec(22)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
            elif q == 4:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(28)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_u_exec(28)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )

        elif r == 4:
            if q == 0:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(5)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_u_exec(5)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
            elif q == 1:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(11)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_u_exec(11)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
            elif q == 2:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(17)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_u_exec(17)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
            elif q == 3:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(23)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_u_exec(23)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
            elif q == 4:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(29)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_u_exec(29)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )

        elif r == 5:
            if q == 0:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(6)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_u_exec(6)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
            elif q == 1:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(12)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_u_exec(12)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
            elif q == 2:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(18)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_u_exec(18)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
            elif q == 3:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(24)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_u_exec(24)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )
            elif q == 4:
                tk.Button(tab, text="tare", command=lambda: cmd_k_exec(30)).place(
                    x=r * AXIS_X + X_OFS, y=q * AXIS_Y + BTN_Y
                )
                tk.Button(tab, text="unit", command=lambda: cmd_u_exec(30)).place(
                    x=r * AXIS_X + BTN_OFS, y=q * AXIS_Y + BTN_Y
                )

    return
