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

calc2=float(input("Enter your Calc 2 Grade: "))
phys2=float(input("Enter your Physics 1 Grade: "))
ela2=float(input("Enter your ELA Grade: "))
econ2=float(input("Enter your Econ Grade: "))

A_plus = 4.3
A = 4.0
A_minus = 3.7
B_plus = 3.3
B = 3.0
B_minus = 2.7
C_plus = 2.3
C = 2.0
C_minus = 1.7
D = 1
F = 0

if calc2 >= 98:
    calc2_letter = A_plus
elif calc2 >= 93:
    calc2_letter = A
elif calc2 >= 90:
    calc2_letter = A_minus
elif calc2 >= 88:
    calc2_letter = B_plus
elif calc2 >= 83:
    calc2_letter = B
elif calc2 >= 80:
    calc2_letter = B_minus
elif calc2 >= 78:
    calc2_letter = C_plus
elif calc2 >= 73:
    calc2_letter = C
elif calc2 >= 70:
    calc2_letter = C_minus
elif calc2 >= 60:
    calc2_letter = D
else:
    calc2_letter = F

#this is the values for the Letter grade classification

#used the pick and choose shortcut (cmd+D)
if phys2 >= 98:
    phys2_letter = A_plus
elif phys2 >= 93:
    phys2_letter = A
elif phys2 >= 90:
    phys2_letter = A_minus
elif phys2 >= 88:
    phys2_letter = B_plus
elif phys2 >= 83:
    phys2_letter = B
elif phys2 >= 80:
    phys2_letter = B_minus
elif phys2 >= 78:
    phys2_letter = C_plus
elif phys2 >= 73:
    phys2_letter = C
elif phys2 >= 70:
    phys2_letter = C_minus
elif 60 <= phys2 <= 69:
    phys2_letter = D
elif phys2 >= 60:
    phys2_letter = D
else:
    phys2_letter = F

#ela2

if ela2 >= 98:
    ela2_letter = A_plus
elif ela2 >= 93:
    ela2_letter = A
elif ela2 >= 90:
    ela2_letter = A_minus
elif ela2 >= 88:
    ela2_letter = B_plus
elif ela2 >= 83:
    ela2_letter = B
elif ela2 >= 80:
    ela2_letter = B_minus
elif ela2 >= 78:
    ela2_letter = C_plus
elif ela2 >= 73:
    ela2_letter = C
elif ela2 >= 70:
    ela2_letter = C_minus
elif ela2 >= 60:
    ela2_letter = D
else:
    ela2_letter = F

#econ2

if econ2 >= 98:
    econ2_letter = A_plus
elif econ2 >= 93:
    econ2_letter = A
elif econ2 >= 90:
    econ2_letter = A_minus
elif econ2 >= 88:
    econ2_letter = B_plus
elif econ2 >= 83:
    econ2_letter = B
elif econ2 >= 80:
    econ2_letter = B_minus
elif econ2 >= 78:
    econ2_letter = C_plus
elif econ2 >= 73:
    econ2_letter = C
elif econ2 >= 70:
    econ2_letter = C_minus
elif econ2 >= 60:
    econ2_letter = D
else:
    econ2_letter = F

final_gpa = (calc2_letter + econ2_letter + phys2_letter + ela2_letter) / 4

print(f"Your Final Calculated GPA: {final_gpa}")