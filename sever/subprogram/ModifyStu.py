from DB.Info import StudentInfo
class ModifyStu:
    def __init__(self, parameters):
        self.parameters = parameters

    def execute(self):
        reply_msg = self.modify()
        return reply_msg

    def modify(self):
        name = self.parameters['name']
        scores = self.parameters['scores']
        StudentInfo().update_a_student(name, scores)

        return {'status': 'OK'}