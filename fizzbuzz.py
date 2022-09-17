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

for i in range(1,length+1):
    
    fizzbuzz(i) 