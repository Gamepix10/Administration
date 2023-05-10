from models import *
import pytest


def test_db_data():
    with db:
        db.create_tables([CLIENTS, ORDERS])

    print('DONE')


def test_db_info_clients():
    all_clients = CLIENTS.select()
    for client in all_clients:
        if (client.name != ' ') and (client.city != ' ') and (client.address != ' '):
            print("Succesfull")
        else:
            print("Error!")


def test_db_info_orders():
    all_orders = ORDERS.select()
    for order in all_orders:
        if (order.client != ' ') and (order.date != ' ') and (order.amount != ' ') and (order.description != ' '):
            print("Succesfull")
        else:
            print("Error!")


def test_db_count_clients():
    all_clients = CLIENTS.select()
    if (len(all_clients) < 10):
        print("Little data")
    else:
        print("Succesfull")


def test_db_count_clients():
    all_orders = ORDERS.select()
    if (len(all_orders) < 10):
        print("Little data")
    else:
        print("Succesfull")
