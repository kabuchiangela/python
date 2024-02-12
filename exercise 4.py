print("grades calculator.")
maths = int(input("maths: "))
eng = int(input("eng: "))
physics = int(input("physics: "))
kiswahili = int(input("kiswahili: "))
geography = int(input("geography: "))
chemistry = int(input("chemistry: "))
agriculture = int(input("agriculture: "))
grade =(maths + eng + physics + kiswahili + geography + chemistry + agriculture)/7

if grade > 0 and grade < 20:
    print("grade E")
elif grade > 21 and grade < 33:
    print("grade D")
elif grade > 34 and grade < 41:
    print("grade D+")
elif grade > 42 and grade < 52:
    print("grade C")
elif grade > 53 and grade < 61:
    print("grade C+")
elif grade > 62 and grade < 71:
    print("grade B")
elif grade > 72 and grade < 81:
    print("grade B+")
elif grade > 82 and grade < 91:
    print("grade A-")
elif grade > 92 and grade < 100:
    print("grade A")
else:
    print("invalid input")