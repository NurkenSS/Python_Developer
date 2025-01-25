def is_valid_ogrnip(ogrnip):
    return len(ogrnip) == 15 and ogrnip.isdigit()

def is_valid_bank_account(bank_account):
    return len(bank_account) == 20 and bank_account.isdigit()
