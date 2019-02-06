def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return "Insufficient fund"
        else:
            balance = balance - amount
        return balance
    return withdraw

if __name__ == '__main__':
    new_withdraw = make_withdraw(100)
    print(new_withdraw(25))
    print(new_withdraw(25))