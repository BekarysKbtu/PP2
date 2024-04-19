import time
import math

def invoke_sqrt_after_delay(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(number)
    return result

number = int(input())
milliseconds = int(input())
print(f"Square root of {number} after {milliseconds} milliseconds is {invoke_sqrt_after_delay(number, milliseconds)}")
