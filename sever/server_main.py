from server_demo import SocketServer
from DB.DBConnection import DBConnection
from DB.DBInitializer import DBInitializer

def main():
    server = SocketServer()
    server.daemon = True
    server.serve()
    DBConnection.db_file_path = "student.db"
    DBInitializer().execute()

    while True:
        command = input()
        if command == "finish":
            break

    server.server_socket.close()
    print("leaving ....... ")

main()