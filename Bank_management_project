import json
import random
import string
from pathlib import Path

try:
    while True:
        user_input = input("do you want to continue ? (enter/exit) : ")

        if user_input == "exit":
            print("thank you for using our services")
            break

        elif user_input == "enter":
            print("welcome to the bank")

        class Bank:
            database = 'data.json'
            data = []
            try:
                if Path(database).exists():
                    with open(database) as fs:
                        data = json.loads(fs.read())
                else:
                    print("no such file exists")

            except Exception as err:
                print(f"an error occured as {err}")

            @classmethod
            def __update_details(cls):
                    with open(cls.database, 'w') as ss:
                        ss.write(json.dumps(Bank.data))


            @classmethod
            def __accountgenerate(cls):
                alphabet = random.choices(string.ascii_letters,k = 3)
                number = random.choices(string.digits,k = 3)
                spchr = random.choices("!@#$%^&*()_+",k = 1)
                id = alphabet + number + spchr
                random.shuffle(id)
                return "".join(id)


            


            def create_account(self):
                info = {

                    'name': input("enter your name : "),
                    'age': int(input("entere your age : ")),
                    'email': input("enter your email : "),
                    'pin': int(input("enter your pin : ")),
                    'accountnumber': Bank.__accountgenerate(),
                    'balance': 0
                    
                }
                if info['age'] < 18 or len(str(info['pin'])) != 4:
                    print("sorry , you are not eligible to create an account")
                else:
                    print("account created successfully")
                    for i in info:
                        print(f"{i} : {info[i]}")
                    print("please note down your account number")
                    Bank.data.append(info)
                    
                    Bank.__update_details()

            
            def deposit(self):
                    account_number = input("please enter your account number : ")
                    pin_code = int(input("please enter your pin code : "))
                    userdata = [i for i in Bank.data if i['accountnumber'] == account_number and i['pin'] == pin_code]
                    if not userdata:
                        print("invalid account number or pin code")
                    else:
                        amount = int(input("how much you want to deposit: "))
                        if amount > 10000000 or amount <= 0:
                            print("sorry ,you can't deposit more than 1 crore and <= 0 in a single transaction")
                        else:
            
                            userdata[0]['balance'] += amount
                            Bank.__update_details()
                            print(f"you have deposited {amount} successfully and your current balance is {userdata[0]['balance']}")
                
            
            
            
            def withdraw(self):
                account_number = input("please enter your account number : ")
                pin_code = int(input("please enter your pin code : "))
                userdata = [i for i in Bank.data if i['accountnumber'] == account_number and i['pin'] == pin_code]
                if not userdata:
                    print("invalid account number or pin code")
                else:
                    amount = int(input("how much you want to withdraw: "))
                    if amount > 10000000 or amount <= 0:
                        print("sorry ,you can't withdraw more than 1 crore and <= 0 in a single transaction")
                    elif amount > userdata[0]['balance']:
                        print(f"sorry ,you can't withdraw more than your current balance {userdata[0]['balance']}")
                    else:
                        userdata[0]['balance'] -= amount
                        Bank.__update_details()
                        print(f"you have withdrawn {amount} successfully and your current balance is {userdata[0]['balance']}")



            def details(self):
                account_number = input("please enter your account number : ")
                pin_code = int(input("please enter your pin code : "))
                userdata = [i for i in Bank.data if i['accountnumber'] == account_number and i['pin'] == pin_code]
                print("your information are \n\n\n\n")
                for i in userdata[0]:
                    print(f"{i} : {userdata[0][i]}")

            def updatedetails(self):
                account_number = input("please enter your account number : ")
                pin_code = int(input("please enter your pin code : "))
                userdata = [i for i in Bank.data if i['accountnumber'] == account_number and i['pin'] == pin_code]
                if not userdata:
                    print("invalid account number or pin code")
                else:
                    print("you can't the age , account number ,and balance , you can only update your name , email and pin code")
                    print("fill the details you want to update and if you don't want to update any field then just press enter")
                    newdata = {

                        'name': input("enter your name : ") or userdata[0]['name'],
                        'email': input("enter your email : ") or userdata[0]['email'],
                        'pin': int(input("enter your pin : ") or userdata[0]['pin']),
                    }
                    if newdata["name"] == "":
                        newdata["name"] = userdata[0]['name']
                    if newdata["email"] == "":
                        newdata["email"] = userdata[0]['email']
                    if newdata["pin"] == "":
                        newdata["pin"] = userdata[0]['pin']
                    newdata["age"] = userdata[0]['age']
                    newdata["accountnumber"] = userdata[0]['accountnumber']
                    newdata["balance"] = userdata[0]['balance']

                    if type(newdata['pin']) == str:
                        newdata['pin'] = int(userdata[0]['pin'])

                    for i in newdata:
                        if newdata[i] == userdata[0][i]:
                            continue
                        else:
                            userdata[0][i] = newdata[i]
                    Bank.__update_details()
                    print("details updated successfully")
            
            def check_balance(self):
                account_number = input("please enter your account number : ")
                pin_code = int(input("please enter your pin code : "))
                userdata = [i for i in Bank.data if i['accountnumber'] == account_number and i['pin'] == pin_code]
                if not userdata:
                    print("invalid account number or pin code")
                else:
                    print(f"your current balance is {userdata[0]['balance']}")
            def delete_account(self):
                account_number = input("please enter your account number : ")
                pin_code = int(input("please enter your pin code : "))
                userdata = [i for i in Bank.data if i['accountnumber'] == account_number and i['pin'] == pin_code]
                if not userdata:
                    print("invalid account number or pin code")
                else:
                    check = input("are you sure you want to delete your account ? (y/n) : ")
                    if check == "y":
                        Bank.data.remove(userdata[0])
                        Bank.__update_details()
                        print("your account has been deleted successfully")
                    else:
                        print("account deletion cancelled")

        user = Bank()
        print("press 1 for creating an account")
        print("press 2 for withdrawing money")
        print("press 3 for depositing money")
        print("press 4 for details")
        print("press 5 for updating the details")
        print("press 6 for checking the balance")
        print("press 7 for deleting an account")

        check = input("enter your choice : ")
        if check == "1":
            user.create_account()
        elif check == "2":
            user.withdraw()
        elif check == "3":
            user.deposit()
        elif check == "4":
            user.details()
        elif check == "5":
            user.updatedetails()
        elif check == "6":
            user.check_balance()
        elif check == "7":
            user.delete_account()
except Exception as err:
    print(f"an error occured as {err}")