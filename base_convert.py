
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    
    if num//b < 1:
        return str(helper_function(num, b))
    else:
        return str(convert(num//b, b)) + str(helper_function(num, b))  


def helper_function(num, b):

    if num%b < 10:
        return (num % b)

    if num%b == 10:
        return 'A'
    elif num%b == 11:
        return 'B'
    elif num%b == 12:
        return 'C'
    elif num%b == 13:
        return 'D'
    elif num%b == 14:
        return 'E'
    elif num%b == 15:
        return 'F'

