from pyadb.command.host import Host
from pyadb.connection import Connection
from pyadb.utils.logger import AdbLogging

logger = AdbLogging.get_logger(__name__)

class Client(Host):
    def __init__(self, host='127.0.0.1', port=5037):
        self.host = host
        self.port = port

    def create_connection(self, timeout=None):
        conn = Connection(self.host, self.port, timeout)
        conn.connect()
        return conn

    def device(self, serial):
        devices = self.devices()

        for device in devices:
            if device.serial == serial:
                return device

        return None
