from DB.Connect import Connection
from DB.Init import Initialization
from threading import Thread
import socket
import json
from subprogram.AddStu import AddStu
from subprogram.PrintAll import PrintAll
from subprogram.ModifyStu import ModifyStu
from subprogram.DelStu import DelStu
from subprogram.Query import Query

host = "127.0.0.1"
port = 20001

action_menu = {
    "add": AddStu,
    "show": PrintAll,
    "modify": ModifyStu,
    "del": DelStu,
    "query": Query
}

class SocketServer(Thread):
    def __init__(self):
        super().__init__()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)

    def serve(self):
        self.start()

    def run(self):
        while True:
            try:
                connection, address = self.server_socket.accept()
                print("{} connected".format(address))
                self.new_connection(connection=connection,
                                    address=address)
            except:
                pass

    def new_connection(self, connection, address):
        Thread(target=self.receive_data,
               kwargs={
                   "connection": connection,
                   "address": address}, daemon=True).start()

    def receive_data(self, connection, address):
        keep_going = True
        while keep_going:
            try:
                data = connection.recv(1024).strip().decode()
                if not data:
                    print(f"No data received from {address}, closing connection.")
                    keep_going = False
                    continue
            except Exception as e:
                print("Exeption happened {}, {}".format(e, address))
                break
            try:
                print(data)
                data = json.loads(data)
                print('    server received:{}'.format(data))
                command = data['command']
                parameters = data['parameters']

                reply_data = action_menu[command](parameters).execute()
                connection.send(json.dumps(reply_data).encode())
            except json.JSONDecodeError as json_error:
                print(f"JSON decode error: {json_error} from {address}, possibly client disconnected.")
                break

        connection.close()
        print("{} close connection".format(address))

def main():
    server = SocketServer()
    server.daemon = True
    server.serve()
    Connection.db_file_path = "student.db"
    Initialization().execute()

    while True:
        command = input()
        if command == "finish":
            break

    server.server_socket.close()
    print("leaving ....... ")

main()