import numpy

def test():
    x=int(input("Enter number x: "))
    y=int(input("Enter number y:"))
    print("x**y =",x**y)
    print("log(x) =",numpy.log2(x))

def house():
    
    portion_down_payment=0.25
    current_savings=0
    invest_return=0.04
    annual_salary=float(input("Enter your annual salary: "))
    portion_saved=float(input("Enter the percent of your salary to save, as decimal: "))
    total_cost=float(input("Enter the cost of your dream home: "))
    semi_raise=float(input("Enter the semi-annual raise,as a decimal: "))

    down_pay=total_cost*portion_down_payment
    saving_per_month=(annual_salary*portion_saved)/12
    num_months=0
    while current_savings<down_pay:
        current_savings+=saving_per_month+(current_savings*invest_return)/12
        num_months+=1
        if num_months % 6 ==0:
            saving_per_month+=semi_raise*saving_per_month

    print("Number of months:",num_months)



def house2():
    
    portion_down_payment=0.25
    
    invest_return=0.04
    annual_salary=float(input("Enter starting salary: "))
    
    total_cost=1000000
    semi_raise=.07

    down_pay=total_cost*portion_down_payment
    num_months=36
    epsilon=100
    low=0.0
    high=1.0
    guess=(low+high)/2
    current_saving=(annual_salary*guess*3)
    current_saving+=6*0.7*current_saving
    current_saving+=3*0.4*current_saving
    print("Current saving before loop",current_saving)
    num_steps=0
    while abs(current_saving-down_pay) >= epsilon :
        print(current_saving,down_pay)
        #print(guess)
        print("Low is",low,"high is",high)
        num_steps+=1
        if current_saving > down_pay :
            high=guess
       
        else:
            low=guess

        guess=(low+high)/2


   
    if current_saving>=down_pay:

        print("Best savings rate:",guess)
        print("Steps in bisection search",num_steps)
    else:
        print("It is not possible to pay down payment in three years")

    
house2()




