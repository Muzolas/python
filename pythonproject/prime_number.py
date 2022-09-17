"""
Asal sayılar : 1'e ve kendisinden başka sayıya bölünmeyen sayılardır.

"""

from xml.etree.ElementInclude import FatalIncludeError


def prime_number(number):

    if (number == 1):
        return False        # Bir asal olmadığı için değer olarak döndürmedik.

    elif(number == 2):    # En küçük asal sayımızı önceden belirttik çünkü asal sayılar içinden 2'ye bölünebilen tek sayı 2'dir.
        return True

    else:
        for i in range(2,number):

            if(number % i == 0):    # Sayımızın kendinden başka sayıya bölünüp bölünmediğini kontrol ettik
                return False    # Bölün sayı var ise asal sayı değildir

            return True     # Yoksa sayı asaldır

while True:

    number = input("Enter a number: ")

    if(number == "q"):       # Döngüden çıkmak için yazılan kod
        break

    else:
        number = int(number)

        if (prime_number(number)):
            print(number,"is a prime number...")
            print("-" * 25)

        else:
            print(number,"is not a prime number...")
            print("-" * 25)
            