'''
Title     : operators
Subdomain : 30 days of code
Domain    : Python
Author    : Sai Ram Adidela
Created   : 18 April 2018
'''
if __name__ == "__main__":
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())
    tip = float(meal_cost*(tip_percent/100))
    # print("tip: ",tip)
    tax = float(meal_cost*(tax_percent/100))
    # print("tax: ",tax)
    
    totalCost = round(meal_cost+tip+tax)
    # print(totalCost)
    
    print('The total meal cost is %d dollars.'%totalCost)

