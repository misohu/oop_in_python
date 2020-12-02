from information_system import InformationSystem
from personal import Teacher 

def print_menu():
    print("\n*******************************************")
    print("Vitajte v systeme")
    print("Stlačte prosím:")
    print("\t[0] Pre pridanie učiteľa")
    print("\t[1] Pre pridanie kurzu")
    print("\t[2] Pre pridanie žiaka")
    print("\t[3] Pre ukončenie práce so systémom")
    print("\t[4] Pre zoznam kurzov")
    print("\t[5] Pre zoznam ziakov")
    print("\t[6] Pre zoznam ucitelov")
    
in_sys = InformationSystem(
    teachers=[
        Teacher("Michal", "Hucko", "Ing"),
        Teacher("Andrej", "Hucko", "Ing")
    ]
)

while True:
    print_menu()
    try:
        menu_choice=int(input("Menu choice: "))
        if menu_choice<0 or menu_choice >=7:
            raise Exception("Wrong menu choice")
    except Exception as e:
        print(e)
        print("Please choose valid menu choice")
        continue
    if menu_choice ==3:
        print("Good bye")
        break
    elif menu_choice == 0:
        in_sys.create_teacher()
    elif menu_choice == 1:
        in_sys.create_course()
    elif menu_choice == 2:
        in_sys.create_student()
    elif menu_choice == 4:
        print("Courses are")
        for course in in_sys.courses:
            print(course)
    elif menu_choice == 5:
        print("Students are")
        for student in in_sys.students:
            print(student)
    elif menu_choice == 6:
        print("Teachers are")
        for teacher in in_sys.teachers:
            print(teacher)
    
