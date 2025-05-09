from pythonosc import udp_client
from utils.logger import Logger

class OSCClient:
    def __init__(self, ip="127.0.0.1", port=9000):
        self.logger = Logger()
        self.logger.info('Initializing OSC client')
        try:
            self.client = udp_client.SimpleUDPClient(ip, port)
            self.logger.debug(f'OSC client initialized successfully at {ip}:{port}')
        except Exception as e:
            self.logger.error(f'Failed to initialize OSC client: {str(e)}')
            raise

    def send_message(self, message):
        try:
            self.logger.info('Sending message to VRChat')
            self.client.send_message("/chatbox/input", [message, True])
            self.logger.debug('Message sent successfully')
        except Exception as e:
            self.logger.error(f'Failed to send message to VRChat: {str(e)}')
            raise 