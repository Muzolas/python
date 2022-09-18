"""
Decarator kullanımı.
"""

def extra(function): # decarator 

    def wrapper(numbers):  # fonksiyon içinde fonksiyon

        evens_total = 0
        even_numbers = 0
        odds_total = 0
        odd_numbers = 0    

        for number in numbers: 

            if(number % 2 == 0):

                evens_total += number
                even_numbers +=1

            else:

                odds_total += number
                odd_numbers +=1

        print("\nAverage of odd numbers:",odds_total/odd_numbers)   # tek sayıların ortalaması heseaplandı
        print("\nAverage of even numbers:",evens_total/even_numbers)    # çift sayıların ortalaması heseaplandı

        function(numbers)

    return wrapper

@extra # decarator çağırıldı
def average(numbers):

    total = 0

    for number in numbers:

        total += number

    print("\nOverall average:",total/len(numbers)) # genel ortalama heseaplandı

average([1,2,3,4,5,6,7,8,9,10])
