#TESTING GIT BRANCH

import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
            for account in data:
                if isinstance(account.get('pin'),int):
                    account['pin'] = str(account['pin'])
            data.__update_details()
        else:
            print("no such file exists")
            data = []
    except Exception as err:
        print(f"an error occured as {err}")
        data = []

    @classmethod
    def __update_details(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(cls.data))


    @classmethod
    def __accountgenerate(cls):
        alphabet = random.choices(string.ascii_letters,k = 4)
        number = random.choices(string.digits,k = 4)
        spchr = random.choices("!@#$%^&*()_+",k = 2)
        id = alphabet + number + spchr
        random.shuffle(id)
        return "".join(id)

    @classmethod
    def __IFSC_code_generate(cls):
        alpha = random.choices(string.ascii_uppercase,k =4)
        digits = random.choices(string.digits,k = 7)
        IFSC_CODE = alpha + digits
        return "".join(IFSC_CODE)
    

    def create_account(self):
        user_data = {
            "name" : input("your name  --->").strip(),
            "age" : int(input("your age  --->").strip()),
            "email" : input("your email  --->").strip(),
            "address" : input("your address  --->").strip(),
            "IFSC_code" : Bank.__IFSC_code_generate(),
            "account_number" : Bank.__accountgenerate(),
            "pin" : input("pin code  --->").strip(),
            "balance" : 0
        }
        if user_data['age'] < 18 or not (user_data['pin'].isdigit() and len(user_data['pin']) == 4):
            print(f"sorry you can't create your account")
        else:
            print(f"account created successfully")

            for i in user_data:
                print(f"{i} : {user_data[i]}")
            print("please notedown your account number")
            Bank.data.append(user_data)
            Bank.__update_details()


        if user_data['age'] < 18 or not (user_data['pin'].isdigit() and len(user_data['pin']) == 4):
            print(f"sorry you can't create your account")
        else:
            print(f"account created successfully")

            for i in user_data:
                print(f"{i} : {user_data[i]}")
            print("please note down your account number")
            Bank.data.append(user_data)
            Bank.__update_details()

    

    
    def update_account(self):
        acc_num = input("account number  --->").strip()
        pin = input("pin code  --->").strip()
        IFSC_CODE = input("IFSC CODE  --->").strip()
        user_data = [i for i in Bank.data if i['account_number'] == acc_num and i['pin'] == pin and i['IFSC_code'] == IFSC_CODE]
        if not user_data:
            print("no such user found")
        else:
            print("age , account number , IFSC code and balance can't be updated")
            print("fill the given details to update or leave empty")
            new_data = {
                "name" : input("new name  --->").strip(),
                "email" : input("new email  --->").strip(),
                "address" : input("new address  --->").strip(),
                "pin" : input("new pin code  --->").strip()
            }
            if new_data['name'] == "":
                new_data['name'] = user_data[0]['name']
            if new_data['email'] == "":
                new_data['email'] = user_data[0]['email']
            if new_data['address'] == "":
                new_data['address'] = user_data[0]['address']
            if new_data['pin'] == "":
                new_data['pin'] = user_data[0]['pin']
            else:
                if not (new_data['pin'].isdigit() and len(new_data['pin']) == 4):
                    print("invalid new PIN must be 4 digits")
                    return

            new_data['age'] = user_data[0]['age']
            new_data['account_number'] = user_data[0]['account_number']
            new_data['IFSC_code'] = user_data[0]['IFSC_code']
            new_data['balance'] = user_data[0]['balance']

            for i in new_data:
                if new_data[i] == user_data[0][i]:
                    continue
                else:
                    user_data[0][i] = new_data[i]
            Bank.__update_details()
            print("details updated successfully")
    


    def show_details(self):
        acc_num = input("account number  --->").strip()
        pin = input("pin code  --->").strip()
        IFSC_CODE = input("IFSC CODE  --->").strip()
        user_data = [i for i in Bank.data if i['account_number'] == acc_num and i['pin'] == pin and i['IFSC_code'] == IFSC_CODE]

        print(f"your information are  :\n\n\n")
        
        if not user_data:
            print("invalid input")
        else:
            print(f"your information are  :\n\n\n")
        for i in user_data[0]:
            print(f"{i} : {user_data[0][i]}")
            
    
    
    def check_balance(self):
        acc_num = input("account number  --->").strip()
        pin = input("pin code  --->").strip()
        IFSC_CODE = input("IFSC CODE  --->").strip()
        user_data = [i for i in Bank.data if i['account_number'] == acc_num and i['pin'] == pin and i['IFSC_code'] == IFSC_CODE]
        if not user_data:
            print("invalid input")
        else:
            print(f"your current balance is {user_data[0]['balance']}")




    def deposit_money(self):
        acc_num = input("account number  --->").strip()
        pin = input("pin code  --->").strip()
        IFSC_CODE = input("IFSC CODE  --->").strip()
        user_data = [i for i in Bank.data if i['account_number'] == acc_num and i['pin'] == pin and i['IFSC_code'] == IFSC_CODE]
        if not user_data:
            print("invalid input")
        else:
            amount = int(input("how much you want to DEPOSIT  --->").strip())
            if amount > 10000000 or amount <= 0:
                print(f" you can't deposit such amount")
            else:
                user_data[0]['balance'] += amount
                Bank.__update_details()
                print(f"amount depositted successfully")



    def withdraw_money(self):
        acc_num = input("account number  --->").strip()
        pin = input("pin code  --->").strip()
        IFSC_CODE = input("IFSC CODE  --->").strip()
        user_data = [i for i in Bank.data if i['account_number'] == acc_num and i['pin'] == pin and i['IFSC_code'] == IFSC_CODE]
        if not user_data:
            print("invalid input")
        else:
            amount = int(input("how much you want to withdraw  --->").strip())
            if amount > 10000000000 or amount <= 0:
                print(f" you can't withdraw such amount")
            else:
                user_data[0]['balance'] -= amount
                Bank.__update_details()
                print(f"amount withdrawn successfully")


    def transfer_money(self):
        print("user 1 details \n")

        acc_num = input("account number  --->").strip()
        pin = input("pin code  --->").strip()
        IFSC_CODE = input("IFSC CODE  --->").strip()

        print("user 2 details \n")

        acc_num2 = input("account number  --->").strip()
        pin2 = input("pin code  --->").strip()
        IFSC_CODE2 = input("IFSC CODE  --->").strip()


        user_data = [i for i in Bank.data if i['account_number'] == acc_num and i['pin'] == pin and i['IFSC_code'] == IFSC_CODE]
        user_data2 = [i for i in Bank.data if i['account_number'] == acc_num2 and i['pin'] == pin2 and i['IFSC_code'] == IFSC_CODE2]

        if not user_data or not user_data2:
            print("invalid input")

        else:
            amount = int(input("how much you want to transfer  --->").strip())
            if amount > 10000000000 or amount <= 0:
                print(f" you can't transfer such amount")
            elif amount > user_data[0]['balance']:
                    print("insufficient balance")
            else:
                user_data[0]['balance'] -= amount
                user_data2[0]['balance'] += amount
                Bank.__update_details()
                print(f"amount transferred successfully")
   


    def delete_account(self):
        acc_num = input("account number  --->").strip()
        pin = input("pin code  --->").strip()
        IFSC_CODE = input("IFSC CODE  --->").strip()
        user_data = [i for i in Bank.data if i['account_number'] == acc_num and i['pin'] == pin and i['IFSC_code'] == IFSC_CODE]
        if not user_data:
            print("invalid input")
        else:
            delete_account = input("type (y) if you actually want to delete your account and type (n) if you don't want to delete your account  --->").strip()
            if delete_account.lower() == "n":
                print("bypassed")
            else:
                index = Bank.data.index(user_data[0])
                Bank.data.pop(index)
                print("account deleted successfully")
                Bank.__update_details()
    


try:
    while True:
        user_choice = input("\nDO YOU WANT TO CONTINUE ? (enter/exit): ").strip()
        if user_choice == "exit":
            print("THANK YOU FOR USING OUR SERVICES")
            break
        elif user_choice == "enter":
            print("\nWELCOME TO THE BANK")

            user_input = Bank()
            print(f"press 1 for creating an acccount")
            print(f"press 2 for updating an acccount")
            print(f"press 3 for viewing details of your acccount")
            print(f"press 4 for checking balance in your acccount")
            print(f"press 5 for depositing money to your acccount")
            print(f"press 6 for withdrawing money to your acccount")
            print(f"press 7 for transferring money to an acccount")
            print(f"press 8 for deleting acccount")
            
            try:
                check = int(input("enter your choice  --->").strip())
            except ValueError:
                print("invalid input - please enter a number")
                continue
            if check == 1:
                user_input.create_account()

            elif check == 2:
                user_input.update_account()

            elif check == 3:
                user_input.show_details()

            elif check == 4:
                user_input.check_balance()

            elif check == 5:
                user_input.deposit_money()

            elif check == 6:
                user_input.withdraw_money()

            elif check == 7:
                user_input.transfer_money()

            elif check == 8:
                user_input.delete_account()
            else:
                print("Invalid choice!")
    else:
        print("Please type 'enter' or 'exit'")

except Exception as err:
    print(f"an error occured as {err}")