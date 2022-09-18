"""
Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.
"""

ones_digit = [" ","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
tens_digit = [" ","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]

def pronunciation(number):

    ones = number % 10   # birler basamağı belirlendi
    tens = number // 10    # onlar basamağı belirlendi

    return tens_digit[tens] + " " + ones_digit[ones]

print("-" * 50)
print("\t  Press 'q' to end the program.")
print("-" * 50)

while True:

    number = int(input("\nEnter a two-digit number: "))

    if(number == "q"):       # Döngüden çıkmak için yazılan kod
        break

    else:
       print("Read the number entered: {}".format(pronunciation(number)))
            