""" Sayı tahmin oyunu """

import random
import time

print("""--------------------------------------------------
          1-100 Number Prediction Game 
        Your Right to Guess is 6 Of You...  
--------------------------------------------------""")

random_number = random.randint(1, 100)  # rastgele sayımızı seçiyoruz

number_of_predictions = 6   # tahmin hakkı sayısı

while True:
    prediction = int(input("\nYour guess: "))

    if (prediction < random_number):   # tahminimizin sayıdan küçük olması durumu
        print("\nProcessing data...")
        time.sleep(1)

        print("\nEnter a higher number...")

        number_of_predictions -= 1

        print("\nYour remaining right: {}\n\n".format(number_of_predictions))
        print("-" * 50)

    elif (prediction > random_number):   # tahminimizin sayıdan büyük olması durumu
        print("\nProcessing data...")
        time.sleep(1)

        print("\nEnter a lower number...")

        number_of_predictions -= 1

        print("\nYour remaining right: {}\n\n".format(number_of_predictions))
        print("-" * 50)

    else:   # tahminimizin sayıya eşit olması durumu
        print("\nProcessing data...")
        time.sleep(1)

        print("\nCongratulations! Number:", random_number)

    if (number_of_predictions == 0):  # tahmin hakkımız biterse durumu
        print("\nYour guess count is over...")
        print("\nNumber:", random_number)
        break
