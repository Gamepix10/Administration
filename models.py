from peewee import *


db = SqliteDatabase('db/database.db')


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'


class CLIENTS(BaseModel):
    name = CharField()
    city = CharField()
    address = CharField()

    class Meta:
        db_table = 'clients'


class ORDERS(BaseModel):
    client = ForeignKeyField(CLIENTS)
    date = DateField()
    amount = FloatField()
    description = CharField()

    class Meta:
        db_table = 'orders'
