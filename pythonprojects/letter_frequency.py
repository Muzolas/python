"""
Elinizde uzunca bir string olsun.

"ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.
"""

string =  list("ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb")

letter_dict = dict()

for i in string:

    if(i in letter_dict):
        letter_dict[i] += 1

    else:
        letter_dict[i] = 1
    
for letter,number in letter_dict.items():
    print("The letter {} appears {} times in the text.".format(letter,number))
    print("-" * 40)
