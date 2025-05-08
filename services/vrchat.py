from pythonosc import udp_client
import time

class VRChatService:
    def __init__(self):
        # Default VRChat OSC settings
        self.client = udp_client.SimpleUDPClient("127.0.0.1", 9000)
        self.chatbox_address = "/chatbox/input"

    def send_to_chatbox(self, text: str):
        try:
            # Send the message to VRChat's chatbox
            self.client.send_message(self.chatbox_address, [text, True])
            time.sleep(0.1)  # Small delay to ensure message is sent
        except Exception as e:
            print(f"Error sending to VRChat: {str(e)}")

    def set_osc_settings(self, ip: str = "127.0.0.1", port: int = 9000):
        """Update OSC connection settings"""
        self.client = udp_client.SimpleUDPClient(ip, port) 