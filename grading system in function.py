from datetime import date
def initial_output():
    display = ('''       SUNWAY INTERNATIONAL GRADING SYSTEM
           MAITIDEVI, KATHMANDU''')
    print(display)


def talking_input():
    StudentName = input("Enter the name of student : ")
    StudentAddress = input("Enter the address of student")
    StudentFaculty = input("Enter the faculty of the student")
    StudentProgram = input("Enter the program of student")
    StudentIntake = input("Enter the intake date of student")
    Applied_Programming, Mobile_programming, Enterprenuership, Communication, DOS = input(
            "Enter the obtained marks").split(
            ",")
    P: float = ((int(Applied_Programming) + int(Mobile_programming) + int(Enterprenuership) + int(Communication) + int(
            DOS)) / 500) * \
                   100
    return StudentIntake,StudentProgram,StudentFaculty,StudentName,StudentAddress;


def calculation(P):
    P: float
    g = float
    if P >= 90:
        g = 'A+'
    elif 90 > P >= 80:
        g = 'A'
    elif 80 > P >= 70:
        g = 'B+'
    elif 70 > P >= 60:
        g = 'B-'
    elif 60 > P >= 50:
        g = 'B'
    elif 50 > P >= 40:
        g = 'C+'
    elif 40 > P >= 30:
        g = 'D'
    elif P < 30:
        g = 'F'
        return g

initial_output()
print("/t Date", date.today())
StudentIntake, StudentProgram, StudentFaculty, StudentName, StudentAddress = talking_input()
print("Name : ", StudentName, "\t Address : ", StudentAddress)
print("Faculty : ", StudentFaculty, "\t Program : ", StudentProgram)
print("Intake : ", StudentIntake)