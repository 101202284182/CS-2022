import csv
import random
import matplotlib.pyplot as plt

# TASK 1

# def calculate_monthly_repayment(net_salary, loan_amount, loan_term):
#     monthly_interest_rate = 0.02

#     monthly_repayment = loan_amount * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -loan_term)
    
#     return monthly_repayment

# with open('pg269/loan_results.csv', 'w', newline='') as csvfile:
#     csvwriter = csv.writer(csvfile)
    
#     csvwriter.writerow(['Loan Term', 'Monthly Repayment'])

#     scenarios = [
#         {'Net Salary': 2500, 'Loan Amount': 20000, 'Loan Term': i} for i in range(1, 7)
#     ]

#     for scenario in scenarios:
#         loan_term = scenario['Loan Term']
#         net_salary = scenario['Net Salary']
#         loan_amount = scenario['Loan Amount']
        
#         monthly_repayment = calculate_monthly_repayment(net_salary, loan_amount, loan_term)

#         csvwriter.writerow([loan_term, monthly_repayment])

#         plt.plot(loan_term, monthly_repayment, marker='o', label=f'Scenario: Net Salary={net_salary}, Loan Amount={loan_amount}')

# plt.xlabel('Loan Term (Months)')
# plt.ylabel('Monthly Repayment')
# plt.title('Loan Scenarios')

# plt.legend()

# plt.show()

# TASK 2

# def bmiCalc(height, weight):
#     if(weight <= 0 or height <= 0): return "error"
#     result = weight / (height ** 2)
#     if(type(weight) == float or type(weight) == int or type(height) == float or type(height) == int): return "your result is: %.2f" % result
#     return "error"

# print(bmiCalc(1.90, 80))

# TASK 3

# def bmiCalc(height, weight):
#     if(weight <= 0 or height <= 0): return "error"

#     result = {
#         "bmi": weight / (height ** 2),
#         "status": ""
#     }

#     if(result["bmi"] < 18.5):
#         result["status"] = "Underweight"
    
#     elif(result["bmi"] > 18.5 and result["bmi"] < 24.9):
#         result["status"] = "Normal"
    
#     elif(result["bmi"] > 25 and result["bmi"] < 29.9):
#         result["status"] = "Overweight"
    
#     elif(result["bmi"] >= 30):
#         result["status"] = "Obese"
    
#     if(type(weight) == float or type(weight) == int or type(height) == float or type(height) == int): return "Your BMI is: %.2f\nYour status is: \"%s\"" % (result["bmi"], result["status"])

#     return "error"

# print(bmiCalc(1.90, 90))

# TASK 5
# outcome = [] # 1 - win, 0 - lose

# def diceModel(diceInt, userInt):
#     if(diceInt == userInt):
#         outcome.append(1)

# for i in range(0, 600):
#     dice = random.randint(1, 6)
#     userGuess = 5
#     diceModel(dice, userGuess)

# plt.plot([0, 600], [0, len(outcome)])
# plt.show()

# TASK 6
outcome = [] # 1 - win, 0 - lose
xpoints = [0]

def diceModel(diceInt, userInt):
    if(diceInt == userInt):
        outcome.append(1)
    else:
        outcome.append(0)

for i in range(0, 600):
    dice = random.randint(1, 6)
    userGuess = 5
    diceModel(dice, userGuess)

for i in range(0, 599):
    xpoints.append(xpoints[i] + 1)

plt.plot(xpoints, outcome)
plt.show()