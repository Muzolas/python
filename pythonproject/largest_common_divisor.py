"""
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen
bir tane fonksiyon yazın.
"""

def lcd(number1,number2):
    i = 1
    lcd = 1

    while (i <= number1 and i <= number2):
        if not(number1 % i) and not(number2 % i):
            lcd = i 
        i += 1

    return lcd

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

print("\nLargest common divisor: {}".format(lcd(number1,number2)))
