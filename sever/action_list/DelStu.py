from DB.StudentInfoTable import StudentInfoTable
class DelStu:
    def __init__(self, parameters):
        self.parameters = parameters

    def execute(self):
        reply_msg = self.delstu()
        return reply_msg

    def delstu(self):
        name = self.parameters['name']
        StudentInfoTable().delete_a_student(name)

        return {'status': 'OK'}