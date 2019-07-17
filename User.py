from LogDatum import *
from LogTag import *

class User():
    def __init__(self, uid, name, checkin_location_dict, file_name):
        self.uid = uid
        self.name = name
        self.checkin_location_dict = checkin_location_dict
        self.togo_list = []
        self.viewed_notification_hot_checkin = []
        self.viewed_notification_hot_spot = []
        self.viewed_checkin = []
        self.liked_checkin = []
        self.collected_checkin = []
        self.report_anywhere = []
        self.report_checkin = []
        self.report_togo = []
        self.file_name = file_name
    def read_log(self, tag, msg, timestamp):
        location = msg
        if tag == LOG_TOGO_ADD:
            location = msg
            self.togo_list.append(LogDatum(location, location, True, timestamp))
        elif tag == LOG_TOGO_REMOVE:
            location = msg
            self.togo_list.append(LogDatum(location, location, False, timestamp))
        elif tag == LOG_NOTIFICATION_CLICKED_HOT_CHECKIN:
            checkin_id = msg
            if checkin_id in self.checkin_location_dict:
                location = self.checkin_location_dict[checkin_id]
            self.viewed_notification_hot_checkin.append(LogDatum(checkin_id, location, True, timestamp))
        elif tag == LOG_NOTIFICATION_CLICKED_HOT_SPOT:
            location = msg
            self.viewed_notification_hot_spot.append(LogDatum(location, location, True, timestamp))
        elif tag == LOG_CHECKIN_OPEN:
            checkin_id = msg
            if checkin_id in self.checkin_location_dict:
                location = self.checkin_location_dict[checkin_id]
            self.viewed_checkin.append(LogDatum(checkin_id, location, True, timestamp))
        elif tag == LOG_CHECKIN_LIKE:
            checkin_id = msg
            if checkin_id in self.checkin_location_dict:
                location = self.checkin_location_dict[checkin_id]
            self.liked_checkin.append(LogDatum(checkin_id, location, True, timestamp))
        elif tag == LOG_CHECKIN_UNLIKE:
            checkin_id = msg
            if checkin_id in self.checkin_location_dict:
                location = self.checkin_location_dict[checkin_id]
            self.liked_checkin.append(LogDatum(checkin_id, location, False, timestamp))
        elif tag == LOG_CHECKIN_COLLECT_ADD:
            checkin_id = msg
            if checkin_id in self.checkin_location_dict:
                location = self.checkin_location_dict[checkin_id]
            self.collected_checkin.append(LogDatum(checkin_id, location, True, timestamp))
        elif tag == LOG_CHECKIN_COLLECT_REMOVE:
            checkin_id = msg
            if checkin_id in self.checkin_location_dict:
                location = self.checkin_location_dict[checkin_id]
            self.collected_checkin.append(LogDatum(checkin_id, location, False, timestamp))
        elif tag == LOG_REPORT_CHECKIN:
            checkin_id = msg
            if checkin_id in self.checkin_location_dict:
                location = self.checkin_location_dict[checkin_id]
            self.report_checkin.append(LogDatum(checkin_id, location, True, timestamp))
        elif tag == LOG_REPORT_ANYWHERE:
            location = msg
            self.report_anywhere.append(LogDatum(location, location, True, timestamp))

        elif tag == LOG_REPORT_TOGO:
            location = msg
            self.report_togo.append(LogDatum(location, location, True, timestamp))

    def write_data(self):
        self.togo_list.sort(key=lambda x: x.timestamp)
        #for togo_data in self.togo_list:
        #    print(self.name + " togo: " + togo_data.location + "," + str(togo_data.flag) + " (" + str(togo_data.timestamp) + ")")
        for log in self.report_anywhere:
            uid = self.uid
            name = self.name
            location = log.location
            is_togo_result = self.get_result_by_location(log, self.togo_list)
            is_viewed_from_notification_result = self.get_result_by_checkin_id(log, self.viewed_notification_hot_checkin) or self.get_result_by_location(log, self.viewed_notification_hot_spot)
            is_viewed_from_checkin_result = self.get_result_by_checkin_id(log, self.viewed_checkin)
            liked_result = self.get_result_by_checkin_id(log, self.liked_checkin)
            saved_result = self.get_result_by_checkin_id(log, self.collected_checkin)
            self.write_reported(uid + "," + name + "," + location + "," + is_togo_result + "," + is_viewed_from_notification_result + "," + is_viewed_from_checkin_result + "," + liked_result + "," + saved_result + "," + "report anywhere")
        for log in self.report_checkin:
            uid = self.uid
            name = self.name
            location = log.location
            is_togo_result = self.get_result_by_location(log, self.togo_list)
            is_viewed_from_notification_result = self.get_result_by_checkin_id(log, self.viewed_notification_hot_checkin) or self.get_result_by_location(log, self.viewed_notification_hot_spot)
            is_viewed_from_checkin_result = self.get_result_by_checkin_id(log, self.viewed_checkin)
            liked_result = self.get_result_by_checkin_id(log, self.liked_checkin)
            saved_result = self.get_result_by_checkin_id(log, self.collected_checkin)
            self.write_reported(uid + "," + name + "," + location + "," + is_togo_result + "," + is_viewed_from_notification_result + "," + is_viewed_from_checkin_result + "," + liked_result + "," + saved_result + "," + "report saved")
        for log in self.report_togo:
            uid = self.uid
            name = self.name
            location = log.location
            is_togo_result = self.get_result_by_location(log, self.togo_list)
            is_viewed_from_notification_result = self.get_result_by_checkin_id(log, self.viewed_notification_hot_checkin) or self.get_result_by_location(log, self.viewed_notification_hot_spot)
            is_viewed_from_checkin_result = self.get_result_by_checkin_id(log, self.viewed_checkin)
            liked_result = self.get_result_by_checkin_id(log, self.liked_checkin)
            saved_result = self.get_result_by_checkin_id(log, self.collected_checkin)
            self.write_reported(uid + "," + name + "," + location + "," + is_togo_result + "," + is_viewed_from_notification_result + "," + is_viewed_from_checkin_result + "," + liked_result + "," + saved_result + "," + "report togo")

        togo_map = {}
        for log in self.togo_list:
            togo_map[log.location] = log
        for key, log in togo_map.items():
            if log.flag == True and self.unvisited(log):
                uid = self.uid
                name = self.name
                location = log.location
                is_togo_result = self.get_result_by_location(log, self.togo_list)
                is_viewed_from_notification_result = self.get_result_by_checkin_id(log, self.viewed_notification_hot_checkin) or self.get_result_by_location(log, self.viewed_notification_hot_spot)
                is_viewed_from_checkin_result = self.get_result_by_checkin_id(log, self.viewed_checkin)
                liked_result = self.get_result_by_checkin_id(log, self.liked_checkin)
                saved_result = self.get_result_by_checkin_id(log, self.collected_checkin)
                self.write_unvisited(uid + "," + name + "," + location + "," + is_togo_result + "," + is_viewed_from_notification_result + "," + is_viewed_from_checkin_result + "," + liked_result + "," + saved_result + "," + "report togo")

    def get_result_by_location(self, log, log_data_list):
        result = False
        for log_data in log_data_list:
            if log.location == log_data.location and log.timestamp > log_data.timestamp:
                #print(log.location + " > " + str(log.timestamp) + ", " + str(log_data.timestamp))
                result = log_data.flag
        return str(result)
    def get_result_by_checkin_id(self, log, log_data_list):
        result = False
        for log_data in log_data_list:
            if log.checkin_id == log_data.checkin_id and log.timestamp > log_data.timestamp:
                result = log_data.flag
        return str(result)
    def unvisited(self, log):
        result = True
        flag = True
        for log_data in self.togo_list:
            if log.location == log_data.location and log.timestamp > log_data.timestamp:
                #print(log.location + " > " + str(log.timestamp) + ", " + str(log_data.timestamp))
                flag = log_data.flag
        if flag == False:
            return False
        for log_data in self.report_togo:
            if log.location == log_data.location:
                print(self.name + " visited " + log.location)
                return False
        for log_data in self.report_checkin:
            if log.location == log_data.location:
                print(self.name + " visited " + log.location)
                return False
        for log_data in self.report_anywhere:
            if log.location == log_data.location:
                print(self.name + " visited " + log.location)
                return False
        return True
    def write_reported(self, data):
        reported_file = open("reported_" + self.file_name, "a+")
        reported_file.write(data.encode("utf-8") + "\n")
    def write_unvisited(self, data):
        unvisited_file = open("unvisited_" + self.file_name, "a+")
        unvisited_file.write(data.encode("utf-8") + "\n")
