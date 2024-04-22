class DelStu:
    def __init__(self, client):
        self.student_dict = {}
        self.client = client

    def execute(self):
        self.get_student_name()
        self.query_student_before_deletion()
        answer = input("  Confirm to delete (y/n): ")
        if answer =='y':
            self.delete_student()
            print("    Del success")

    def get_student_name(self):
        name = input("  Please input a student's name or exit: ")
        if name == "exit":
            print("    exit")
            return
        else:
            self.student_dict = {'name' : name}

    def query_student_before_deletion(self):
        self.client.send_command("query", self.student_dict)
        self.client.wait_response()

    def delete_student(self):
        self.client.send_command("del", self.student_dict)
        self.client.wait_response()
