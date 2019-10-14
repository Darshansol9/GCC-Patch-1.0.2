# modify this function, and create other functions below as you wish
def question02(risk, bonus, trader):
    total_profit = 0
    for t in range(0,len(trader)):
        curr_profit = 0
        for r in range(0,len(risk)):
            if(trader[t] < risk[r]):
                continue
            else:
                if(curr_profit < bonus[r]):
                    curr_profit = bonus[r]
                    
        total_profit += curr_profit
                    
    # modify and then return the variable below
    
    return total_profit
