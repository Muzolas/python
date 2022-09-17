from random import randint

""" Küçük çapta bir çarpım oyunu """

print("-" * 50)
print("\t\t  Hoşgeldiniz")
print("-" * 50)

def multiplication(a, b ,c):

    if(c != -1):        # c değeri -1 olmadığı sürece bu kod bloğuna giricektir
        result = str(a * b)

        if(result == c):     # c değeri sonuca eşit olunca bu kod bloğuna giricektir
            print("\n\t\t***** The correct answer. *****")
        
        else:
            print("\n\t***** The wrong answer would be %s. *****" % result)

    else:
        choice()

def start(space1,space2):

    if(space1 > 10):    # Bölümlerde zorluğa göre kaç soru çıkacağını gösteren kod
        x = 10

    else:
        x = 5

    for i in range(0,x):    # Seçilen zorlukğa göre soruların hazırlandığı yerler
        for j in range(0,x):    

            number1 = randint(space1,space2)    # Zorluğa göre aralık ayarlaması
            number2 = randint(space1,space2)    # Zorluğa göre aralık ayarlaması

            print("-" * 50, "\n")

            print("\t\t%d x %d equals how much?\n" % (number1,number2)) # soru

            result1 = input("Result >> ")

            multiplication(number1,number2,result1)

            if(i == 1 and j == 1):  # Bir sonraki zorluğa geçiş kısmı
                print("\n *-- This section is over, you can move to the next section --*\n")
                choice()

def choice():


    print("Choose the difficulty of the game!\n\n1 - Easy\n2 - Medium\n3 - Difficult\n4 - Very difficult\n")

    degree = input(">>> ")   # Oyunun derece seçimi

    if(degree == "1"):
        start(1,6)
    elif (degree == "2"):
        start(6,12)
    elif (degree == "3"):
        start(12,25)
    elif (degree == "4"):
        start(25,100)
    else:
        exit(0)

if __name__ == '__main__':
    choice()