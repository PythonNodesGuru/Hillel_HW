from adaptee import IUkPlug
from client import UsSocket


class UktoUsAdapter(IUkPlug):

    def __init__(self):
        self.us_socket = UsSocket()

    def electricity_220v(self):
        self.us_socket.electricity_110v()
