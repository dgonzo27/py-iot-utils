"""module parameter validation comparisons"""

from typing import Any, Dict, List, Optional


def compare_dictionary(
    d1: Dict[str, Any],
    d2: Dict[str, Any],
    value_match: Optional[bool] = False,
    recurse: Optional[bool] = True,
) -> str:
    """compare two dictionaries for keys, optionally recursive and optionally for exact value match"""
    for k in d2:
        if k not in d1:
            return f"key {k} does not exist in d1"

    for k in d1:
        if k not in d2:
            return f"key {k} does not exist in d2"

        if not isinstance(d1[k], type(d2[k])):
            return f"key {k} has different type between d1[{k}] and d2[{k}]"

        if isinstance(d1[k], dict):
            if recurse:
                error = compare_dictionary(d1[k], d2[k])
                if error:
                    return f"{k}: {error}"

        elif isinstance(d1[k], list):
            if recurse:
                error = compare_list(d1[k], d2[k])
                if error:
                    return f"{k}: {error}"

        elif d1[k] != d2[k] and value_match == True:
            return f"key {k} has different values between d1[{k}] and d2[{k}]"

    return ""


def compare_list(
    l1: List[Any],
    l2: List[Any],
    value_match: Optional[bool] = False,
    recurse: Optional[bool] = True,
) -> str:
    """compare two lists for length and type, optionally recursive and optionally for exact value match"""
    if len(l1) != len(l2):
        return f"length of l1 ({len(l1)}) and l2 ({len(l2)}) do not match"

    for i in range(len(l1)):
        if not isinstance(l1[i], type(l2[i])):
            return f"index {i} has different type between l1[{i}] and l2[{i}]"

        if isinstance(l1[i], dict):
            if recurse:
                error = compare_dictionary(l1[i], l2[i])
                if error:
                    return f"[{i}]: {error}"

        elif isinstance(l1[i], list):
            if recurse:
                error = compare_list(l1[i], l2[i])
                if error:
                    return f"[{i}]: {error}"

        elif l1[i] != l2[i] and value_match == True:
            return f"index {i} has different values between l1[{i}] and l2[{i}]"

    return ""
