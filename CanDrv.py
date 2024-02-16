import os
import can


# ======================================================================
#      Cant Driver API
# ======================================================================
class CanDrv:

    """constructor"""

    def __init__(self):
        self.__state = False
        return

    """destructor"""

    def __del__(self):
        if self.__state is True:
            os.system("sudo ifconfig can0 down")

        return

    """open can port"""

    def open(self):
        self.__state = True
        os.system("sudo ip link set can0 type can bitrate 500000 loopback off")
        os.system("sudo ifconfig can0 up")

        self.__can0 = can.interface.Bus(channel="can0", bustype="socketcan")

        return

    """close can port"""

    def close(self):
        self.__state = False
        os.system("sudo ifconfig can0 down")
        return

    """send data"""

    def send(self, id, data, ext=False):
        if self.__state is True:
            msg = can.Message(id, data, ext)
            self.__can0.send(msg)

        return msg

    """receive data"""

    def receive(self):
        if self.__state is True:
            msg = self.__can0.recv(1.0)
        else:
            msg = None

        return msg
