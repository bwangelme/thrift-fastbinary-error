from gen_py.tutorial import Service

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def main():
    # Make socket
    transport = TSocket.TSocket('localhost', 9090)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # TBinaryProtocolAccelerated 表示 binary 协议使用 fastbinary 进行序列化
    protocol = TBinaryProtocol.TBinaryProtocolAccelerated(transport)
    # protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = Service.Client(protocol)

    # Connect!
    transport.open()

    print(client.hello("bwangel"))
    print(client.add(40, 2))


if __name__ == '__main__':
    main()
