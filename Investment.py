balance = 0
invest = eval(input('How much will you invest monthly? '))
interest = ((eval(input('How much is the monthly interest? '))) / 100) + 1
opt = 'y'
while opt == 'y':
    for i in range(1, 13):
        balance += invest
        balance *= interest
    print('Balance of the investment after 1 year: R$ {0:.2f}'.format(balance))
    opt = input('Do you want to process another year? (y/n)')
