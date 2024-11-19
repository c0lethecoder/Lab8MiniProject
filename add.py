from app import db, app, Account, Courses, Grades

with app.app_context():
    db.session.query(Grades).delete()  # Deletes all records from the Grades table
    db.session.query(Courses).delete()  # Deletes all records from the Courses table
    db.session.query(Account).delete()  # Deletes all records from the Account table
    db.session.commit()  # Commit to save changes

# Accounts
stud1 = Account(username="stud1", password="stud1", name="Henry Arinze", is_teacher=False, is_admin=False)
stud2 = Account(username="stud2", password="stud2", name="Cole Harris", is_teacher=False, is_admin=False)
stud3 = Account(username="stud3", password="stud3", name="Rohit Vedulla", is_teacher=False, is_admin=False)
stud4 = Account(username="stud4", password="stud4", name="Sophia Huang", is_teacher=False, is_admin=False)
stud5 = Account(username="stud5", password="stud5", name="Olivia Brooks", is_teacher=False, is_admin=False)
stud6 = Account(username="stud6", password="stud6", name="Lucas Reed", is_teacher=False, is_admin=False)
stud7 = Account(username="stud7", password="stud7", name="Arjun Mehta", is_teacher=False, is_admin=False)
stud8 = Account(username="stud8", password="stud8", name="Chen Wei", is_teacher=False, is_admin=False)

teach1 = Account(username="teach1", password="teach1", name="Margaret Harper", is_teacher=True, is_admin=False)
teach2 = Account(username="teach2", password="teach2", name="Benjamin Carter", is_teacher=True, is_admin=False)
teach3 = Account(username="teach3", password="teach3", name="Ammon Hepworth", is_teacher=True, is_admin=False)

admin = Account(username="admin", password="admin", name="admin", is_teacher=False, is_admin=True)

# Add accounts to database
db.session.add_all([stud1, stud2, stud3, stud4, stud5, stud6, stud7, stud8, teach1, teach2, teach3, admin])
db.session.commit()  # Commit accounts first so they can be queried

# Query teacher IDs
teach1_id = Account.query.filter_by(username="teach1").first().id
teach2_id = Account.query.filter_by(username="teach2").first().id
teach3_id = Account.query.filter_by(username="teach3").first().id

# Courses
course1 = Courses(name="Math 141",
                  time="MW 9:00-10:50 AM",
                  currentEnrollment=4,
                  maxEnrollment=10,
                  instructor_id=teach1_id)

course2 = Courses(name="Physics 11",
                  time="MWF 1:00-2:15 PM",
                  currentEnrollment=5,
                  maxEnrollment=10,
                  instructor_id=teach2_id)

course3 = Courses(name="CSE 165",
                  time="TR 2:00-2:50 PM",
                  currentEnrollment=4,
                  maxEnrollment=10,
                  instructor_id=teach3_id)

course4 = Courses(name="CSE 155",
                  time="TR 4:00-5:45 PM",
                  currentEnrollment=5,
                  maxEnrollment=5,
                  instructor_id=teach3_id)

# Add courses to database
db.session.add_all([course1, course2, course3, course4])
db.session.commit()

# Query student IDs
henry_id = Account.query.filter_by(name="Henry Arinze").first().id
cole_id = Account.query.filter_by(name="Cole Harris").first().id
rohit_id = Account.query.filter_by(name="Rohit Vedulla").first().id
sophia_id = Account.query.filter_by(name="Sophia Huang").first().id
olivia_id = Account.query.filter_by(name="Olivia Brooks").first().id
lucas_id = Account.query.filter_by(name="Lucas Reed").first().id
arjun_id = Account.query.filter_by(name="Arjun Mehta").first().id
chen_id = Account.query.filter_by(name="Chen Wei").first().id

# Query course IDs
math_id = Courses.query.filter_by(name="Math 141").first().id
physics_id = Courses.query.filter_by(name="Physics 11").first().id
cs165_id = Courses.query.filter_by(name="CSE 165").first().id
cs155_id = Courses.query.filter_by(name="CSE 155").first().id

# Grades
grades = [
    Grades(student_id=henry_id, class_id=math_id, grade=92),
    Grades(student_id=cole_id, class_id=math_id, grade=65),
    Grades(student_id=rohit_id, class_id=math_id, grade=86),
    Grades(student_id=sophia_id, class_id=math_id, grade=77),

    Grades(student_id=olivia_id, class_id=physics_id, grade=53),
    Grades(student_id=sophia_id, class_id=physics_id, grade=85),
    Grades(student_id=lucas_id, class_id=physics_id, grade=94),
    Grades(student_id=rohit_id, class_id=physics_id, grade=91),
    Grades(student_id=cole_id, class_id=physics_id, grade=88),

    Grades(student_id=arjun_id, class_id=cs165_id, grade=93),
    Grades(student_id=chen_id, class_id=cs165_id, grade=85),
    Grades(student_id=olivia_id, class_id=cs165_id, grade=57),
    Grades(student_id=lucas_id, class_id=cs165_id, grade=68),

    Grades(student_id=arjun_id, class_id=cs155_id, grade=99),
    Grades(student_id=olivia_id, class_id=cs155_id, grade=87),
    Grades(student_id=chen_id, class_id=cs155_id, grade=92),
    Grades(student_id=rohit_id, class_id=cs155_id, grade=67),
    Grades(student_id=cole_id, class_id=cs155_id, grade=75)
]


# Add grades to database
db.session.add_all(grades)
db.session.commit()

print("Sample data added successfully!")
