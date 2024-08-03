import random
import sqlite3
from faker import Faker
import hashlib

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

faker = Faker()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def generate_user_data():
    name = faker.name()
    phone_no = faker.phone_number()
    code = faker.random.randint(100000, 999999)
    email = faker.email()
    password = "password"  # You can use a more complex password if needed
    hashed_password = hash_password(password)
    return name, phone_no, code, email, hashed_password

def generate_contact_data(user_id=None):
    name = faker.name()
    phone_no = faker.phone_number()
    code = faker.random.randint(100000, 999999)
    is_spam = random.choice([True, False])
    is_registered = random.choice([True, False])
    email = faker.email() if random.random() < 0.5 else None
    return name, phone_no, code, is_spam, is_registered, user_id, email

for _ in range(10):
    name, phone_no, code, email, hashed_password = generate_user_data()
    cursor.execute("INSERT INTO User (name, phone_no, code, email, password) VALUES (?, ?, ?, ?, ?)", (name, phone_no, code, email, hashed_password))

for _ in range(20):
    name, phone_no, code, is_spam, is_registered, user_id, email = generate_contact_data(random.choice(range(1, 11)) if random.random() < 0.7 else None)
    cursor.execute("INSERT INTO Contacts (name, phone_no, code, is_spam, is_registered, user_id, email) VALUES (?, ?, ?, ?, ?, ?, ?)", (name, phone_no, code, is_spam, is_registered, user_id, email))

conn.commit()
conn.close()

print("Database populated with dummy data!")
