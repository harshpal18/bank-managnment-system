from login_register import login, register
import basic_features as bf
import time

def home(acc_no):
    print("\n" + "." * 50)
    print(":                  BANK SYSTEM                   :")
    print("." * 50)
    print(": 1. Check Balance                               :")
    print(": 2. Withdraw                                    :")
    print(": 3. Deposit                                     :")
    print(": 4. Transfer Funds                              :")
    print(": 5. View Transaction History                    :")
    print(": 6. Loan Eligibility                            :")
    print(": 7. Report Wrongful Transaction                 :")
    print(": 8. Update Account Details                      :")
    print(": 9. KYC Status                                  :")
    print(": 10. Logout                                     :")
    print("." * 50)
    n = int(input("Enter choice (1-10): ").strip())

    if n == 1:
        bal = bf.check_balance(acc_no)
        print(f"Balance: {bal}")
    elif n == 2:
        bf.withdraw(acc_no, float(input("Enter amount to withdraw: ").strip()))
        print("Withdrawal successful.")
    elif n == 3:
        bf.deposit(acc_no, float(input("Enter amount to deposit: ").strip()))
        print("Deposit successful.")
    elif n == 4:
        bf.transfer_funds(acc_no)
        print("Transfer completed.")
    elif n == 5:
        history = bf.view_transaction_history(acc_no)
        for record in history:
            print(record)
    elif n == 6:
        eligibility = bf.check_loan_eligibility(acc_no)
        print(eligibility)
    elif n == 7:
        transaction_id = int(input("Enter Transaction ID to report: ").strip())
        reason = input("Enter reason for reporting: ").strip()
        report = bf.report_wrongful_transaction(acc_no, transaction_id, reason)
        if report: 
            print("Transaction reported successfully.")
        else:
            print("Failed to report transaction.") 
    elif n == 8:
        print("Feature not implemented yet.")
    elif n == 9:
        status = bf.check_kyc_status(acc_no)
        if status:
            print("KYC is completed for this account.")
        else:
            print("KYC is not completed for this account.")
    elif n == 10:
        print("Logging out...")
        control_menu(acc_no)
        return
    else:
        print("Invalid choice")

    control_menu(acc_no)


def control_menu(acc_no):
    print("\n" + "." * 50)
    print(":                  BANK SYSTEM                   :")
    print("." * 50)
    print(": 1. Go Back                                     :")
    print(": 2. Exit                                        :")
    print("." * 50)
    n = int(input("Enter choice (1-2): ").strip())
    if n == 1:
        home(acc_no)
    else:
        print("Exiting... Goodbye!")
        time.sleep(2)
        exit()


def start_menu():
    print("\n" + "." * 50)
    print(":                  BANK SYSTEM                   :")
    print("." * 50)
    print(": 1. Create Account                              :")
    print(": 2. Login                                       :")
    print("." * 50)
    n = int(input("Enter choice (1-2): ").strip())
    if n == 1:
        acc_no = register()
        time.sleep(1)
        if acc_no is not None:
            home(acc_no)
    else:
        acc_no = login()
        time.sleep(1)
        if acc_no is not None:
            home(acc_no)


if __name__ == "__main__":
    start_menu()