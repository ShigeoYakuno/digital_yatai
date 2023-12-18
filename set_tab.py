# ======================================================================
#       ISHIDA GO TANAHAKARI SYSTEM Setting Mode Tab
# ======================================================================

import tkinter as tk
from public import *
import tkinter.font as f
import os

setlist = ["1g/6kg", "2g/15kg", "10g/30kg", "50g/150kg", "precision"]


# ======================================================================
#      button func
# ======================================================================
def cmd_I_exec(num):
    get_val = SpanSet[num].get()

    print(f"push i {num} {get_val}")
    id = (num << 4) | BIT_SET
    if get_val == 1:  # 1g/6kg 1e=10cnt
        # mode1~4 stable num 10 stable with 2 unst with 4 rest with 20
        os.system("cansend can0 " + str(format(id, "03X")) + "#310A020414304130")
    elif get_val == 2:  # 2g/15kg 1e=10cnt
        os.system("cansend can0 " + str(format(id, "03X")) + "#320A020414304130")
    elif get_val == 3:  # 10g/30kg 1e=10cnt
        os.system("cansend can0 " + str(format(id, "03X")) + "#330A020414304130")
    elif get_val == 4:  # 50g/150kg 1e=10cnt
        os.system("cansend can0 " + str(format(id, "03X")) + "#340A020414304130")
    elif get_val == 5:  # 1g/6kg 1e=100cnt
        # mode5 stable num 10 stable with 15 unst with 40 rest with 200
        os.system("cansend can0 " + str(format(id, "03X")) + "#350A0F28C8304130")


# ======================================================================
#      create button
# ======================================================================
def create_set_tab(app, tab):
    LabelFont = f.Font(family="Lucida Console", weight="bold", size=11)

    for num in range(GOUKI_MAX):
        q, r = num // 6, num % 6

        tk.Label(
            tab, relief=tk.SOLID, width=25, height=7, anchor="nw", font=LabelFont
        ).place(x=r * AXIS_X, y=q * AXIS_Y)

        if r == 0:
            if q == 0:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(1)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[1] = tk.IntVar()
                SpanSet[1].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[1]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[1]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[1]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[1]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

            elif q == 1:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(7)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[7] = tk.IntVar()
                SpanSet[7].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[7]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[7]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[7]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[7]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

            elif q == 2:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(13)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[13] = tk.IntVar()
                SpanSet[13].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[13]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[13]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[13]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[13]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

            elif q == 3:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(19)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[19] = tk.IntVar()
                SpanSet[19].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[19]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[19]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[19]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[19]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

            elif q == 4:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(25)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[25] = tk.IntVar()
                SpanSet[25].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[25]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[25]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[25]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[25]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

        elif r == 1:
            if q == 0:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(2)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[2] = tk.IntVar()
                SpanSet[2].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[2]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[2]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[2]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[2]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

            elif q == 1:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(8)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[8] = tk.IntVar()
                SpanSet[8].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[8]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[8]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[8]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[8]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

            elif q == 2:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(14)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[14] = tk.IntVar()
                SpanSet[14].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[14]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[14]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[14]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[14]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

            elif q == 3:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(20)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[20] = tk.IntVar()
                SpanSet[20].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[20]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[20]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[20]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[20]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

            elif q == 4:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(26)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[26] = tk.IntVar()
                SpanSet[26].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[26]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[26]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[26]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[26]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

        elif r == 2:
            if q == 0:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(3)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[3] = tk.IntVar()
                SpanSet[3].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[3]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[3]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[3]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[3]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

            elif q == 1:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(9)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[9] = tk.IntVar()
                SpanSet[9].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[9]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[9]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[9]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[9]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

            elif q == 2:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(15)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[15] = tk.IntVar()
                SpanSet[15].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[15]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[15]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[15]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[15]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

            elif q == 3:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(21)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[21] = tk.IntVar()
                SpanSet[21].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[21]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[21]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[21]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[21]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

            elif q == 4:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(27)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[27] = tk.IntVar()
                SpanSet[27].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[27]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[27]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[27]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[27]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

        elif r == 3:
            if q == 0:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(4)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[4] = tk.IntVar()
                SpanSet[4].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[4]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[4]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[4]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[4]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

            elif q == 1:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(10)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[10] = tk.IntVar()
                SpanSet[10].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[10]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[10]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[10]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[10]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

            elif q == 2:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(16)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[16] = tk.IntVar()
                SpanSet[16].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[16]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[16]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[16]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[16]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

            elif q == 3:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(22)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[22] = tk.IntVar()
                SpanSet[22].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[22]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[22]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[22]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[22]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

            elif q == 4:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(28)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[28] = tk.IntVar()
                SpanSet[28].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[28]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[28]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[28]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[28]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

        elif r == 4:
            if q == 0:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(5)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[5] = tk.IntVar()
                SpanSet[5].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[5]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[5]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[5]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[5]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

            elif q == 1:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(11)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[11] = tk.IntVar()
                SpanSet[11].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[11]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[11]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[11]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[11]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

            elif q == 2:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(17)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[17] = tk.IntVar()
                SpanSet[17].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[17]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[17]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[17]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[17]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

            elif q == 3:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(23)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[23] = tk.IntVar()
                SpanSet[23].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[23]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[23]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[23]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[23]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

            elif q == 4:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(29)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[29] = tk.IntVar()
                SpanSet[29].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[29]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[29]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[29]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[29]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

        elif r == 5:
            if q == 0:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(6)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[6] = tk.IntVar()
                SpanSet[6].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[6]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[6]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[6]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[6]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

            elif q == 1:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(12)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[12] = tk.IntVar()
                SpanSet[12].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[12]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[12]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[12]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[12]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

            elif q == 2:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(18)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[18] = tk.IntVar()
                SpanSet[18].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[18]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[18]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[18]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[18]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

            elif q == 3:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(24)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[24] = tk.IntVar()
                SpanSet[24].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[24]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[24]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[24]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[24]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

            elif q == 4:
                tk.Button(tab, text="ini", command=lambda: cmd_I_exec(30)).place(
                    x=r * AXIS_X + X_OFS2, y=q * AXIS_Y + BTN_Y
                )

                SpanSet[30] = tk.IntVar()
                SpanSet[30].set(1)
                tk.Radiobutton(
                    tab, text=setlist[0], value=1, variable=SpanSet[30]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[1], value=2, variable=SpanSet[30]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y)
                tk.Radiobutton(
                    tab, text=setlist[2], value=3, variable=SpanSet[30]
                ).place(x=r * AXIS_X + RD_OFS, y=q * AXIS_Y + RD_Y2)
                tk.Radiobutton(
                    tab, text=setlist[4], value=5, variable=SpanSet[30]
                ).place(x=r * AXIS_X + RD_OFS2, y=q * AXIS_Y + RD_Y2)

    return
