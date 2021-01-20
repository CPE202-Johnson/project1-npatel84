def bears(n):

    if (n == 42):
        return True

    if (n < 42):
        return False

    if (n % 5 is 0) and bears(n - 42):
        return True

    elif (n % 2 is 0) and bears(n / 2):
        return True

    elif (n % 4 is 0) or (n % 3 is 0):
        
        a = n % 10
        b = (n % 100) / 10
        return a * b != 0 and bears(n - a * b)

    # return False

