import requests
import json
from stats_response import StatsResponse
from hourly_stats_response import HourlyStatsResponse
from total_stats_response import TotalStatsResponse

class Client:

    def enable_face_detection(self):
    
        request_url = 'http://localhost:5000/enable_feature?feature=face'
        self.send_control_request(request_url)
    
    
    def disable_face_detection(self):
    
        request_url = 'http://localhost:5000/disable_feature?feature=face'
        self.send_control_request(request_url)        
        
        
    def enable_people_detection(self):
    
        request_url = 'http://localhost:5000/enable_feature?feature=people'
        self.send_control_request(request_url)        


    def disable_people_detection(self):
    
        request_url = 'http://localhost:5000/disable_feature?feature=people'
        self.send_control_request(request_url)        
        
        
    def send_control_request(self, request_url):
    
        response = requests.get(request_url)
        response_json = json.loads(response.text)
        if (response_json["result"] != 'success'):
            raise Exception(response_json["reason"])
            
            
    def get_status(self):
    
        response = requests.get('http://localhost:5000/status')
        response_json = json.loads(response.text)
        return response_json["status"]
        
        
    def get_statistics(self, start_time, end_time):
    
        response = requests.get('http://localhost:5000/stats?start=' + start_time + '&end=' + end_time)
        stats_response = StatsResponse(response.text)
        return stats_response

        
    def get_hourly_statistics(self, start_time, end_time):
    
        response = requests.get('http://localhost:5000/hourly_stats?start=' + start_time + '&end=' + end_time)
        stats_response = HourlyStatsResponse(response.text)
        return stats_response        
        
        
    def get_total_statistics(self, start_time, end_time):
    
        response = requests.get('http://localhost:5000/total_stats?start=' + start_time + '&end=' + end_time)
        stats_response = TotalStatsResponse(response.text)
        return stats_response                