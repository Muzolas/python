"""Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı

( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4"""

number = input("Enter a number: ")

number_of_digits = len(number)       # len() fonksiyonuyla basamak sayımız bulduk
number = int(number)
digits = 0
total = 0 

temporary_number = number       # Geçici bir sayı tanımladık

while temporary_number > 0:

    digits = temporary_number % 10      # Basamakları bulmak için sayımızı 10 a bölüp kalanını aldık

    total += digits ** number_of_digits

    temporary_number //= 10     # Sayımızı 10 a kalansız bölerek sayıyı bir basamak küçültttük

if(total == number):

    print("{} is the armstrong number...".format(number))

else:

    print("{} is not an armstrong number...".format(number))



















