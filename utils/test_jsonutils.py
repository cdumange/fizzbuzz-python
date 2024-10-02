from dataclasses import dataclass
from utils import from_json

@dataclass
class test:
    id: int
    value: str


def TestParsingJSONOk():
    j = """{
        "id": 1,
        "value": "test"
    }"""

    obj = from_json(j, test)
    assert isinstance(obj, test)
    assert obj.id == 1
    assert obj.value == "test"