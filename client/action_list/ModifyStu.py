import json
class ModifyStu:
    def __init__(self, client):
        self.student_dict = {}
        self.client = client

    def execute(self):
        name = self.get_name()
        raw_data = self.query_first() 
        if raw_data.get('status') == 'Fail':
            print("  The name {} is not found".format(name))
            return

        self.get_subject(raw_data)
        self.main(raw_data,name)


    def get_name(self):
        name = input("  Please input a student's name or exit: ")
        if name == "exit":
            print("    exit")
            return
        else:
            self.student_dict = {'name' : name}
            return name

    def get_subject(self, raw_data):
        print("  current subjects are ", end='')
        for subject, score in raw_data.get('scores').items():
                print("{} ".format(subject), end='')

    def main(self, raw_data,name):
        self.student_dict['scores'] = raw_data.get('scores') 

        change_subject = input("\n\n  Please input a subject you want to change: ")
        if change_subject in self.student_dict['scores']:
            self.Modify(change_subject,name)
        else:
            self.Add(change_subject,name)

    def Modify(self, change_subject,name):
        while True:
            try:
                score = float(input("  Please input {}'s {} score or < 0 for discarding the subject: ".format(name,change_subject)))
                if score < 0:
                    break
                self.student_dict['scores'][change_subject] = score
                self.modify_communicate()
                print("  Modify [{}, {}, {}] success".format(self.student_dict['name'], change_subject, score))
                break
            except Exception as e:
                print("    The exception {} occurs".format(e))

    def Add(self, change_subject,name):
        while True:
            try:
                score = float(input("  Please input {}'s {} score or < 0 for discarding the subject: ".format(name,change_subject)))
                if score < 0:
                    break
                self.student_dict['scores'][change_subject] = score
                self.modify_communicate()
                print("  Add [{}, {}, {}] success".format(self.student_dict['name'], change_subject, score))
                break
            except Exception as e:
                print("    The exception {} occurs".format(e))
        # return test

    def query_first(self):
        self.client.send_command("query", self.student_dict)
        raw_data = self.client.wait_response()
        raw_data = json.loads(raw_data)

        return raw_data

    def modify_communicate(self):
        self.client.send_command("modify", self.student_dict)
        self.client.wait_response()