import requests
import json
from stats_response import StatsResponse
from hourly_stats_response import HourlyStatsResponse
from total_stats_response import TotalStatsResponse
from face_stats_response import FaceStatsResponse
from face_hourly_stats_response import FaceHourlyStatsResponse
from total_face_stats_response import TotalFaceStatsResponse

class Client:

    url = 'http://localhost:5000'

    def enable_face_detection(self):
    
        request_url = self.url + '/enable-feature?feature=face'
        result = self.send_control_request(request_url)
        return result
    
    
    def disable_face_detection(self):
    
        request_url = self.url + '/disable-feature?feature=face'
        result = self.send_control_request(request_url)
        return result
        
        
    def enable_people_detection(self):
    
        request_url = self.url + '/enable-feature?feature=people'
        result = self.send_control_request(request_url)
        return result


    def disable_people_detection(self):
    
        request_url = self.url + '/disable-feature?feature=people'
        result = self.send_control_request(request_url)
        return result
        
        
    def send_control_request(self, request_url):
    
        response = requests.get(request_url)
        response_json = json.loads(response.text)
        if (response_json["result"] != 'success'):
            raise Exception(response_json["reason"])
        return 'ok'
            
            
    def get_status(self):
    
        response = requests.get(self.url + '/status')
        response_json = json.loads(response.text)
        return response_json["status"] + ', version: ' + response_json["version"]
        
        
    def get_statistics(self, start_time, end_time):
    
        response = requests.get(self.url + '/people_stats?start=' + start_time + '&end=' + end_time)
        stats_response = StatsResponse(response.text)
        return stats_response

        
    def get_hourly_statistics(self, start_time, end_time):
    
        response = requests.get(self.url + '/hourly_people_stats?start=' + start_time + '&end=' + end_time)
        stats_response = HourlyStatsResponse(response.text)
        return stats_response        
        
        
    def get_total_statistics(self, start_time, end_time):
    
        response = requests.get(self.url + '/total_people_stats?start=' + start_time + '&end=' + end_time)
        stats_response = TotalStatsResponse(response.text)
        return stats_response


    def get_face_statistics(self, start_time, end_time):
        response = requests.get(self.url + '/face_stats?start=' + start_time + '&end=' + end_time)
        stats_response = FaceStatsResponse(response.text)
        return stats_response


    def get_hourly_face_statistics(self, start_time, end_time):
        response = requests.get(self.url + '/hourly_face_stats?start=' + start_time + '&end=' + end_time)
        stats_response = FaceHourlyStatsResponse(response.text)
        return stats_response


    def get_total_face_statistics(self, start_time, end_time):
        response = requests.get(self.url + '/total_face_stats?start=' + start_time + '&end=' + end_time)
        stats_response = TotalFaceStatsResponse(response.text)
        return stats_response
