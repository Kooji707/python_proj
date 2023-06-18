def fizz_buzz(input):
    tmp = ""
    if (input % 3 == 0) and (input % 5 == 0):
        tmp = "FizzBuzz"
    elif input % 3 == 0:
        tmp = "Fizz"
    elif input % 5 == 0:
        tmp = "Buzz"
    else:
        tmp = input

    return tmp

print(fizz_buzz(8))