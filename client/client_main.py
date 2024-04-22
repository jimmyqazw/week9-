from client_demo import SocketClient
from action_list.AddStu import AddStu
from action_list.PrintAll import PrintAll
from action_list.DelStu import DelStu
from action_list.ModifyStu import ModifyStu

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