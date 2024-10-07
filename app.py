import argparse
from config.model import Teacher, Student, Group, Subject
from config.db_config import session

def create_teacher(name):
    teacher = Teacher(fullname=name)
    session.add(teacher)
    session.commit()
    print(f"Teacher '{name}' has been created.")

def list_teacher():
    teachers = session.query(Teacher).all()
    print("Teachers:")
    for teacher in teachers:
        print(f"{teacher.id}. {teacher.fullname}")

def update_teacher(teacher_id, name):
    teacher = session.query(Teacher).filter_by(id=teacher_id).first()
    if teacher:
        teacher.fullname = name
        session.commit()
        print(f"Teacher '{name}' has been updated.")
    else:
        print("Teacher not found.")

def remove_teacher(teacher_id):
    teacher = session.query(Teacher).filter_by(id=teacher_id).first()
    if teacher:
        session.delete(teacher)
        session.commit()
        print(f"Teacher with ID {teacher_id} has been removed.")
    else:
        print("Teacher not found.")

def main():
    parser = argparse.ArgumentParser(description="CLI for CRUD training")

    parser.add_argument("-a", "--action", choices=['create', 'list', 'update', 'remove'], required=True, help="Operations: create, list, update, remove")
    parser.add_argument("-m", "--model", choices=['Teacher','Student','Group','Subject'], required=True, help="Model for operations: Teacher, Student, Group")
    parser.add_argument("-n", "--name", type=str, required=True, help="Name for operation")
    parser.add_argument("-id", type=int, help="ID for updates")

    args = parser.parse_args()

    if args.model == 'Teacher':
        if args.action == 'create':
            if args.name:
                create_teacher(args.name)
            else:
                print('Please provide a name')
        elif args.action == 'list':
            list_teacher()
        elif args.action == 'update':
            if args.id and args.name:
                update_teacher(args.id, args.name)
            else:
                print('Please provide an ID and a name')
        elif args.action == 'remove':
            if args.id:
                remove_teacher(args.id)
            else:
                print('Please provide an ID')

if __name__ == "__main__":
    main()