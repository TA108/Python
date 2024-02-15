while True:
    a = int(input('Enter account Number: '))
    b = input('Enter 4 digit number Pin: ')
    pin_no = ['1234', '2345', '4567', '4545', '6667']
    acc_money = 50232
    if b == '0':
        break
    if b in pin_no:
        print('Service available here are-'
              '\n 0) Exit'
              '\n 1) Cash withdrawal'
              '\n 2) Balance'
              '\n 3) Mini Statement'
              '\n 4) Cash Deposit'
              '\n 5) Pin Change Facility')
        sev_no = input('Enter the number with service you want: ')
        if sev_no == '0':
            break
        elif sev_no == '1':
            with_d = int(input('Enter withdrawal amount: '))
            if with_d > 10000:
                print('Withdrawal cancel: Withdrawal amount Exceeded')
            elif with_d < 10000:
                print('Withdrawal successful: Withdrawal of Rupees', with_d, 'Completed'
                      '\nBalance:', acc_money - with_d)
        elif sev_no == '2':
            print('Balance:', acc_money)
        elif sev_no == '3':
            print('Last Three Transaction:'
                  '\n 1) 5000'
                  '2) 2000'
                  '3) 300')
        elif sev_no == '4':
            dep = int(input('Enter the Cash Amount you want to deposit'))
            print('Put money in the outlet'
                  '\n PROCESSING..........'
                  '\n Deposit Complete'
                  '\n New Balance:', acc_money + dep)
        elif sev_no == 5:
            pin = input('Enter your pin:')
            if pin == pin_no:
                new_pin = input('Enter your new pin:')
                print('New Pin confirmed')
    else:
        print('Invalid PIN')
    '''
    Upgrades Required
    1) Invalid input print if the input is not numerical
    2) Mapping of Pin_ no with a list of acc_Money
    3) Find a Way to minimize use of elif 
    4) only Number allowed in pin
    '''
