"""
1'den 10'kadar olan sayılarla ekrana çarpım tablosu yazdıran program.
"""

for i in range(1,11):

    print("------------")

    for j in range(1,11):

        print("{} x {} = {}".format(i,j,i*j))
        