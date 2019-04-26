import threading
from websocket import create_connection
from time import sleep
from notification import Notification

class Notifier:
    
    stopped = True
    listener_thread = None
    
    
    def __init__(self, on_event_received):
    
        self.event_handler = on_event_received
        
    
    def start_event_listener(self):
    
        self.stopped = False
        self.listener_thread = threading.Thread(target=self.event_listener_thread, args=())
        self.listener_thread.start()
            
            
    def stop_event_listener(self):
        
        self.stopped = True
        
        
    def event_listener_thread(self):
    
        ws = create_connection("ws://localhost:6789/websocket")
        while (self.stopped == False):
            result =  ws.recv()
            notification = Notification(result)
            self.event_handler(notification)        
 
