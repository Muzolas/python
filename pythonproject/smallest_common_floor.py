"""
Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen
bir tane fonksiyon yazın.
"""

def smf(number1,number2):
    
    i = number1
    while (i <= number1 * number2):
        if(i % number1 == 0 and i % number2 == 0):
            smf = i
        i += 1
    return smf

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

print("\nSmallest common floor: {}".format(smf(number1,number2)))
