"""
    Bir sayının tam bölenlerini listeleyen program

"""

def full_divisor(number):   # tam bölenleri bulan fonksiyon

    exact_divisors = []    # tam bölenler listesi

    for i in range(2,number):
        if(number % i == 0):
            exact_divisors.append(i)
    return exact_divisors

while True:

    number = input("\nEnter a number: ")
    if(number == "q"):
        print("Program quitting...")
        break
    else:
        number = int(number)
        print("Exact divisors:",full_divisor(number))
