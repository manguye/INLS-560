# Desirable: Easy mortgage lending qualifications.
MIN_CREDIT_SCORE = 750
MIN_SALARY = 22000

# Prospective loanee inputs information.
user_credit_score = int(input('Enter your credit score: '))
user_salary = int(input('Enter your salary, rounded to the nearest dollar: '))

if user_credit_score >= MIN_CREDIT_SCORE and user_salary >= MIN_SALARY:
    print('You are eligible for an easy mortgage loan.')
else:
# Multi-line with f-string.
    print(f'''
    You are ineligible for an easy mortgage loan. You must meet these criteria.
    The minimum credit score required is {MIN_CREDIT_SCORE}.
    The minimum salary required is {MIN_SALARY}.
    Please speak with a representative if you'd like to open a standard loan.
    ''')