"""Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir.

Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)"""

number = int(input("Enter the number: "))

i = 1
total = 0

while(i < number):

    if(number % i == 0):
        total += i 
    i += 1

if(total == number):

    print("\n{} is a perfect number.".format(number))

else:
    
    print("\n{} is not a perfect number.".format(number))
