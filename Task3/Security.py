def add_user(username, real_name, password):
    with open("passwd.txt", "a") as file:
        file.write(f"{username}:{real_name}:{password}\n")
    print("User Created.")

def delete_user(username):
    lines = []
    with open("passwd.txt", "r") as file:
        for line in file:
            if not line.startswith(username + ":"):
                lines.append(line)
    with open("passwd.txt", "w") as file:
        file.writelines(lines)
    print("User Deleted.")

def change_password(username, new_password):
    lines = []
    with open("passwd.txt", "r") as file:
        for line in file:
            if line.startswith(username + ":"):
                parts = line.strip().split(":")
                parts[2] = new_password
                line = ":".join(parts) + "\n"
            lines.append(line)
    with open("passwd.txt", "w") as file:
        file.writelines(lines)
    print("Password changed.")

def check_password(username, password):
    with open("passwd.txt", "r") as file:
        for line in file:
            parts = line.strip().split(":")
            if parts[0] == username and parts[2] == password:
                return True
    return False

def main():
    action = input("Choose action (adduser, deluser, passwd, login): ")
    
    if action == "adduser":
        username = input("Enter new username: ")
        real_name = input("Enter real name: ")
        password = input("Enter password: ")
        add_user(username, real_name, password)
    
    elif action == "deluser":
        username = input("Enter username: ")
        delete_user(username)
    
    elif action == "passwd":
        username = input("User:             ")
        current_password = input("Current Password: ")
        new_password = input("New Password:     ")
        confirm_password = input("Confirm:          ")
        if new_password == confirm_password:
            change_password(username, new_password)
        else:
            print("Passwords do not match.")
    
    elif action == "login":
        username = input("User:     ")
        password = input("Password: ")
        if check_password(username, password):
            print("Access granted.")
        else:
            print("Access denied.")
    
    else:
        print("Invalid action.")

if __name__ == "__main__":
    main()
