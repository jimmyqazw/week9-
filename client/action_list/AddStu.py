import json

class AddStu:
    def __init__(self, client):
        self.student_dict = {}
        self.client = client

    def execute(self):
        name = self.get_name()
        self.client_query()
        self.get_class(name)
        self.client_add()

    def get_name(self):
        name = input("  Please input a student's name or exit: ")
        if name == "exit":
            print("    exit")
            return
        else:
            self.student_dict = {'name' : name}
            return name

    def get_class(self, name):
        scores = {}
        while True:
            subject = input("  Please input a subject name or exit for ending: ")
            if subject == "exit":
                return
            while True:
                try:
                    score = float(input("  Please input {}'s {} score or < 0 for discarding the subject: ".format(name, subject)))
                    if score < 0:
                        break
                    scores[subject] = score
                    self.student_dict['scores'] = scores
                    break
                except Exception as e:
                    print("    Wrong format with reason {}, try again".format(e))

    def client_query(self):
        self.client.send_command("query", self.student_dict)
        self.client.wait_response()

    def client_add(self):
        self.client.send_command("add", self.student_dict)
        raw_data = self.client.wait_response()

        # 判斷名字是否已存在
        raw_data = json.loads(raw_data)
        if raw_data.get('status') == 'OK':
            print("    Add {} success".format(self.student_dict))  # 不存在
        else:
            print("    Add {} fail".format(self.student_dict))  # 已存在