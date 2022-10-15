
"""
acct_name
acct_balance
debt_balance
pin



{
    acct_no:{
        'acc_no': 019187171,
        'acc_name': user name,
        'debt_balance': 0,
        'acct_balance': 0,
        'pin': pin

    },
    acct_no:{
        'acc_no': 019187171,
        'acc_name': user name,
        'debt_balance': 0,
        'acct_balance': 0,
        'pin': pin

    },
    acct_no:{
        'acc_no': 019187171,
        'acc_name': user name,
        'debt_balance': 0,
        'acct_balance': 0,
        'pin': pin

    },
    
}

-- create bank account
-- check acct balance
-- transfer
-- get loan

"""

import random
import string
import pickle

# file = open("bankapp.txt", "wb")
# empty_dict = {}
# pickle.dump(empty_dict, file)
# file.close()

while True:
    print("Enter 1 to CREATE BANK ACCOUNT")
    print("Enter 2 to CHECK ACCOUNT BALANCE")
    print("Enter 3 to TRANSFER FUNDS")
    print("Enter 4 to GET LOAN")
    print("Enter ANYTHING ELSE to QUIT\n")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        file = open("bankapp.txt", "rb")
        data = file.read()
        database_dict = pickle.loads(data)
        full_name = input("Enter your full Name: ")
        pin = int(input("Enter your PIN: "))
        acct_no = random.sample(string.digits, 10)
        acct_no = "".join(acct_no)
        database_dict[acct_no] = {
            'acct_no': acct_no,
            'acct_name': full_name,
            'debt_balance': 0,
            'acct_balance': 5000,
            'pin': pin
        }
        print(database_dict)
        file = open("bankapp.txt", "wb")
        pickle.dump(database_dict, file)
        file.close()
    elif choice == 2:
        acct_no = input("Enter your account number: ")
        pin = int(input("Enter your account PIN: "))
        file = open("bankapp.txt", "rb")
        data = file.read()
        database_dict = pickle.loads(data)
        # print(database_dict)
        if database_dict.get(acct_no):
            db_pin = database_dict[acct_no]['pin']
            if pin == db_pin:
                acct_bal = database_dict[acct_no]['acct_balance']
                print(f"Your account balance is N{acct_bal}")
            else:
                print("Incorrect PIN")
        else:
            print("Account does not exist")
    elif choice == 3:
        acct_no = input("Enter your account number: ")
        rec_acct_no = input("Enter recievers acct no: ")
        pin = int(input("Enter your account PIN: "))
        amount = int(input("Enter amount N: "))
        file = open("bankapp.txt", "rb")
        data = file.read()
        database_dict = pickle.loads(data)
        sender_exists = database_dict.get(acct_no)
        reciever_exists = database_dict.get(rec_acct_no)
        if sender_exists != None and reciever_exists != None:
            if database_dict[acct_no]['acct_balance'] > amount:
                if database_dict[acct_no]['pin'] == pin:
                    database_dict[acct_no]['acct_balance'] -= amount
                    database_dict[rec_acct_no]['acct_balance'] += amount
                    print("transferring funds...")
                    print(f"transfer of {amount} successful")
                else:
                    print("Incorrect PIN")
            else:
                print("Insufficient Funds...")
        else:
            print("Incorrect account details")
        file.close()
        file = open("bankapp.txt", "wb")
        pickle.dump(database_dict, file)
        file.close()
    elif choice == 4:
        file = open("bankapp.txt", "rb")
        data = file.read()
        database_dict = pickle.loads(data)
        print(database_dict)
    else:
        break