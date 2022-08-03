import unittest

from iot.edge.logger import init_logging


class TestLogger(unittest.TestCase):
    """package logger testing"""

    def test_log_levels(self):
        """
        align with syslog standard:

        https://en.wikipedia.org/wiki/Syslog#Severity_level
        """

        with self.assertLogs() as debug:
            logger = init_logging(module_name="test_log_lvl")
            logger.debug("debug log!")
        self.assertEqual(len(debug.records), 1)
        self.assertEqual(debug.records[0].message, "debug log!")
        self.assertEqual(debug.records[0].levelname, "DBG")
        self.assertEqual(debug.records[0].levelno, 7)

        with self.assertLogs() as info:
            logger = init_logging(module_name="test_log_lvl")
            logger.info("info log!")
        self.assertEqual(len(info.records), 1)
        self.assertEqual(info.records[0].message, "info log!")
        self.assertEqual(info.records[0].levelname, "INF")
        self.assertEqual(info.records[0].levelno, 6)

        with self.assertLogs() as warn:
            logger = init_logging(module_name="test_log_lvl")
            logger.warning("warning log!")
        self.assertEqual(len(warn.records), 1)
        self.assertEqual(warn.records[0].message, "warning log!")
        self.assertEqual(warn.records[0].levelname, "WRN")
        self.assertEqual(warn.records[0].levelno, 4)

        with self.assertLogs() as error:
            logger = init_logging(module_name="test_log_lvl")
            logger.error("error log!")
        self.assertEqual(len(error.records), 1)
        self.assertEqual(error.records[0].message, "error log!")
        self.assertEqual(error.records[0].levelname, "ERR")
        self.assertEqual(error.records[0].levelno, 3)

        with self.assertLogs() as critical:
            logger = init_logging(module_name="test_log_lvl")
            logger.critical("critical log!")
        self.assertEqual(len(critical.records), 1)
        self.assertEqual(critical.records[0].message, "critical log!")
        self.assertEqual(critical.records[0].levelname, "CRIT")
        self.assertEqual(critical.records[0].levelno, 2)


if __name__ == "__main__":
    unittest.main()
