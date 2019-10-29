#try..except practice
"""
def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument')

print(spam(2))
print(spam(0))
print(spam(42))
"""
def spam(divideBy):
    return 42/divideBy

try:
    print(spam(2))
    print(spam(0))
    print(spam(42))
except ZeroDivisionError:
    print('Error: Invalid argument')
