from notifier import Notifier
from notification import Notification


def on_event_received (notification):
    
    print ('received: ' + str(len(notification.events)) + ' events')
    if len(notification.events) > 0:
        print ('event: ' + notification.events[0].event_type)
        if (notification.events[0].event_type == 'people_update'):
            i = 0
            while i < len(notification.events[0].people):
                print ('id: ' + str(notification.events[0].people[i].id))
                print ('gender: ' + notification.events[0].people[i].gender)
                print ('age: ' + notification.events[0].people[i].age)
                print ('rectangle: ' + str(notification.events[0].people[i].rectangle))
                i += 1
    
    
def start_notifier(notifier):

    notifier.start_event_listener()
    print (notifier)
    print ('started')
    
    
def stop_notifier(notifier):

    notifier.stop_event_listener()
    print ('stopped')
    

notifier = Notifier(on_event_received)    
start_notifier(notifier)
print ('press any key to finish')
input()
stop_notifier(notifier)