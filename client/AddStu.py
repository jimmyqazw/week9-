import json

class AddStu:
    def __init__(self, client):
        self.student_dict = {}
        self.client = client

    def execute(self):
        name = self.get_student_name()
        self.query_student_before_deletion()
        self.collect_student_scores(name)
        self.add_student_to_server()

    def get_student_name(self):
        name = input("  Please input a student's name or exit: ")
        if name == "exit":
            print("    exit")
            return
        else:
            self.student_dict = {'name' : name}
            return name

    def collect_student_scores(self, name):
        scores = {}
        while True:
            subject = input("  Please input a subject name or exit for ending: ")
            if subject == "exit":
                return
            while True:
                try:
                    score = float(input(f"  Please input {name}'s {subject} score or < 0 for discarding the subject: "))
                    if score < 0:
                        break
                    scores[subject] = score
                    self.student_dict['scores'] = scores
                    break
                except Exception as e:
                    print(f"    Wrong format with reason {e}, try again")

    def query_student_before_deletion(self):
        self.client.send_command("query", self.student_dict)
        self.client.wait_response()

    def add_student_to_server(self):
        self.client.send_command("add", self.student_dict)
        raw_data = self.client.wait_response()

        raw_data = json.loads(raw_data)
        if raw_data.get('status') == 'OK':
            print("    Add {} success".format(self.student_dict)) 
        else:
            print("    Add {} fail".format(self.student_dict)) 