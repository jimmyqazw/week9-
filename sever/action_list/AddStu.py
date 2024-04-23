from DB.StudentInfoTable import StudentInfoTable
class AddStu:
    def __init__(self, parameters):
        self.parameters = parameters

    def execute(self):
        students_dict = self.get_students_dict()
        reply_msg = self.add(students_dict)
        return reply_msg

    def get_students_dict(self):
        student_records = StudentInfoTable().select_all_students()
        students_dict = {}

        for entry in student_records:
            DB_name = entry['name']
            DB_subject = entry['subject']
            DB_score = entry['score']
            if DB_name not in students_dict:
                students_dict[DB_name] = {'name': DB_name, 'scores': {}}
            students_dict[DB_name]['scores'][DB_subject] = DB_score

        return students_dict

    def add(self, students_dict):
        name = self.parameters['name']
        scores = self.parameters['scores']

        if name in students_dict:
            return {'status': 'Fail', 'reason': 'The name already exists.'}
        StudentInfoTable().insert_a_student(name, scores)
        return {'status': 'OK'}