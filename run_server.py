#import p4p
from pcaspy import Driver, SimpleServer

pvdb = {
    "pv1": {
        "prec": 3,
        "value": 1.0
    },
}


class myDriver(Driver):
    def  __init__(self):
        super(myDriver, self).__init__()

if __name__ == "__main__":
    server = SimpleServer()
    server.createPV("test:", pvdb)
    driver = myDriver()
    while True:
        server.process(0.1)