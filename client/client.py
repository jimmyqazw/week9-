import socket 
import json
from AddStu import AddStu
from PrintAll import PrintAll
from DelStu import DelStu
from ModifyStu import ModifyStu

class SocketClient:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.client_socket.connect((host, port))
 
    def send_command(self, command, student_dict):
        send_data = {'command': command, 'parameters': student_dict}
        self.client_socket.send(json.dumps(send_data).encode())
        print("    The client sent data => {}".format(send_data))

    def wait_response(self):
        data = self.client_socket.recv(BUFFER_SIZE)
        result = data.decode()
        print("    The client received data => {}".format(result))

        return result
    
options = {
    "add": AddStu,
    "del": DelStu,
    "modify": ModifyStu,
    "show": PrintAll
}

def show_options():
    print()
    print("add: Add a student's name and score")
    print("del: Delete a student")
    print("modify: Modify a student's score")
    print("show: Print all")
    print("exit: Exit")
    choice = input("Please select: ")
    return choice

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 20001
    BUFFER_SIZE = 1940
    client = SocketClient()
    user_choice = "initial"

    while True:
        user_choice = show_options()
        if user_choice == "exit":
            break
        try:
            action = options[user_choice](client)
            action.execute()
        except KeyError as e:
            print(f"Invalid option: {e}")
    client.client_socket.close()
