from rich import print, pretty
import os, sys, requests

def get_user() -> str:
    try:
        with open("./config/user/cfg.cfg", "r") as file:
            l = file.readline()
            return l.split("user_name")[1].split(":")[1]
    except:
        print("Error user is not init? Use config --help")
        exit()
def get_server() ->str:
    try:
        with open("./config/user/server/cfg.cfg", "r") as file:
            return file.readline()
    except:
        print("Server? Use config --help")
        exit()

def help() -> None: ...
def get() -> None: ...
def init() -> None: ...
def add(args: list) -> None:
    if args[0] == "--help":
        print("for add task write this command add '<user>' '<label>' '<text>'")
        return
    if len(args) != 3:
        print("Please write command correctly, use add --help, for more info")
        return
    print(requests.post(get_server()+"/add", headers={"user":args[0],"label":args[1],"text":args[2], "creator":get_user()}).text)   
    
def config(args: list) -> None:
    if args[0] == "--help":
        print("for init user write this command config -u <user>")
        print("for add server write this command config -s <ip:port>")
    elif args[0] == "-u":
        os.makedirs("./config/user", exist_ok=True)
        with open("./config/user/cfg.cfg", "w") as file:
            file.write("user_name:"+args[1])
        print("Done add user")
    elif args[0] == "-s":
        os.makedirs("./config/user/server", exist_ok=True)
        with open("./config/user/server/cfg.cfg", "w") as file:
            file.write(args[1])
        print("Done add server")
    else:
        print(args)
        print("Args not correctly")
        
def done() -> None: ...
def get_my() -> None: ...

def main() -> None:
    if len(sys.argv) > 1:
        if sys.argv[1] == "--help":
            help()
        elif sys.argv[1] == "get": ...
        elif sys.argv[1] == "init": ...
        elif sys.argv[1] == "add":
            add(sys.argv[2:])
        elif sys.argv[1] == "sync": ...
        elif sys.argv[1] == "config":
            config(args=sys.argv[2:])
        elif sys.argv[1] == "done": ...
        elif sys.argv[1] == "get_my": ...
        else:
            print("Command non correctly")
    else:
        print("Please write command, --help")

if __name__ == "__main__":
    main()