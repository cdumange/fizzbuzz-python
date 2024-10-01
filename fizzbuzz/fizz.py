from dataclasses import dataclass
from typing import List

@dataclass
class FizzbuzzInput:
    int1: int
    int2: int
    str1: str
    str2: str
    limit: int

@dataclass
class FizzbuzzOutput:
    values: List[str]

def Compute(input: FizzbuzzInput) -> FizzbuzzOutput|Exception:
    if input.int1 == 0 or input.int2 == 0:
        return Exception("int1 and int2 can't be 0")
    if input.limit == 0:
        return FizzbuzzOutput([])
    
    ret = []
    for v in range(1, input.limit +1):
        divisible1 = (v % input.int1) == 0
        divisible2 = (v % input.int2) == 0
    
        if divisible1 and divisible2:
            ret.append(input.str1 + input.str2)
            continue
        if divisible1:
            ret.append(input.str1)
            continue
        if divisible2:
            ret.append(input.str2)
            continue
        ret.append(v.__str__())
    return FizzbuzzOutput(ret)
