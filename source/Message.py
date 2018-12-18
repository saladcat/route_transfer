from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Message(QObject):

    def __init__(self, src, dest, content):
        super().__init__()
        self.src = src
        self.dest = dest
        self.content = content

    def serialize_instance(obj):
        d = {'__classname__': type(obj).__name__}
        d.update(vars(obj))
        return d

    def unserialize_object(d):
        clsname = d.pop('__classname__', None)
        if clsname:
            cls = classes[clsname]
            obj = cls.__new__(cls)  # Make instance without calling __init__
            for key, value in d.items():
                setattr(obj, key, value)
            return obj
        else:
            return d


classes = {
    'Message': Message
}
