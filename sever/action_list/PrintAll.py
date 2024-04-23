from DB.StudentInfoTable import StudentInfoTable
class PrintAll:
    def __init__(self, parameters):
        self.parameters = parameters

    def execute(self):
        students_dict = self.get_students_dict()
        reply_msg = self.show(students_dict)
        return reply_msg

    def get_students_dict(self):
        student_records= StudentInfoTable().select_all_students()
        students_dict = {}

        for entry in student_records:
            DB_name = entry['name']
            DB_subject = entry['subject']
            DB_score = entry['score']
            if DB_name not in students_dict:
                students_dict[DB_name] = {'name': DB_name, 'scores': {}}
            students_dict[DB_name]['scores'][DB_subject] = DB_score

        return students_dict

    def show(self, students_dict):
        if students_dict:
            return {'status': 'OK', 'parameters': students_dict}
        return {'status': 'OK', 'parameters': {}}