"""
Faktoriyel bulan program.
"""

print("-" * 50)
print("\t  Factorial Discovery Program \n\tPress '-1' to exit the program.")
print("-" * 50)

while True:
    number = int(input("\nEnter the number to be factored into: "))

    if(number == -1):
        print("Program Termination...")
        break

    else:
        factorial = 1
        for i in range(2,number+1):
            factorial *= i
    
    print("\n{}! = {}".format(number,factorial))
    