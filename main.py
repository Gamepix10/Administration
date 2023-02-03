import datetime
from models import *

# Core functional
with db:
    db.create_tables([CLIENTS, ORDERS])

print('DONE')


parametr = input()

if (parametr == 'init'):
    with db:
        db.create_tables([CLIENTS, ORDERS])

    print('DONE')


if (parametr == 'fill'):
    with db:
        clients = [
            {'name': 'Billy', 'city': 'London', 'address': 'WalkStreet 12'},
            {'name': 'Sergey', 'city': 'Surgut', 'address': 'Druzby 34'},
            {'name': 'Vadim', 'city': 'Moscow', 'address': 'Sokolniki 20'},
            {'name': 'Roman', 'city': 'Surgut', 'address': 'Mziskaya 1'},
            {'name': 'Anton', 'city': 'Boston', 'address': 'Franclin 45'},
            {'name': 'Andrey', 'city': 'Madrid', 'address': 'Lisabon 12'},
            {'name': 'Valeriy', 'city': 'Barcelona', 'address': 'Union 3'},
            {'name': 'Stan', 'city': 'California', 'address': 'Vashington 14'},
            {'name': 'Bran', 'city': 'Sanct-Peterburg', 'address': 'Lomonosova 67'},
            {'name': 'Aleksey', 'city': 'Nefteugansk', 'address': 'Dekabrisrov 15'}
        ]
        CLIENTS.insert_many(clients).execute()

    with db:
        clients = CLIENTS.select()
        orders = [
            {'client': clients[0], 'date': datetime.date(2022, 4, 14),
                'amount': 12000, 'description': 'What that!'},
            {'client': clients[1], 'date': datetime.date(2022, 5, 17),
                'amount': 13000, 'description': 'Who is who!'},
            {'client': clients[2], 'date': datetime.date(2022, 6, 12),
                'amount': 14000, 'description': 'Who there!'},
            {'client': clients[3], 'date': datetime.date(2022, 7, 18),
                'amount': 15000, 'description': 'I dont know!'},
            {'client': clients[4], 'date': datetime.date(2022, 8, 9),
                'amount': 16000, 'description': 'I also dont know!'},
            {'client': clients[5], 'date': datetime.date(2022, 9, 14),
                'amount': 2000, 'description': 'I make that!'},
            {'client': clients[6], 'date': datetime.date(2022, 4, 20),
                'amount': 5000, 'description': 'Please 5'},
            {'client': clients[7], 'date': datetime.date(2022, 11, 10),
                'amount': 34000, 'description': 'Great job'},
            {'client': clients[8], 'date': datetime.date(2023, 1, 1),
                'amount': 2000, 'description': 'Who is who!'},
            {'client': clients[9], 'date': datetime.date(2023, 2, 3),
                'amount': 3000, 'description': 'When!'}
        ]
        ORDERS.insert_many(orders).execute()

if (parametr == 'show[CLIENTS]'):
    all_clients = CLIENTS.select()
    for client in all_clients:
        print(client.id, '|', client.name, '|',
              client.city, '|', client.address)


if (parametr == 'show[ORDERS]'):
    all_orders = ORDERS.select()
    for order in all_orders:
        print(order.client, '|', order.date, '|',
              order.amount, '|', order.description)
