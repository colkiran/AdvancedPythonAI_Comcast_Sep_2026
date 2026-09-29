"""
Requirement

Withdraw money from bank:
  a. balance in bank should not be less than 1000
  b. user account will be blocked for an hour of the user enters wrong pin for 3 times
"""

import time

class BalanceExceptionError(Exception):
    pass

class AttemptExceptionError(Exception):
    pass

attempts = 1
def withdraw():
    global attempts
    saved_pin = 1234
    balance = 10000
    pin = int(input("Enter the PIN :"))
    if pin == saved_pin:
        try:
            amt = float(input("Enter the amount to be withdrawn :"))
            temp_bal = balance - amt
            if temp_bal < 1000:
                raise BalanceExceptionError("Insufficient Balance......")
            balance = balance - amt
            print("Amount debited successfully.....")
            print(f"The balance amount in the account is :{balance}")
        except Exception as var:
            print(var)
    else:
        ans = input("Do you want to reenter the PIN (y/n):")
        if ans.lower() == "y":
            attempts += 1
            try:
                if attempts == 4:
                    raise AttemptExceptionError("Too many attempts, your account is blocked for an hour....")
            except Exception as var:
                print(var)
                time.sleep(3600)
            else:
                withdraw()
        else:
            print("Thank you...")
            return
withdraw()
