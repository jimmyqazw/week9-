from sqlite.StudentInfoTable import StudentInfoTable

class AddStu:
    def __init__(self, parameters):
        self.parameters = parameters

    def execute(self):
        students = self.get_students()
        return self.add(students)

    def get_students(self):
        records = StudentInfoTable().select_all_students()
        students = {}
        for record in records:
            name, subject, score = record['name'], record['subject'], record['score']
            if name not in students:
                students[name] = {'name': name, 'scores': {}}
            students[name]['scores'][subject] = score
        return students

    def add(self, students):
        name, scores = self.parameters['name'], self.parameters['scores']
        if name in students:
            return {'status': 'Fail', 'reason': 'The name already exists.'}
        StudentInfoTable().insert_a_student(name, scores)
        return {'status': 'OK'}

class DelStu:
    def __init__(self, parameters):
        self.parameters = parameters

    def execute(self):
        return self.delete()

    def delete(self):
        name = self.parameters['name']
        StudentInfoTable().delete_a_student(name)
        return {'status': 'OK'}

class ModifyStu:
    def __init__(self, parameters):
        self.parameters = parameters

    def execute(self):
        return self.modify()

    def modify(self):
        name, scores = self.parameters['name'], self.parameters['scores']
        StudentInfoTable().update_a_student(name, scores)
        return {'status': 'OK'}

class PrintAll:
    def __init__(self, parameters):
        self.parameters = parameters

    def execute(self):
        students = self.get_students()
        return {'status': 'OK', 'parameters': students if students else {}}

    def get_students(self):
        records = StudentInfoTable().select_all_students()
        students = {}
        for record in records:
            name, subject, score = record['name'], record['subject'], record['score']
            if name not in students:
                students[name] = {'name': name, 'scores': {}}
            students[name]['scores'][subject] = score
        return students

class Query:
    def __init__(self, parameters):
        self.parameters = parameters

    def execute(self):
        students = self.get_students()
        return self.query(students)

    def get_students(self):
        records = StudentInfoTable().select_all_students()
        students = {}
        for record in records:
            name, subject, score = record['name'], record['subject'], record['score']
            if name not in students:
                students[name] = {'name': name, 'scores': {}}
            students[name]['scores'][subject] = score
        return students

    def query(self, students):
        name = self.parameters['name']
        if name in students:
            scores = students[name]['scores']
            return {'status': 'OK', 'scores': scores}
        return {'status': 'Fail', 'reason': 'The name is not found.'}