from sqlalchemy import func, desc, cast, Numeric, String
from config.model import Student, Teacher, Subject, Grade, Group
from seed import session

def select_1():
    return session.query(Student.fullname, func.round(cast(func.avg(Grade.grade), Numeric), 2).label('avg_grade'))\
    .join(Grade)\
    .group_by(Student.id)\
    .order_by(desc('avg_grade'))\
    .limit(5)\
    .all()

def select_2(subject_name):
    return session.query(Student.fullname, func.round(cast(func.avg(Grade.grade), Numeric), 2).label('avg_grade'))\
    .join(Grade)\
    .join(Grade.subject)\
    .filter(Subject.name == subject_name)\
    .group_by(Student.id)\
    .order_by(desc('avg_grade'))\
    .limit(1)\
    .all()

def select_3(subject_name):
    return session.query(Group.name, func.round(cast(func.avg(Grade.grade), Numeric), 2).label('avg_grade'))\
    .select_from(Group)\
    .join(Student)\
    .join(Grade)\
    .join(Subject)\
    .filter(Subject.name == subject_name)\
    .group_by(Group.id)\
    .all()

def select_4():
    return session.query(func.round(cast(func.avg(Grade.grade), Numeric), 2))\
    .scalar()

def select_5(teacher_name):
    return session.query(Subject.name)\
    .join(Teacher)\
    .filter(Teacher.fullname == teacher_name)\
    .all()

def select_6(group_name):
    return session.query(Student.fullname)\
    .join(Group)\
    .filter(Group.name == group_name)\
    .all()

def select_7(group_name, subject_name):
    return session.query(Student.fullname, Grade.grade, Grade.date)\
    .join(Grade, Grade.student_id == Student.id)\
    .join(Group,Student.group_id == Group.id)\
    .join(Subject, Grade.subject_id == Subject.id)\
    .filter(Group.name == group_name)\
    .filter(Subject.name == subject_name)\
    .all()
    
def select_8(teacher_name):
    grades = ( session.query(func.round(cast(func.round(Grade.grade), Numeric), 2).label('avg_grade'))\
    .join(Subject, Grade.subject_id == Subject.id)\
    .join(Teacher, Subject.teacher_id == Teacher.id)\
    .filter(Teacher.fullname == teacher_name)\
    .all() )

#counting avg grade
    if grades: 
        average_grade = round(sum(grade[0] for grade in grades) / len(grades), 2)
    else:
        average_grade = None #if no grades 
    return average_grade

def select_9(student_name): 
    return session.query(Subject.name)\
    .select_from(Grade)\
    .join(Subject, Grade.subject_id == Subject.id)\
    .join(Student, Grade.student_id == Student.id)\
    .filter(Student.fullname == student_name)\
    .group_by(Subject.name)\
    .all()

def select_10(student_name, teacher_name):
    return session.query(Subject.name)\
    .select_from(Grade)\
    .join(Subject, Grade.subject_id == Subject.id)\
    .join(Student, Grade.student_id == Student.id)\
    .join(Teacher, Subject.teacher_id == Teacher.id)\
    .filter(Student.fullname == student_name)\
    .filter(Teacher.fullname == teacher_name)\
    .group_by(Subject.name)\
    .all()

def select_ex_1(teacher_name, student_name):
    return session.query(Subject.name, func.round(cast(func.avg(Grade.grade), Numeric), 2).label('avg_grade'))\
    .join(Grade, Grade.subject_id == Subject.id)\
    .join(Student, Grade.student_id == Student.id)\
    .join(Teacher, Subject.teacher_id == Teacher.id)\
    .filter(Student.fullname == student_name, Teacher.fullname == teacher_name)\
    .group_by(Subject.name)\
    .all()

def select_ex_2(group_name, subject_name):
    last_lesson_date = (
        session.query(func.max(Grade.date))\
        .join(Student)\
        .join(Group)\
        .join(Subject)\
        .filter(Group.name == group_name, Subject.name == subject_name)\
        .scalar()
    )

    return (
        session.query(Student.fullname, Grade.grade, Grade.date)\
        .join(Grade)\
        .join(Group)\
        .join(Subject)\
        .filter(
            Group.name == group_name,
            Subject.name == subject_name,
            Grade.date == last_lesson_date
        )\
        .all()
    )