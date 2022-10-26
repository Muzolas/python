"""
1'den 1000'e kadar olan asal sayıları ekrana yazdıran bir program yazın.
Daha sonra bir tane decorator fonksiyon kullanarak bu fonksiyona 1'den 1000'e
kadar olan mükemmel sayıları yazdırma özelliği ekleyin.
"""

def decarator(function):

    def wrapper():
        print("Perfect numbers...")   # Muhteşem sayıları bulan fonksiyon
        for number in range(1,1001):
            i = 1
            total = 0

            while(i < number):

                if(number % i == 0):
                    total += i
                i += 1

            if(total == number):
                print(number)

        function()

    return wrapper

@decarator   # Ekstra özellik olarak muhteşem sayıları buluyoruz
def prime_number():
    print("Prime numbers...")   # Asal sayıları bulan fonksiyon 

    for number in range(2,1001):
        i = 2
        numb = 0 
    
        while(i < number):

            if(number % i == 0):
                numb += 1
            i += 1

        if(numb == 0):
            print(number)

prime_number()
