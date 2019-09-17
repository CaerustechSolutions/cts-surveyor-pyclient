from notifier import Notifier
from notification import Notification


def on_event_received (notification):

    if len(notification.events) > 0:
        if (notification.events[0].event_type == 'people_update'):
            i = 0
            while i < len(notification.events[0].people):
                print ('person coordinates: ' + str(notification.events[0].people[i].rectangle))
                i += 1
            i = 0
            while i < len(notification.events[0].faces):
                print ('************ face analyzed *************')
                print ('gender: ' + notification.events[0].faces[i].gender)
                print ('age lower: ' + str(notification.events[0].faces[i].ageLower))
                print ('age upper: ' + str(notification.events[0].faces[i].ageUpper))
                print ('****************************************')
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