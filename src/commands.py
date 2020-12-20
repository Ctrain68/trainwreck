from main import db
from flask import Blueprint

db_commands = Blueprint("db-custom", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")
    print("Tables deleted")

@db_commands.cli.command("seed")
def seed_db():
    from models.User import User
    from models.Profile import Profile
    from faker import Faker
    from main import bcrypt
    from models.Equipment import Equipment
    from models.EquipmentOrder import EquipmentOrder
    import random
    from random import seed
    from random import randint

    faker = Faker()
    profiles = []
    equipments = []

    categories = ["dumbells", "cardio", "machine", "yoga", "mobility"]
    

    for i in range(10):
        user = User()
        user.email = f"test{i}@test.com"
        user.password = bcrypt.generate_password_hash("123456").decode("utf-8")
        db.session.add(user)
        
    db.session.commit()

    for i in range(10):
        profile = Profile()
        profile.username = faker.name()
        profile.fname = faker.first_name()
        profile.lname = faker.last_name()
        profile.account_active=faker.boolean()
        profile.user_id = i+1
        profiles.append(profile)
        db.session.add(profile)

    db.session.commit()

    for i in range(30):
        equipment = Equipment()
        equipment.equipment_name = faker.name()
        equipment.equipment_description = faker.catch_phrase()
        equipment.rented = random.choice([True, False])
        equipment.rentpw= randint(8, 120)
        equipment.owner_id = random.choice(profiles).profileid
        equipment.category = random.choice(categories)
        equipments.append(equipment)
        db.session.add(equipment)
 
    for i in range(30):
        equipment_order = EquipmentOrder()
        equipment_order.order_begin_date = faker.date_between(start_date='-1y', end_date='today')
        equipment_order.order_return_date_estimate = faker.date_between(start_date='today', end_date='+1y')
        equipment_order.order_actual_return_date = faker.date_between(start_date='today', end_date='+1y')
        equipment_order.order_active= random.choice([True, False])
        equipment_order.equipment_id = randint(1, 29)
        # equipment_order.equipment_id = random.choice(equipments).id
        equipment_order.hirer_id = random.choice(profiles).profileid
        db.session.add(equipment_order)

    db.session.commit()
    print("Tables seeded")