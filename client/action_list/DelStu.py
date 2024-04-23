class DelStu:
    def __init__(self, client):
        self.student_dict = {}
        self.client = client

    def execute(self):
        self.get_name()
        self.client_query()
        answer = input("  Confirm to delete (y/n): ")
        if answer =='y':
            self.client_del()
            print("    Del success")

    def get_name(self):
        name = input("  Please input a student's name or exit: ")
        if name == "exit":
            print("    exit")
            return
        else:
            self.student_dict = {'name' : name}

    def client_query(self):
        self.client.send_command("query", self.student_dict)
        self.client.wait_response()

    def client_del(self):
        self.client.send_command("del", self.student_dict)
        self.client.wait_response()
