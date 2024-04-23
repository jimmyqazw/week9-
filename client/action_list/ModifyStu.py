import json
class ModifyStu:
    def __init__(self, client):
        self.student_dict = {}
        self.client = client

    def execute(self):
        name = self.get_name()
        raw_data = self.client_query() # raw_data = {'status': 'OK', 'scores': {'Python': 19.0, 'Eng': 100.0}}
        if raw_data.get('status') == 'Fail':
            print("  The name {} is not found".format(name))
            return

        self.get_current_subjects(raw_data)
        self.main(raw_data)


    def get_name(self):
        name = input("  Please input a student's name or exit: ")
        if name == "exit":
            print("    exit")
            return
        else:
            self.student_dict = {'name' : name}
            return name

    def get_current_subjects(self, raw_data):
        print("  current subjects are ", end='')
        for subject, score in raw_data.get('scores').items(): # {'Python': 19.0, 'Eng': 100.0}
                print("{} ".format(subject), end='')

    def main(self, raw_data):
        self.student_dict['scores'] = raw_data.get('scores') # self.student_dict = {'name' : name, 'scores' : {'Python': 19.0, 'Eng': 100.0} }

        cl = input("\n\n  Please input a subject you want to change: ")
        if cl in self.student_dict['scores']:
            self.Modify(cl)
        else:
            self.Add(cl)
    def Modify(self, cl):
        while True:
            try:
                score = float(input("  Please input Bill's {} score or < 0 for discarding the subject: ".format(cl)))
                if score < 0:
                    break
                self.student_dict['scores'][cl] = score
                self.client_modify()
                print("  Modify [{}, {}, {}] success".format(self.student_dict['name'], cl, score))
                break
            except Exception as e:
                print("    The exception {} occurs".format(e))
        # return test
    def Add(self, cl):
        while True:
            try:
                score = float(input("  Please input Bill's {} score or < 0 for discarding the subject: ".format(cl)))
                if score < 0:
                    break
                self.student_dict['scores'][cl] = score
                self.client_modify()
                print("  Add [{}, {}, {}] success".format(self.student_dict['name'], cl, score))
                break
            except Exception as e:
                print("    The exception {} occurs".format(e))
        # return test

    def client_query(self):
        self.client.send_command("query", self.student_dict)
        raw_data = self.client.wait_response()
        raw_data = json.loads(raw_data)

        return raw_data

    def client_modify(self):
        self.client.send_command("modify", self.student_dict)
        self.client.wait_response()