
# Eaxmaple code for creating function

def tax_calc():
    
    b_income = float (input('What is your annual income from business ??'))
    s_income = float (input('What is your annual income from salary ??'))
    o_income = float (input('What is your annual income from other sources ??'))
    total_income = b_income+s_income+o_income

    if s_income > (total_income * .75):
        if total_income >= 0 <= 600000:
            tax_amount = (0.0)
        if total_income >= 600001 <= 1200000:
            tax_amount = (total_income-600000)*.05
        if total_income >= 1200001 <= 1800000:
            tax_amount = (30000 + (total_income-1200000)*.10)
        if total_income >=1800001 <= 2500000:
            tax_amount = (90000 + (total_income-1800000)*.15)
        if total_income >= 2500001 <= 3500000:
            tax_amount = (195000 + (total_income-2500000)*.175)
        if total_income >= 3500001 <= 5000000:
            tax_amount = (370000 + (total_income-3500000)*.20)
        if total_income >= 5000001 <= 8000000:
            tax_amount = (670000 + (total_income-5000000)*.225)
        if total_income >= 8000001 <= 12000000:
            tax_amount = (1345000 + (total_income-8000000)*.25)
        if total_income >=12000001 <= 30000000:
            tax_amount = (2345000 + (total_income-12000000)*.275)
        if total_income >= 30000001 <= 50000000:
            tax_amount = (7295000 + (total_income-30000000)*.3)
        if total_income >= 50000001 <= 75000000:
            tax_amount = (13295000 + (total_income-50000000)*.325)
        if total_income > 75000000:
            tax_amount = (21420000 +(total_income-75000000)*.35)
        if tax_amount <= 0:
            print('Since your salary income is more than 75 percent of total income,' \
              ' so you shall be charged at salary tax rates.')
            print('You do not have to pay any tax for the year')
        else:
            print('Since your salary income is more than 75 percent of total income,' \
              ' so you shall be charged at salary tax rates.')
            print('You have to pay Rs. '+ str(tax_amount) +' as tax for the year .')
    if b_income >= (total_income*.25):
        if total_income >= 0 <= 400000:
            tax_amount = (0.0)
        if total_income >= 400001 <= 600000:
            tax_amount = ((total_income-400000)*.05)
        if total_income >= 600001 <= 1200000:
            tax_amount = (10000 +(total_income-600000)*.10)
        if total_income >= 1200001 <= 2400000:
            tax_amount = (70000 +(total_income-1200000)*.15)
        if total_income >= 2400001 <= 3000000:
            tax_amount = (250000 +(total_income-2400000)*.20)
        if total_income >= 3000001 <= 4000000:
            tax_amount = (370000 +(total_income-3000000)*.25)
        if total_income >= 4000001 <= 6000000:
            tax_amount = (620000 +(total_income-4000000)*.30)
        if total_income > 6000000:
            tax_amount = (1220000 +(total_income-6000000)*.35)
        if tax_amount <= 0.0:
            print('Since your business income is 25 percent or more of total income,' \
                ' so you shall be charged at business tax rates.')
            print('You do not have to pay any tax for the year.')
        else:
            print('Since your business income is 25 percent or more of total income,' \
                ' so you shall be charged at business tax rates.')
            print('You have to pay Rs. '+str(tax_amount)+ ' as tax for the year.')


