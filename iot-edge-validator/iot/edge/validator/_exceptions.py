"""edge module exception responses"""

import traceback
import uuid
from typing import Optional

from azure.iot.device.iothub.models.methods import MethodRequest, MethodResponse


def generate_error_response(
    request: MethodRequest,
    message: str,
    status: Optional[int] = 500,
) -> MethodResponse:
    """given a method request, generate an error response"""
    resp_payload = {"error": message}
    try:
        return MethodResponse(request.request_id, status, resp_payload)
    except Exception:
        pass
    return MethodResponse(f"unknown-{uuid.uuid4()}", status, resp_payload)


def format_exception_error(context: str, exception: Exception) -> str:
    """format exceptions using traceback"""
    try:
        return (
            "Internal Error\n"
            "---------------\n"
            f"context: {context}\n"
            f"type: {exception.__class__.__name__}\n"
            f"detail: {exception}\n"
            f"trace: {traceback.format_exc()}"
        )
    except Exception:
        pass
    return (
        "Internal Error\n"
        "---------------\n"
        f"context: {context}\n"
        "detail: unable to format exception via traceback, skipping exception details..."
    )
