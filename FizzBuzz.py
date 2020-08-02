def fizzbuzz(int):

    if int % 3 == 0 and int % 5 != 0:
        return "Fizz"
    elif int % 3 != 0 and int % 5 == 0:
        return "Buzz"
    elif int % 3 == 0 and int % 5 == 0:
        return "FizzBuzz"
    else:
        return int