import copy
import unittest
from typing import Any, Dict

from iot.edge.validator import compare_dictionary

DIRECT_METHOD_PAYLOAD_EX: Dict[str, Any] = {
    "input": {
        "body": {
            "command": "do something",
        },
        "headers": {
            "content_type": "application/json",
            "Authorization": "Bearer token",
        },
    },
    "output": {
        "body": {
            "command": "do something",
        },
        "headers": {
            "content_type": "application/json",
            "Authorization": "Bearer token",
        },
    },
}


class TestValidator(unittest.TestCase):
    """package validator testing"""

    def test_format_validation_success(self):
        payload = copy.deepcopy(DIRECT_METHOD_PAYLOAD_EX)
        error_msg = compare_dictionary(
            d1=DIRECT_METHOD_PAYLOAD_EX,
            d2=payload,
            value_match=False,
            recurse=True,
        )
        self.assertEqual(error_msg, "")

    def test_format_validation_failure(self):
        error_msg = compare_dictionary(
            d1=DIRECT_METHOD_PAYLOAD_EX,
            d2={"invalid": "keys"},
            value_match=False,
            recurse=True,
        )
        self.assertEqual(error_msg, "key invalid does not exist in d1")

    def test_value_validation_success(self):
        payload = copy.deepcopy(DIRECT_METHOD_PAYLOAD_EX)
        error_msg = compare_dictionary(
            d1=DIRECT_METHOD_PAYLOAD_EX,
            d2=payload,
            value_match=True,
            recurse=True,
        )
        self.assertEqual(error_msg, "")

    def test_value_validation_failure(self):
        payload = copy.deepcopy(DIRECT_METHOD_PAYLOAD_EX)
        payload["input"]["body"]["command"] = "do nothing"
        error_msg = compare_dictionary(
            d1=DIRECT_METHOD_PAYLOAD_EX,
            d2=payload,
            value_match=True,
            recurse=True,
        )
        self.assertEqual(
            error_msg, "key input has different values between d1[input] and d2[input]"
        )


if __name__ == "__main__":
    unittest.main()
