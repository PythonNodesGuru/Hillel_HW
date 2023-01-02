from abc import ABC, abstractmethod


class IUkPlug(ABC):

    @staticmethod
    @abstractmethod
    def electricity_220v():
        """electricity supply, in VOLT"""


class UkPlug(IUkPlug):

    def electricity_220v(self):
        print("220 Volt")
