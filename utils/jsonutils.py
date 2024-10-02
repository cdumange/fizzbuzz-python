from typing import TypeVar, Type
import json

T = TypeVar('T')

def from_json(value: str, typeOfT: Type) -> T | Exception:
    dic = json.loads(value)
    try:
        v = typeOfT(**dic)
        return v
    except Exception as e:
        return e
