"""
1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın.
Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.
Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır.
Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).
"""
def perfect_number(number):
    
    i = 1
    total = 0

    while(i < number):

        if(number % i == 0):
            total += i

        i += 1

    return total == number

for i in range(1,1001):

    if(perfect_number(i)):

        print(i,"is a perfect number.")
