import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')
parser.add_argument('--payment')


args = parser.parse_args()

zzz = 0
if args.type == 'diff':
    if args.payment != None:
        print('Incorrect parameters.')
    else:
        args.principal = int(args.principal)
        args.periods = int(args.periods)
        args.interest = float(args.interest)
        num_month = 1
        normal_interest_rate = args.interest / (12 * 100)
        for i in range(1, args.periods + 1):
            diff_payment = (args.principal / args.periods) + (normal_interest_rate * (args.principal - (args.principal * (num_month - 1) / args.periods)))
            zzz += math.ceil(diff_payment)
            print(f'Month {num_month}: payment is {math.ceil(diff_payment)}')
            num_month += 1
        print(f"Overpayment = {math.ceil(zzz - args.principal)}")
elif args.type == 'annuity':
    if args.periods == None:
        args.interest = float(args.interest)
        args.payment = int(args.payment)
        args.principal = int(args.principal)
        normal_interest_rate = args.interest / (12 * 100)
        number_of_month = math.log(args.payment / (args.payment - normal_interest_rate * args.principal),1 + normal_interest_rate)
        if number_of_month <= 11:
            print(f'It will take {number_of_month} months to repay this loan!')
        else:
            years = math.ceil(number_of_month) // 12
            month = math.ceil(number_of_month) % 12
            if month == 0:
                print(f'It will take {years} years to repay loan!')
                print(f'Overpayment = {math.ceil(args.payment * math.ceil(number_of_month) - args.principal)}')
            else:
                print(f'It will take {years} years and {month} months to repay this loan!')
                print(f'Overpayment = {math.ceil(args.payment * math.ceil(number_of_month) - args.principal)}')
    elif args.principal == None:
        args.interest = float(args.interest)
        args.payment = int(args.payment)
        args.periods = int(args.periods)
        normal_interest_rate = args.interest / (12 * 100)
        loan_principal = args.payment / ((normal_interest_rate * math.pow((1 + normal_interest_rate), args.periods)) / (math.pow((1 + normal_interest_rate), args.periods) - 1))
        print(f'Your loan principal = {math.floor(loan_principal)}!')
        print(f'Overpayment = {math.ceil(args.payment * args.periods - loan_principal)}')
    elif args.payment == None:
        args.periods = int(args.periods)
        args.interest = float(args.interest)
        args.principal = int(args.principal)
        normal_interest_rate = args.interest / (12 * 100)
        annuity_payment = args.principal * ((normal_interest_rate * math.pow((1 + normal_interest_rate), args.periods)) / (math.pow((1 + normal_interest_rate), args.periods) - 1))
        annuity_payment = math.ceil(annuity_payment)
        print(f'Your monthly payment = {math.ceil(annuity_payment)}!')
        print(f'Overpayment = {math.ceil(annuity_payment * args.periods - args.principal)}')