import sys
sys.path.append('gen-py')

from gen_py.tutorial import Service
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class ServiceHandler:
    def __init__(self):
        self.log = {}

    def hello(self, name):
        return "hello, %s" % name

    def add(self, a, b):
        return a + b


if __name__ == '__main__':
    handler = ServiceHandler()
    processor = Service.Processor(handler)
    transport = TSocket.TServerSocket(host='127.0.0.1', port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print('Starting the server...')
    server.serve()
    print('done.')
