"""IoT Edge common logging"""

import logging
import sys
from datetime import datetime
from typing import Optional, Union

import pytz

VALID_TIMEZONES = [
    "US/Alaska",
    "US/Central",
    "US/Eastern",
    "US/Mountain",
    "US/Pacific",
    "UTC",
]


class CustomLogFilter(logging.Filter):
    module_name: str

    def __init__(self, module_name: str) -> None:
        self.module_name = module_name

    def filter(self, record: logging.LogRecord) -> logging.LogRecord:
        """add the module name as a custom log filter"""
        record.module_name = self.module_name
        return record


class CustomLogFormatter(logging.Formatter):
    fmt: str
    datefmt: Union[str, None]
    timespec: str
    timezone: str

    def __init__(
        self,
        fmt: Optional[
            str
        ] = "<%(levelno)s> %(asctime)s [%(levelname)s] %(module_name)s %(message)s",
        datefmt: Optional[Union[str, None]] = None,
        timespec: Optional[str] = "milliseconds",
        timezone: Optional[str] = "UTC",
    ) -> None:
        self.fmt = fmt
        self.datefmt = datefmt
        self.timespec = timespec
        if timezone in VALID_TIMEZONES:
            self.timezone = timezone
        else:
            self.timezone = "UTC"

    def format_exception(self, exc_info: Exception) -> str:
        """format exceptions with repr"""
        result = super().format_exception(exc_info)
        return repr(result)

    def convert_to_syslog(self, record: logging.LogRecord) -> logging.LogRecord:
        """
        convert python log levels to syslog standard

        https://en.wikipedia.org/wiki/Syslog#Severity_level
        """
        if record.levelno == logging.DEBUG:
            record.levelno = 7
            record.levelname = "DBG"
        elif record.levelno == logging.INFO:
            record.levelno = 6
            record.levelname = "INF"
        elif record.levelno == logging.WARNING:
            record.levelno = 4
            record.levelname = "WRN"
        elif record.levelno == logging.ERROR:
            record.levelno = 3
            record.levelname = "ERR"
        elif record.levelno == logging.CRITICAL:
            record.levelno = 2
            record.levelname = "CRIT"
        return record

    def format(self, record: logging.LogRecord) -> str:
        """format a standard python log"""
        record = self.convert_to_syslog(record)
        formatter = logging.Formatter(self.fmt)
        result = formatter.format(record)
        if record.exc_text:
            result = result.replace("\n", "")
        return result

    def tz_converter(self, timestamp: str) -> datetime:
        """convert the timestamp of a log record to a specific timezone"""
        dt = datetime.fromtimestamp(timestamp)
        tzinfo = pytz.timezone(self.timezone)
        return tzinfo.localize(dt)

    def format_time(self, record: logging.LogRecord) -> str:
        """format the timestamp of a log record"""
        dt = self.tz_converter(record.created, self.timezone)
        if self.datefmt:
            result = dt.strftime(self.datefmt)
        else:
            try:
                result = dt.isoformat(" ", timespec=self.timespec)
            except TypeError:
                result = dt.isoformat()
                pass
            result = result.replace("+", " +")
        return result


def init_logging(
    module_name: str,
    level: Optional[str] = "DEBUG",
    format: Optional[
        str
    ] = "<%(levelno)s> %(asctime)s [%(levelname)s] %(module_name)s %(message)s",
    datefmt: Optional[Union[str, None]] = None,
    timespec: Optional[str] = "milliseconds",
    timezone: Optional[str] = "UTC",
) -> logging.Logger:
    """initialize log handlers"""
    logger = logging.getLogger(__name__)
    logger.setLevel(getattr(logging, level))

    # create console handler
    console = logging.StreamHandler(sys.stdout)
    console.setLevel(level)

    # configure custom log filter
    filter = CustomLogFilter(module_name=module_name)
    logger.addFilter(filter)

    # configure custom log formatter
    formatter = CustomLogFormatter(
        fmt=format, datefmt=datefmt, timespec=timespec, timezone=timezone
    )
    console.setFormatter(formatter)
    logger.addHandler(console)

    return logger
