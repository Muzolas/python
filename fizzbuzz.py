def fizzbuzz(number):
    
    if(number % 3 == 0 and number % 5 == 0):
        print("FizzBuzz")
    elif(number % 3 == 0):
        print("Fizz")
    elif(number % 5 == 0):
        print("Buzz")
    else:
        print(number)

length = int(input("Enter length of line (1-?): "))

