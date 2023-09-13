"""Este es el archivo donde se encuentra la información relacionada al ORM Peewee.
Se declaran las 3 variables a utilizar en la app: prenda, modelo y precio. 
Se utiliza la base de datos SqLite"""


from peewee import Model, SqliteDatabase, CharField, IntegerField

db = SqliteDatabase("baseleofds3.db")


class BaseDatos(Model):
    class Meta:
        database = db


class Venta(BaseDatos):
    prenda = CharField()
    modelo = CharField()
    precio = IntegerField()


db.connect()
db.create_tables([Venta])
