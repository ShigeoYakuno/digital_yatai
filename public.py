# ======================================================================
#       ISHIDA GO TANAHAKARI SYSTEM common
# ======================================================================

from enum import IntEnum, auto


class DISP_MODE(IntEnum):
    NORMAL = 0
    TEST = auto()
    SETTING = auto()
    CONNECT = auto()
    INFO = auto()
    COUNT = auto()
    NB_MAX = auto()
    # Add NB page above here
    PAIRING = auto()
    DOWNLOAD = auto()


AXIS_X = 210
AXIS_Y = 120

BTN_X = 180
BTN_Y = 75
BTN_Y2 = 20

GOUKI_ROW = 5
GOUKI_COLUMU = 6
GOUKI_MAX = GOUKI_ROW * GOUKI_COLUMU

ADBox = [0] * GOUKI_MAX
UnitBox = [0] * GOUKI_MAX
NumBox = [0] * GOUKI_MAX
txt_item = [0] * GOUKI_MAX
lbl_item = [0] * GOUKI_MAX
info_soft = [0] * GOUKI_MAX
info_adj = [0] * GOUKI_MAX
ch_obj = [0] * GOUKI_MAX
unit_flg = [0] * GOUKI_MAX


SpanSet = [0] * (GOUKI_MAX + 1)

SIZE_AD = 8
SIZE_UNIT = 6
SIZE_NUM = 4

AD_X = 20
AD_Y = 70
UNIT_X = 140
UNIT_Y = 30
NUM_X = 140
NUM_Y = 70

TXT_X = 7
TXT_X2 = 80
TXT_X3 = 120

TXT_Y = 30
TXT_Y2 = 50

BTN_OFS = 70
BTN_OFS2 = 100
BTN_OFS3 = 55
RD_OFS = 40
RD_OFS2 = 105
RD_Y = 70
RD_Y2 = 90
X_OFS = 10
X_OFS2 = 5

DISP_X = 1280
DISP_Y = 800

EXIT_X = 1150
EXIT_Y = 650

DOWN_X = 1200
DOWN_Y = 650

FILE_X = 1000
FILE_Y = 650

PROG_BAR = 1000

SCL_X = 5
SCL_Y = 630
SCL_WTH = 140

SOUR_SCALE = 1
SOUR_SELF = 0

BIT_PON = 0x00
BIT_DATA = 0x01
BIT_SET = 0x02
BIT_ADJUST = 0x03
BIT_INFO = 0x04

BIT_PAIR_STA = 0x07
BIT_PAIR_END = 0x08

UNIT_DATA = 10
