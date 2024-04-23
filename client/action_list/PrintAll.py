import json

class PrintAll:
    def __init__(self, client):
        self.client = client

    def execute(self):
        keep_going_dict = self.client_print()
        self.print(keep_going_dict)

    def client_print(self):
        self.client.send_command("show", student_dict={})
        raw_data = self.client.wait_response()
        keep_going_dict = json.loads(raw_data)

        return keep_going_dict

    def print(self, keep_going_dict):
        print ("\n==== student list ====\n")
        for name, info in keep_going_dict['parameters'].items():
            print("Name: {}".format(name))
            for subject, score in info['scores'].items():
                print("    subject: {}, score: {}".format(subject, score))
            print()

        print ("======================")