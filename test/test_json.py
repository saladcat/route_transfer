from source.Message import Message
import json

classes = {
    'Message': Message
}


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

if __name__ == '__main__':
    msg = Message(0, 1, "dsads")
    a = json.dumps(msg, default=serialize_instance)
    b = json.loads(a, object_hook=unserialize_object)
    print(b.content)
