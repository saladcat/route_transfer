from source.PC import PC
from source.Message import Message

if __name__ == '__main__':
    li = [PC(1), PC(2), PC(3)]
    li[0].route.regis_route((li[1].route, li[2].route))
    a = li[0]
    msg = Message(1, 2, 321)
    a.host.send_msg(msg)
