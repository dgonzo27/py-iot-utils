import unittest

from azure.iot.device.iothub.models.methods import MethodResponse

from iot.edge.validator import generate_error_response, format_exception_error


class TestExceptions(unittest.TestCase):
    """package exceptions testing"""

    def test_generate_error_success(self):
        method_request = {"request_id": "test"}
        error_resp = generate_error_response(
            request=method_request,
            message="test message",
            status=500,
        )
        self.assertIsInstance(error_resp, MethodResponse)

    def test_generate_error_fail(self):
        method_request = "invalid"
        error_resp = generate_error_response(
            request=method_request,
            message="test message",
            status=500,
        )
        self.assertIsInstance(error_resp, MethodResponse)

    def test_format_exception_success(self):
        exception_resp = ""
        test_dictionary = {"hello": "world"}
        try:
            test_dictionary = test_dictionary["fail"]
        except Exception as ex:
            exception_resp = format_exception_error("testing success", ex)
            pass
        self.assertIsNotNone(exception_resp)

    def test_format_exception_fail(self):
        exception_resp = format_exception_error("testing failure", "fake exception")
        self.assertIsNotNone(exception_resp)


if __name__ == "__main__":
    unittest.main()
