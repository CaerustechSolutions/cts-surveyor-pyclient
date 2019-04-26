from client import Client
import datetime

def print_menu():

    print ('select between the following options')
    print ('1 - enable face detection')
    print ('2 - disable face detection')
    print ('3 - enable people detection')
    print ('4 - disable people detection')
    print ('5 - get status')
    print ('6 - get stats')
    print ('7 - get hourly stats')
    print ('8 - get total stats')
    print ('0 - exit')
    
    
client = Client()
option = ''
while option != '0':
    print_menu()
    option = input()
    if option == '1':
        client.enable_face_detection()
    elif option == '2':
        client.disable_face_detection()
    elif option == '3':
        client.enable_people_detection()
    elif option == '4':
        client.disable_people_detection()
    elif option == '5':
        print ('status: ' + client.get_status())
    elif option == '6':
        d = datetime.datetime.today()
        start_time = str(d.year) + str(d.month).zfill(2) + str(d.day).zfill(2) + 'T000000'
        end_time = str(d.year) + str(d.month).zfill(2) + str(d.day).zfill(2) + 'T235959'
        stats_response = client.get_statistics(start_time, end_time)
        i = 0
        while i < len(stats_response.entries):
            print ('id: ' + str(stats_response.entries[i].id))
            print ('gender: ' + stats_response.entries[i].gender)
            print ('lower age limit: ' + str(stats_response.entries[i].age_lower))
            print ('upper age limit: ' + str(stats_response.entries[i].age_upper))
            print ('detected time: ' + stats_response.entries[i].arrived)
            i += 1
    elif option == '7':
        d = datetime.datetime.today()
        start_time = str(d.year) + str(d.month).zfill(2) + str(d.day).zfill(2) + 'T000000'
        end_time = str(d.year) + str(d.month).zfill(2) + str(d.day).zfill(2) + 'T235959'
        stats_response = client.get_hourly_statistics(start_time, end_time)
        i = 0
        while i < len(stats_response.entries):
            print ('start: ' + str(stats_response.entries[i].start))
            print ('end: ' + str(stats_response.entries[i].end))
            print ('male count: ' + str(stats_response.entries[i].male_count))
            print ('female count: ' + str(stats_response.entries[i].female_count))
            print ('child count: ' + str(stats_response.entries[i].child_count))
            print ('teen count: ' + str(stats_response.entries[i].teen_count))
            print ('young adult count: ' + str(stats_response.entries[i].young_adult_count))
            print ('adult count: ' + str(stats_response.entries[i].adult_count))
            print ('middle aged count: ' + str(stats_response.entries[i].middle_aged_count))
            print ('senior count: ' + str(stats_response.entries[i].senior_count))
            print ('unidentifed count: ' + str(stats_response.entries[i].unidentified_count))
            i += 1            
    elif option == '8':
        d = datetime.datetime.today()
        start_time = str(d.year) + str(d.month).zfill(2) + str(d.day).zfill(2) + 'T000000'
        end_time = str(d.year) + str(d.month).zfill(2) + str(d.day).zfill(2) + 'T235959'
        stats_response = client.get_total_statistics(start_time, end_time)
        print ('start: ' + str(stats_response.entry.start))
        print ('end: ' + str(stats_response.entry.end))
        print ('male count: ' + str(stats_response.entry.male_count))
        print ('female count: ' + str(stats_response.entry.female_count))
        print ('child count: ' + str(stats_response.entry.child_count))
        print ('teen count: ' + str(stats_response.entry.teen_count))
        print ('young adult count: ' + str(stats_response.entry.young_adult_count))
        print ('adult count: ' + str(stats_response.entry.adult_count))
        print ('middle aged count: ' + str(stats_response.entry.middle_aged_count))
        print ('senior count: ' + str(stats_response.entry.senior_count))
        print ('unidentified count: ' + str(stats_response.entry.unidentified_count))
    elif option == '0':
        break