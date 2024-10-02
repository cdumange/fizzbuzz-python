from typing import TypeVar, Type
import json

T = TypeVar('T')

def from_json(value: str, typeOfT: Type) -> T:
    dic = json.loads(value)
    return typeOfT(**dic)
