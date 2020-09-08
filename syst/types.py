class Packet:
    def __init__(self, conn, header, data):
        self.conn = conn
        self.header = header
        self.data = data
