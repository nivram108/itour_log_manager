uid, name, location, is togo, view from notification, view from check-in, like, saved, type
user, location,
is togo,
	report timestamp <> add togo
    LOG_TOGO_ADD, LOG_TOGO_REMOVE
view from notification,
	report timestamp > click notification
    LOG_NOTIFICATION_CLICKED_HOT_CHECKIN
    #LOG_NOTIFICATION_HOT_SPOT
view from check-in,
	report timestamp > click notification
    LOG_CHECKIN_OPEN
like,
	report timestamp <> like
    LOG_CHECKIN_LIKE
    LOG_CHECKIN_UNLIKE
saved
	report timestamp <> save
    LOG_CHECKIN_COLLECT_ADD
    LOG_CHECKIN_COLLECT_REMOVE
