from subprogram.AddStu import AddStu
from subprogram.PrintAll import PrintAll
from subprogram.DelStu import DelStu
from subprogram.ModifyStu import ModifyStu
import socket 
import json

host = "127.0.0.1"
port = 20001
BUFFER_SIZE = 1940

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


action_menu = {
    "add": AddStu,
    "del": DelStu,
    "modify": ModifyStu,
    "show": PrintAll
}

def print_menu():
    print()
    print("add: Add a student's name and score")
    print("del: Delete a student")
    print("modify: Modify a student's score")
    print("show: Print all")
    print("exit: Exit")
    selection = input("Please select: ")

    return selection

def main():
    client = SocketClient()
    select_result = "initial"

    while select_result != "exit":
        select_result = print_menu()
        try:
            action_menu[select_result](client).execute()
        except Exception as e:
            print(e)
    client.client_socket.close()

main()