from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Message(QObject):

    def __init__(self, src, dest, content):
        super().__init__()
        self.src = src
        self.dest = dest
        self.content = content

