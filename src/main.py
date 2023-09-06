from src.utils import last_5_transactions

transactions = last_5_transactions()

def prints_last_5():
    for transaction in transactions:
        '''Выводит 5 последних по дате транзакций на экран, маскерует счет и карты'''
        date = transaction[0]
        description = transaction[1]
        from_ = transaction[2]
        to = transaction[3]
        masked_card_number = from_.replace(from_[14:-4], '******') #Маскировка карты
        masked_card_number_space = masked_card_number[:-12] + ' ' + masked_card_number[-12:-8] + ' ' + masked_card_number[-8:-4] + ' ' + masked_card_number[-4:]
        masked_account_number = to
        masked_account_number = f'**{masked_account_number[-4:]}' #Маскировка счета
        amount = transaction[4]['amount']
        currency_ = transaction[4]['currency']
        currency = currency_['name']


        print(f'{date[:10]} {description}\n{masked_card_number_space} -> Счет {masked_account_number}\n{amount} - {currency}')
        print()



prints_last_5()