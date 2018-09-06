import pytest 

# the test commented out is to verify that pytest is running, you should have one test passing
# def test_canAssertTrue( ):
#     assert True
    
# Test 1: can I call FizzBuzz

def fizzBuzz( value ):
    if isMultiple( value, 3 ) and isMultiple( value, 5 ):
        return  "FizzBuzz"
    elif isMultiple( value, 3 ):
        return "Fizz"
    elif isMultiple ( value, 5 ):
        return "Buzz"
    elif isMultiple( value, 3 ) != 0 and isMultiple( value, 5 ) !=0:
        return "zzzz"
    return str(value)
    
def isMultiple( value, mod ):
    return ( value % mod ) == 0
    

def checkFizzBuzz( value, expectedReturnVal ):
    returnVal = fizzBuzz(value)
    assert returnVal == expectedReturnVal

# Test 2: Get "1" when passing in 1

def test_returns1With1PassedIn():
    checkFizzBuzz (1, "1")
    
# Test 3: get "2" when I pass in 2

def test_returns2With2PassedIn():
    checkFizzBuzz (2, "2")
    
    
# Test 4: get "Fizz" when I pass in 3

def test_returnsFizzWith3PassedIn():
    checkFizzBuzz (3, "Fizz")
    
# Test 5: get "Buzz" when I pass in 5

def test_returnsBuzzWith5PassedIn():
    checkFizzBuzz (5, "Buzz")
    
# Test 6: get "Fizz" when I pass in 6 (or any multiple of 3)

def test_returnsFizzWithMultipleOf3():
    checkFizzBuzz (6, "Fizz")
    
# Test 7: get "Buzz" when I pass in 10 (or any multiple of 5)

def test_returnsBuzzWithMultipleOf5():
    checkFizzBuzz (10, "Buzz")
    
# Test 8: get "FizzBuzz" when I pass in 15 (multiple of 3 and 5) 

def test_returnsFizzBuzzWithMultipleOf3And5():
    checkFizzBuzz (15, "FizzBuzz")
    
# Test 9: get "zzzz" when I pass in 11 (not a multiple of 3 and 5) 

def test_returnsZzzzWithNoMultipleOf3And5():
    checkFizzBuzz (11, "zzzz")