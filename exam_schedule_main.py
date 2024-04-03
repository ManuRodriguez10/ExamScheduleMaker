import json
import student_modules
import teacher_modules

# Load json for student info
with open('student_info.json') as json_file:
    student_data = json.load(json_file)

# Load json for teacher info
with open('teacher_info.json') as json_file:
    teacher_data = json.load(json_file)

#Define Variables
student_id=None
teacher_id=None
student_name=None
student_info=None
teacher_name=None

# Students that register will be appended to this list
all_students = ["Alice", "Bob", "Charlie","David","Eve","Frank","Grace","Harry","Ivy","Jack","Kate","Oliver","Sophia","Liam","Ava"]

math_registered = ['Alice', 'Bob']
writing_registered = []
history_registered = ['David','Eve']
physics_registered = ['Charlie']
bio_registered = ['Grace','Harry']
chem_registered = ['Oliver']
cs_registered = []
english_registered = ['Liam']
geog_registered = ['Ava']

registered = []
current=[]

registered_lists = [math_registered, writing_registered, history_registered,
                       physics_registered, bio_registered, chem_registered,
                       cs_registered, english_registered, geog_registered]
student_mode = True
try_again = True

while True:  # Loop indefinitely until user quits

    # Greeting and Instructions
    mode = input("Please enter if you're a teacher or a student: ").strip().lower()
    valid_modes = ["teacher", "student"]

    while mode not in valid_modes:
        print("Invalid. Please enter 'teacher' or 'student'.")
        mode = input("Please enter if you're a teacher or a student: ").strip().lower()

    if mode == 'student':
        student_modules.student_intructions()
        # Find the student through Student ID
        student_id = input('\nEnter your Student ID: ')
        if student_id in student_data:
            student_info = student_data[student_id]
            student_name = student_info["name"]
        else:
            print("Student ID not found. Please try again.")
            continue
        # Print welcome message and class options
        student_modules.find_student(student_id, student_data, student_name, student_info)
        # Register for the class times
        class1 = None
        class2 = None
        student_modules.register_time(student_id, student_data, class1, class2, registered)

    if mode == 'teacher':
        # Find the teacher through their ID
        teacher_id = input('\nEnter your Teacher ID: ')
        if teacher_id in teacher_data:
            teacher_info = teacher_data[teacher_id]
            teacher_name = teacher_info["teacher_name"]
        else:
                print('Teacher ID not found. Please try again.')
                continue
            # Find the teacher's class and assign students to the respective list
        teacher_class = teacher_modules.find_class(teacher_id, teacher_data, student_data)
        students_missing = teacher_modules.students_missing(teacher_id, teacher_data, all_students, registered_lists)
        # Depending on the class that was selected, the registered list will be assigned to that class list
        if teacher_class == 'MATH101':
                math_registered.append(registered)
                current = math_registered
        elif teacher_class == 'WRITING101':
                writing_registered.append(registered)
                current = writing_registered
        elif teacher_class == 'HIST101':
                history_registered.append(registered)
                current = history_registered
        elif teacher_class == 'PHYSICS101':
                physics_registered.append(registered)
                current = physics_registered
        elif teacher_class == 'BIO101':
                bio_registered.append(registered)
                current = bio_registered
        elif teacher_class == 'CHEM101':
                chem_registered.append(registered)
                current = chem_registered
        elif teacher_class == 'CS101':
                cs_registered.append(registered)
                current = cs_registered
        elif teacher_class == 'ENG101':
                english_registered.append(registered)
                current = english_registered
        elif teacher_class == 'GEOG101':
                geog_registered.append(registered)
                current = geog_registered

                # Print the registered students (if applicable)
        print(f'\n Welcome back {teacher_name}!')
        print(f'The students that are currently registered for the {teacher_class} exam are: {current} \n '
                      f'There are {students_missing} students missing to register')

    # Ask user to quit or go back to the menu
    user_choice = input("\nWould you like to quit or go back to the main menu? (quit/menu): ").strip().lower()
    valid_choices = ["quit", "menu"]

    while user_choice not in valid_choices:
        print("Invalid choice. Please enter 'quit' or 'menu'.")
        user_choice = input("\nWould you like to quit or go back to the main menu? (quit/menu): ").strip().lower()

    if user_choice == "quit":

        try_again = False  # Exit the loop completely (quit)
        print("\nGoodbye!")
        break
    else:
        print('\nWelcome back! \n \n')





















