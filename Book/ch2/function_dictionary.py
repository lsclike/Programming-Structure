#implement a dictionary by using function
def dictionary():
    records = []
    def getitem(key):
        matches = [r for r in records if r[0] == key]
        if len(matches) == 1:
            key, value = matches[0]
            return value

    def setitem(key, value):
        nonlocal records
        non_match = [r for r in records if r[0] != key]
        records = non_match + [key, value]

    def dispatch(message, key=None, value=None):
        if message == 'getitem':
            return getitem(key)

        if message == 'setitem':
            setitem(key, value)

    return dispatch

def account(initial_balance):
    def deposite(amount):
        dispatch['balance'] += amount
        return dispatch['balance']

    def with_draw(amount):
        if amount > dispatch['balance']:
            return 'not sufficient fund'
        dispatch['balance'] -= amount
        return dispatch['balance']

    dispatch = {'deposite': deposite,
                'with_draw': with_draw,
                'balance': initial_balance}
    return dispatch

def with_draw(account, amount):
    return account['with_draw'](amount)

def deposite(account, amount):
    return account['deposite'](amount)

def check_balance(account):
    return account['balance']

if __name__ == '__main__':
    test_account = account(100)
    print(with_draw(test_account, 50))
    print(check_balance(test_account))