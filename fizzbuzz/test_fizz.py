import pytest
from fizzbuzz import fizz


@pytest.mark.parametrize(
    "input, expected", 
    [
        (fizz.FizzbuzzInput(3, 5, "fizz", "buzz", 15), fizz.FizzbuzzOutput(["1","2","fizz", "4","buzz","fizz","7","8","fizz","buzz","11","fizz","13","14","fizzbuzz"])),
        (fizz.FizzbuzzInput(3, 5, "fizz", "buzz", 0), fizz.FizzbuzzOutput([])),
    ])
def testGreenCases(input : fizz.FizzbuzzInput, expected : fizz.FizzbuzzOutput):
    assert fizz.Compute(input).values == expected.values

@pytest.mark.parametrize(
    "input",
    [
        (fizz.FizzbuzzInput(0, 3, "test", "t", 1)),
        (fizz.FizzbuzzInput(1, 0, "test", "t", 1)),
        (fizz.FizzbuzzInput(0, 0, "test", "t", 1)),
    ])
def Exceptions(input: fizz.FizzbuzzInput):
     assert fizz.Compute(input) is Exception

