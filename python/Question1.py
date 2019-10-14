

def question01(initialLevelOfDebt, interestPercentage, repaymentPercentage):
    # modify and then return the variable below
    import math
    deposit = initialLevelOfDebt* 10 * 0.01
    fixed_repay = repaymentPercentage * 0.01 * initialLevelOfDebt
    if(fixed_repay < 50):
        fixed_repay = 50
    initial = initialLevelOfDebt
    initial = round(initial,4)
    i = 1
    while( initial >= 50):
        debt_interest =  initial*(100+interestPercentage) * 0.01
        debt_repayment = debt_interest - fixed_repay
        initial = debt_repayment
        
        #print('Debt interests for round {} is {}, Resultant amount is {} and spending is {}'.format(i,debt_interest,debt_repayment,fixed_repay))
        i +=1

    total_payment = initial + deposit + (i-1)*fixed_repay
    result = int(round(total_payment,0))
    return result
