import json
with open('teacher_info.json') as json_file:
    teacher_data = json.load(json_file)
with open('student_info.json') as json_file:
    student_data = json.load(json_file)

def find_class(teacher_id, teacher_data, student_data):
    """
       Find the class associated with a given teacher ID.

       Parameters:
       teacher_id (str): The unique identifier of the teacher.
       teacher_data (dict): A dictionary containing teacher information with teacher IDs as keys.
       student_data (dict): A dictionary containing student information with student IDs as keys.

       Returns:
       str or None: The class associated with the provided teacher ID, or None if the teacher ID is not found in the teacher data.
       """
    if teacher_id in teacher_data:
        teacher_info = teacher_data[teacher_id]
        teacher_class = list(teacher_info['classes'].keys())[0]
        return teacher_class

def students_missing(teacher_id, teacher_data, all_students, registered_lists):
    """
        Calculate the number of students missing from a class associated with a given teacher ID.

        Parameters:
        teacher_id (str): The unique identifier of the teacher.
        teacher_data (dict): A dictionary containing teacher information with teacher IDs as keys.
        all_students (list): A list containing all student names or IDs.
        registered_lists (list of lists): A list of lists where each sublist contains the registered students for a particular class.

        Returns:
        int: The number of students missing from the class associated with the provided teacher ID.
        """
    if teacher_id in teacher_data:
        teacher_info = teacher_data[teacher_id]
        class_name = list(teacher_info["classes"].keys())[0]
        class_students = teacher_info["classes"][class_name]["students"]

        # Filter registered students based on the class name
        registered_in_class = [reg_list for reg_list in registered_lists if
                               class_name in [r[0] for r in reg_list]]
        registered_students = set([item for sublist in registered_in_class for item in sublist[1:]])

        # Calculate the number of students missing from the class specifically
        students_missing = len(class_students) - len(registered_students)

        return students_missing







