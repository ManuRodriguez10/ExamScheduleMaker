import json
with open('student_info.json') as json_file:
    student_data = json.load(json_file)

def student_intructions():
    """
        Display instructions for students to register for final exams.

        Provides a step-by-step guide on how to select exam times.

        Returns:
        None
        """
    print('\nWelcome! \n'
          '\t Get ready to make your schedule for final exams\n'
          '\t Below you will be provided with a set of instructions in order to make your best exam schedule possible \n'
          "\tHere's how it works: ")
    input('\nPress enter to continue....')
    print('\nThe first step is to enter your Student ID number\n'
          '\t After you have enter your ID number the classes you are currently enrolled in will be shown\n'
          '\tYou will need to pick out the times you would like to take the exam making sure that none of them overlap with each other')
    input('\nPress enter to continue...')


def find_student(student_id, student_data,student_name,student_info):
    """
      Find a student by their ID and display their class enrollment and available exam times.

      Parameters:
      student_id (str): The unique identifier of the student.
      student_data (dict): A dictionary containing student information with student IDs as keys.
      student_name (str): The name of the student.
      student_info (dict): Information about the student's classes and test times.

      Returns:
      str: The name of the student if found, otherwise None.
      """
    if student_id in student_data:
        classes = [class_info["class_name"] for class_info in student_info["classes"]]
        classes_str = " and ".join(classes)
        message = f'Hello, {student_name} you are registered in {classes_str}.\n'

        for class_info in student_info["classes"]:
            class_name = class_info["class_name"]
            class_times = [f"{test_time['date']} at {test_time['time']}" for test_time in class_info["test_times"]]
            class_times_str = ", ".join(class_times)
            message += f'\nFor {class_name}, the available times are: {class_times_str}'

        print(message)
        return student_name
    else:
        print("Student not found")

def register_time(student_id, student_data, class1, class2,registered):
    """
        Register exam times for a student based on their ID and available class options.

        Parameters:
        student_id (str): The unique identifier of the student.
        student_data (dict): A dictionary containing student information with student IDs as keys.
        class1 (str): The first class name.
        class2 (str): The second class name.
        registered (list): A list to store registered students.

        Returns:
        tuple: A tuple containing the chosen exam times and class names for the student.
        """
    if student_id in student_data:
        student_info = student_data[student_id]
        student_name = student_info["name"]
        classes = [class_info["class_name"] for class_info in student_info["classes"]]
        class1 = classes[0]
        class2 = classes[1]

        # Extract test times for class1
        test_times_class1 = [time_info["time"] for class_info in student_info["classes"] if class_info["class_name"] == class1 for time_info in class_info["test_times"]]
        options_class1 = ", ".join(test_times_class1)
        options_class1a, options_class1b = test_times_class1

        # Extract test times for class2
        test_times_class2 = [time_info["time"] for class_info in student_info["classes"] if class_info["class_name"] == class2 for time_info in class_info["test_times"]]
        options_class2 = ", ".join(test_times_class2)
        options_class2a, options_class2b = test_times_class2

        while True:
            print(f"\nWhat time would you like to choose for {class1}? ")
            print(f'Option A: {options_class1a} \n Option B: {options_class1b}')
            choice = input('Choose one option: ').upper()
            if choice == 'A':
                time_class1 = options_class1a
                break
            elif choice == 'B':
                time_class1 = options_class1b
                break
            else:
                print('Invalid. Please provide one of the options given')
                registered.append(student_name)

        while True:
            print(f"\nWhat time would you like to choose for {class2}? ")
            print(f'Option A: {options_class2a} \n Option B: {options_class2b}')
            choice = input('Choose one option: ').upper()
            if choice == 'A':
                time_class2 = options_class2a
                break
            elif choice == 'B':
                time_class2 = options_class2b
                break
            else:
                print('Invalid. Please provide one of the options given')
                registered.append(student_name)

        print(f"\nThank you, {student_name}! \n\nYour chosen exam time for {class1} is {time_class1}.")
        print(f"And your chosen exam time for {class2} is {time_class2}.")

        return time_class1, time_class2,class1,class2
    else:
        print("Student not found")