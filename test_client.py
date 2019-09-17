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
    print ('8 - get total people stats')
    print ('9 - get face stats')
    print ('10 - get hourly face stats')
    print ('11 - get total face stats')
    print ('0 - exit')
    
    
client = Client()
option = ''
while option != '0':
    print_menu()
    option = input()
    print ('***********************************')
    print ('sending request...')
    if option == '1':
        print ('result: ' + client.enable_face_detection())
    elif option == '2':
        print ('result: ' + client.disable_face_detection())
    elif option == '3':
        print ('result: ' + client.enable_people_detection())
    elif option == '4':
        print ('result: ' + client.disable_people_detection())
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
            print ('detected time: ' + stats_response.entries[i].arrived)
            print ('left time: ' + stats_response.entries[i].left)
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
            print ('count: ' + str(stats_response.entries[i].count))
            i += 1            
    elif option == '8':
        d = datetime.datetime.today()
        start_time = str(d.year) + str(d.month).zfill(2) + str(d.day).zfill(2) + 'T000000'
        end_time = str(d.year) + str(d.month).zfill(2) + str(d.day).zfill(2) + 'T235959'
        stats_response = client.get_total_statistics(start_time, end_time)
        print ('count: ' + str(stats_response.entry.count))
    elif option == '9':
        d = datetime.datetime.today()
        start_time = str(d.year) + str(d.month).zfill(2) + str(d.day).zfill(2) + 'T000000'
        end_time = str(d.year) + str(d.month).zfill(2) + str(d.day).zfill(2) + 'T235959'
        stats_response = client.get_face_statistics(start_time, end_time)
        i = 0
        while i < len(stats_response.entries):
            print ('id: ' + str(stats_response.entries[i].id))
            print ('gender: ' + stats_response.entries[i].gender)
            print ('lower age: ' + str(stats_response.entries[i].age_lower))
            print ('upper age: ' + str(stats_response.entries[i].age_higher))
            print ('detected time: ' + stats_response.entries[i].detected_time)
            i += 1
    elif option == '10':
        d = datetime.datetime.today()
        start_time = str(d.year) + str(d.month).zfill(2) + str(d.day).zfill(2) + 'T000000'
        end_time = str(d.year) + str(d.month).zfill(2) + str(d.day).zfill(2) + 'T235959'
        stats_response = client.get_hourly_face_statistics(start_time, end_time)
        i = 0
        while i < len(stats_response.entries):
            print ('start: ' + str(stats_response.entries[i].start))
            print ('end: ' + str(stats_response.entries[i].end))
            print ('male count: ' + str(stats_response.entries[i].male_count))
            print ('female count: ' + str(stats_response.entries[i].female_count))
            print ('child/teen count: ' + str(stats_response.entries[i].child_teen_count))
            print ('young adult count: ' + str(stats_response.entries[i].young_adult_count))
            print ('adult count: ' + str(stats_response.entries[i].adult_count))
            print ('middle aged count: ' + str(stats_response.entries[i].middle_aged_count))
            print ('senior count: ' + str(stats_response.entries[i].senior_count))
            i += 1
    elif option == '11':
        d = datetime.datetime.today()
        start_time = str(d.year) + str(d.month).zfill(2) + str(d.day).zfill(2) + 'T000000'
        end_time = str(d.year) + str(d.month).zfill(2) + str(d.day).zfill(2) + 'T235959'
        stats_response = client.get_total_face_statistics(start_time, end_time)
        print ('male count: ' + str(stats_response.entry.male_count))
        print ('female count: ' + str(stats_response.entry.female_count))
        print ('child/teen count: ' + str(stats_response.entry.child_teen_count))
        print ('young adult count: ' + str(stats_response.entry.young_adult_count))
        print ('adult count: ' + str(stats_response.entry.adult_count))
        print ('middle aged count: ' + str(stats_response.entry.middle_aged_count))
        print ('senior count: ' + str(stats_response.entry.senior_count))
    elif option == '0':
        print ('exitting...')
        break
    else:
        print ('invalid selection')


    print ('***********************************')