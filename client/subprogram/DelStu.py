class DelStu:
    def __init__(self, client):
        self.student_dict = {}
        self.client = client

    def execute(self):
        self.get_name()
        self.query_first()
        check = input("  Confirm to delete (y/n): ")
        if check =='y':
            self.del_communicate()
            print("    Del success")

    def get_name(self):
        name = input("  Please input a student's name or exit: ")
        if name == "exit":
            print("    exit")
            return
        else:
            self.student_dict = {'name' : name}

    def query_first(self):
        self.client.send_command("query", self.student_dict)
        self.client.wait_response()

    def del_communicate(self):
        self.client.send_command("del", self.student_dict)
        self.client.wait_response()
