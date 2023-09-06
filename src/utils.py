import json

def loads_list():
    '''Загружает список из файла в "data"
    '''
    with open('operations.json', 'r') as f:
        data = json.load(f)
    return data

def last_5_transactions():
    '''Добавляет в список - "transactions", данные со статусом -"EXECUTED"
    Сортерует по дате и возвращает 5 последних транзакций'''
    data = loads_list()
    transactions = []
    for transaction in data:
        if 'state' in transaction and transaction['state'] == 'EXECUTED':
            transactions.append([
                transaction['date'],
                transaction['description'],
                transaction['from'] if 'from' in transaction else '',
                transaction['to'],
                transaction['operationAmount']
            ])
    transactions.sort()
    return transactions[:5]