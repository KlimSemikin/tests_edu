# coding=utf-8
from datetime import datetime, timezone
import tzlocal
from framework.constants.date_time_constants import TIMESTAMP_FORMAT_FOR_SQL


class DatetimeUtil(object):
    @staticmethod
    def get_str_datetime(exp_format=TIMESTAMP_FORMAT_FOR_SQL):
        return datetime.now().strftime(exp_format)

    @staticmethod
    def get_current_time(offset_from_utc=0, date_time_format="%H:%M"):
        utc_dt = datetime.now(timezone.utc)
        dt = utc_dt.replace(hour=utc_dt.time().hour + offset_from_utc)
        return dt.strftime(date_time_format)

    @staticmethod
    def from_unix(unix_timestamp):
        local_timezone = tzlocal.get_localzone()  # get pytz timezone
        return datetime.fromtimestamp(unix_timestamp, local_timezone).strftime(TIMESTAMP_FORMAT_FOR_SQL)
