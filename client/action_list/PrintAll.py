import json

class PrintAll:
    def __init__(self, client):
        self.client = client

    def execute(self):
        reply_data_dict = self.show_communicate()
        self.show_student(reply_data_dict)

    def show_communicate(self):
        self.client.send_command("show", student_dict={})
        reply_data = self.client.wait_response()
        reply_data_dict = json.loads(reply_data)

        return reply_data_dict

    def show_student(self, reply_data_dict):
        print ("\n==== student list ====\n")
        for name, info in reply_data_dict['parameters'].items():
            print("Name: {}".format(name))
            for subject, score in info['scores'].items():
                print("    subject: {}, score: {}".format(subject, score))
            print()

        print ("======================")