# Target interface

from abc import ABC, abstractmethod


class IUsSocket(ABC):

    @staticmethod
    @abstractmethod
    def electricity_110v():
        """electricity supply"""
