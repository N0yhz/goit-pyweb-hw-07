import random
from faker import Faker
from config.model import Base, Student, Group, Teacher, Subject, Grade
from datetime import datetime
from config.db_config import session

fake = Faker()

groups = [Group(name=f'Group{i}') for i in range (1,4)]
session.add_all(groups)
session.commit()

students = [Student(fullname=fake.name(), group=random.choice(groups)) for _ in range(42)]
session.add_all(students)
session.commit()

teachers = [Teacher(fullname=fake.name()) for _ in range(5)]
session.add_all(teachers)
session.commit()

subjects = [Subject(name=fake.word(), teacher=random.choice(teachers)) for _ in range(5)]
session.add_all(subjects)
session.commit()

for student in students:
    for subject in subjects:
        for _ in range(random.randint(5,20)):
            grade = Grade(student=student, subject=subject, grade=random.uniform(60,100), date=fake.date_between(start_date='-1y', end_date='today'))
            session.add(grade)
session.commit()