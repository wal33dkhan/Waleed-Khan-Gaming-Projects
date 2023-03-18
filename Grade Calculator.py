
import math


#printing the instructional output to the user
print("Enter grades for the full assignments")


"""
asking user for the inputs of each individiual grades for full assignments
this program has limitations as any value that is not between 0 - 4.3 would not produce accurate results
we are also assuming that there are bonuses available for all assignments
the inputs should only be numerical values as any strings would break the program
"""
a1_input = float(input("A1 grade (0 - 4.3): "))
a2_input = float(input("A2 grade (0 - 4.3): "))
a3_input = float(input("A3 grade (0 - 4.3): "))
a4_input = float(input("A4 grade (0 - 4.3): "))


#asking the user for the inputs of each individual grades for the mini assignments
print("\nEntering grades for the mini-assignments")


mini_a2 = float(input("Mini-A2 grade (0 - 4.3): ".rjust(26)))
mini_a3A = float(input("Mini-A3a grade (0 - 4.3): "))
mini_a3B = float(input("Mini-A3b grade (0 - 4.3): "))
mini_a4A = float(input("Mini-A4a grade (0 - 4.3): "))
mini_a4B = float(input("Mini-A4b grade (0 - 4.3): "))
mini_a4C = float(input("Mini-A4c grade (0 - 4.3): "))


#specifying the number of decimal places for the grades and assigning them to new variables
full_a1 = math.floor(a1_input*10)/10
full_a2 = math.floor(a2_input*10)/10
full_a3 = math.floor(a3_input*10)/10
full_a4 = math.floor(a4_input*10)/10
#the way above is not specifying format explicitly, however is cutting down decimal places by taking the floor in all cases


#doing the same as above but for the mini assignments
mini_A2  = math.floor(mini_a2*10)/10
mini_A3a = math.floor(mini_a3A*10)/10
mini_A3b = math.floor(mini_a3B*10)/10
mini_A4a = math.floor(mini_a4A*10)/10
mini_A4b = math.floor(mini_a4B*10)/10
mini_A4c = math.floor(mini_a4C*10)/10


#calculations happen here
w_f_a = (full_a1 * 0.15) + (full_a2 * 0.20) + (full_a3 * 0.22) + (full_a4 * 0.25)
w_m_a = (mini_A2 * 0.03) + (mini_A3a * 0.03) + (mini_A3b * 0.03) + (mini_A4a * 0.03) + (mini_A4b * 0.03) + (mini_A4c * 0.03)
t_gpa = (w_f_a + w_m_a)


"""
Here, using the weights for each assignment (weights are different for the mini assignments VS
the full assignments). Calculate the grade by multiplying the grade x weight. For the term gpa,
add the weighted averages of full and mini assignments
"""


#output the results to the user in the format specified
print("\nWeighted grade points and the term grade point")


#output is right alligned using the maximum length of a string in that column (in this case being 26 characters)
#printed in tabular format as per output specifications
print("Full assignments:".rjust(26),"\t",full_a1,"\t",full_a2,"\t",full_a3,"\t",full_a4)
print("Mini assignments:".rjust(26),"\t",mini_A2,"\t",mini_A3a,"\t",mini_A3b,"\t",mini_A4a,"\t",mini_A4b,"\t",mini_A4c)
print("Weighted full assignments:\t",(format(w_f_a,".1f")))
print("Weighted mini-assignments:\t",(format(w_m_a,".1f")))
print("TermGPA:".rjust(26),"\t",(format(t_gpa,".1f")))






