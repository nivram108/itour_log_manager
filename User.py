from LogDatum import *
from LogTag import *

class User():
    def __init__(self, uid, name):
        self.uid = uid
        self.name = name
        self.togo_list = []
        self.viewed_notification = []
        self.viewed_checkin = []
        self.liked_checkin = []
        self.collected_checkin = []
        self.report_anywhere = []
        self.report_checkin = []
        pass
    def read_log(tag, checkin, location, timestamp):
        if tag == LOG_TOGO_ADD:
            self.togo_list.append(LogDatum(location, location, True, timestamp))
        elif tag == LOG_TOGO_REMOVE:
            self.togo_list.append(LogDatum(location, location, False, timestamp))
        elif tag == LOG_NOTIFICATION_CLICKED_HOT_CHECKIN:
            self.viewed_notification.append(LogDatum(checkin_id, location, True, timestamp))
        elif tag == LOG_CHECKIN_OPEN:
            self.viewed_checkin.append(LogDatum(checkin_id, location, True, timestamp))
        elif tag == LOG_CHECKIN_LIKE:
            self.liked_checkin.append(LogDatum(checkin_id, location, True, timestamp))
        elif tag == LOG_CHECKIN_UNLIKE:
            self.liked_checkin.append(LogDatum(checkin_id, location, False, timestamp))
        elif tag == LOG_CHECKIN_COLLECT_ADD:
            self.collected_checkin.append(LogDatum(checkin_id, location, True, timestamp))
        elif tag == LOG_CHECKIN_COLLECT_REMOVE:
            self.collected_checkin.append(LogDatum(checkin_id, location, False, timestamp))
        elif tag == LOG_REPORT_CHECKIN:
            self.report_checkin.append(LogDatum(checkin_id, location, True, timestamp))
        elif tag == LOG_REPORT_ANYWHERE
            self.report_anywhere.append(LogDatum(location, location, True, timestamp))
    def write_data():
        
