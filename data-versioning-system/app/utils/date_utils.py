def data_utils():
    from datetime import datetime
    import pytz

    def get_current_utc_time():
        return datetime.now(pytz.utc)

    def convert_to_timezone(utc_time, timezone_str):
        local_tz = pytz.timezone(timezone_str)
        return utc_time.astimezone(local_tz)

    return {
        "get_current_utc_time": get_current_utc_time,
        "convert_to_timezone": convert_to_timezone
    }