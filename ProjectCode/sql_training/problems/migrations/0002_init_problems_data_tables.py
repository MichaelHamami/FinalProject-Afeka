# Generated by Django 3.0.11 on 2021-02-02 23:21

from django.db import migrations
from enum import Enum


class ClothingItem(Enum):
    SHIRTS = 'Shirts'
    PANTS = 'Pants'
    TROUSERS = 'Trousers'
    SHOES = 'Shoes'
    SUITS = 'Suits'

    def get_values():
        return [ClothingItem.SHIRTS.value, ClothingItem.PANTS.value, ClothingItem.TROUSERS.value,
                ClothingItem.SHOES.value, ClothingItem.SUITS.value]


def _init_employee_database(apps, schema_editor):
    Employee = apps.get_model("problems", "Employee")
    employees = [
        Employee(1, "Ariel", "Vainshtein", 26),
        Employee(2, "Joshua", "Graham", 30),
        Employee(3, "Abraham", "Yalkovitch", 28),

    ]
    for data in employees:
        data.save(using="problems_db")


def _init_clothing_store_db(apps, schema_editor):
    ClothingStore = apps.get_model("problems", "ClothingStore")
    items = [
        ClothingStore(803654786, ClothingItem.SHOES.value, "Nike", 25.23),
        ClothingStore(987124123, ClothingItem.SHIRTS.value, "H&O", 22.10),
        ClothingStore(300125487, ClothingItem.PANTS.value, "Diadora", 33.99),
        ClothingStore(159845362, ClothingItem.SUITS.value, "Diadora", 99.99),
    ]
    for data in items:
        data.save(using="problems_db")


def _init_vehicle_db(apps, schema_editor):
    Vehicle = apps.get_model("problems", "Vehicle")
    items = [
        Vehicle('111-22-333', 4, 'Toyota', 5999.99, 10564.23, True),
        Vehicle('165-81-713', 4, 'BMW', 6599.99, 9846.89, False),
        Vehicle('148-879-003', 0, 'Lamborghini', 10999.99, 11003.89, False),
        Vehicle('846-57-446', 2, 'Toyota', 7259.99, 8523.73, True),
        Vehicle('087-918-224', 1, 'Honda', 8250.00, 7999.89, True),
    ]
    for data in items:
        data.save(using="problems_db")


def _init_secret_db(apps, schema_editor):
    BlindSecret = apps.get_model("problems", "BlindSecret")
    item = BlindSecret(1, 'Bingo')
    item.save(using="problems_db")


def _init_safe_db(apps, schema_editor):
    Safe = apps.get_model("problems", "Safe")
    prize_amount = 10000000
    safe = Safe(1, '4-8-15-23-48', prize_amount)
    safe.save(using="problems_db")


# def _init_mockup_user_db(user):
#     items = [
#         User(user.id + 1, 'yxilith', 'notsu@gmail.com', '901a706ec09c2466e450e5ccda37c5', UserRole.ADMIN.value),
#         User(user.id, user.username, user.email, user.password, UserRole.USER.value)
#     ]
#     for item in items:
#         item.save(using="problems_db")
def init_problems_tables(apps, schema_editor):
    _init_employee_database(apps, schema_editor)
    _init_clothing_store_db(apps, schema_editor)
    _init_vehicle_db(apps, schema_editor)
    _init_secret_db(apps, schema_editor)
    _init_safe_db(apps, schema_editor)
    # _init_mockup_user_db(apps)


class Migration(migrations.Migration):
    dependencies = [("problems", "0001_initial")
                    ]

    operations = [
        migrations.RunPython(init_problems_tables),
    ]
