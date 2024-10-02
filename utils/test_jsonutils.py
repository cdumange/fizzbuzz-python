import pytest
from dataclasses import dataclass
from utils import jsonutils

@dataclass
class test:
    id: int
    value: str


def testParsingJSONOk():
    j = """{
        "id": 1,
        "value": "test"
    }"""

    obj = jsonutils.from_json(j, test)
    assert isinstance(obj, test)
    assert obj.id == 1
    assert obj.value == "test"

def testParsingJSONKo():
    j = """{
        "bla": 1,
        "blue": "test"
    }"""

    obj = jsonutils.from_json(j, test)
    assert isinstance(obj, Exception)