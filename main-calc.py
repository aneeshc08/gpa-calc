'''
This will calculate the main grades
(A+ = 4.3)
(A = 4)
(A- = 3.7)
(B+ = 3.3)
(B = 3)
(B- = 2.7)
(C+ = 2.3)
(C = 2.0)
(C- = 1.7)
(D = 1)
(F = 0)

So we will be entering in a float and assign them a grade (A,A+,A-) and then calculating overall GPA
'''

calc2=int(input("Enter your Calc 2 Grade: "))
phys2=int(input("Enter your Physics 1 Grade: "))
ela2=int(input("Enter your ELA Grade: "))
econ2=int(input("Enter your Econ Grade: "))

if calc2 >= 98:
    calc2_letter = "A+"
elif calc2 >= 93:
    calc2_letter = "A"
elif calc2 >= 90:
    calc2_letter = "A-"
elif calc2 >= 88:
    calc2_letter = "B+"
elif calc2 >= 83:
    calc2_letter = "B"
elif calc2 >= 80:
    calc2_letter = "B-"
elif calc2 >= 78:
    calc2_letter = "C+"
elif calc2 >= 73:
    calc2_letter = "C"
elif calc2 >= 70:
    calc2_letter = "C-"
elif 60 <= calc2 <= 69:
    calc2_letter = "D"
elif calc2 <= 60:
    calc2_letter = "F"
#this is the values for the Letter grade classification
"A+" == 4.3
"A-" == 4.0
"A" == 3.7
"B+" == 3.3
"B" == 3.0
"B-" == 2.7
"C+" == 2.3
"C" == 2.0
"C-" == 1.7
"D" == 1
"F" == 0
#used the pick and choose shortcut (cmd+D)
if phys2 >= 98:
    phys2_letter = "A+"
elif phys2 >= 93:
    phys2_letter = "A"
elif phys2 >= 90:
    phys2_letter = "A-"
elif phys2 >= 88:
    phys2_letter = "B+"
elif phys2 >= 83:
    phys2_letter = "B"
elif phys2 >= 80:
    phys2_letter = "B-"
elif phys2 >= 78:
    phys2_letter = "C+"
elif phys2 >= 73:
    phys2_letter = "C"
elif phys2 >= 70:
    phys2_letter = "C-"
elif 60 <= phys2 <= 69:
    phys2_letter = "D"
elif phys2 <= 60:
    phys2_letter = "F"