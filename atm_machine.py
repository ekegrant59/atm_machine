
bal = 20000
pin = 1234
withdrawned = 0

def begin():  
    a = int(input(" --WHAT WOULD YOU LIKE TO DO-- \n 1. WITHDRAW \n 2. VIEW BALANCE \n 3. TRANSFER \n ENTER : "))
    
    if a == 1:
        withdraw()
    elif a == 2:
        balance()
    elif a == 3:
        print('THIS OPTION IS CURRENTLY UNAVAILABLE')
        another()
    else:
        print('PLEASE ENTER A VALID OPTION')
        begin()
    
def balance():
    p = int(input('PLEASE INPUT YOUR PIN : '))
    if p == pin :
        print( 'YOUR BALANCE IS $',bal-withdrawned)
        another()
    else :
        print('INVALID PIN, PLEASE TRY AGAIN')
        balance()

def withdraw():
    p = int(input('PLEASE INPUT YOUR PIN : '))
    if p == pin :
        w = int(input('HOW MUCH WOULD YOU LIKE TO WITHDRAW : '))
        if w < bal:
            global withdrawned
            withdrawned = w
            print('YOUR WITHDRAWAL WAS SUCCESSFUL \n PLEASE COLLECT YOUR CASH')
            another()
        else:
            print('YOU HAVE INSUFICIENT FUNDS')
            another()
    else :
        print('INVALID PIN, PLEASE TRY AGAIN')
        withdraw()
        
def another():
    an = input('DO YOU WANT TO PERFORM ANOTHER TRANSACTION : ')
    if an == 'yes' or an == 'YES' or an == 'Yes' :
        begin()
    else:
        print('THANK YOU FOR BANKING WITH US')
    
begin()
    
