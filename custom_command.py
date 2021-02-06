def new_path_location(current_path, new_path):
    if not new_path:
        return current_path

    if new_path[0] == '.':
        new_path = new_path[1:]
        if not new_path:
            return current_path
        new_path = new_path[1:]  # remove the slash
        return new_path_location(current_path, new_path)

    if new_path[0] == '..':
        new_path = new_path[1:]
        if not current_path:
            return current_path
        current_path.pop()
        current_path.pop()
        if not new_path:
            return current_path
        new_path = new_path[1:]
        return new_path_location(current_path, new_path)

    if not new_path[0].isalnum():
        return new_path[0] + ": No such file or directory"

    if current_path[-1] != '/':
        current_path.append('/')

    current_path.append(new_path[0])
    new_path = new_path[1:]
    if not new_path:
        return current_path
    new_path = new_path[1:]  # remove the slash
    return new_path_location(current_path, new_path)

while True:
    print ("# ", end = "")
    command = input().split()
    if len(command) != 5:
        print ("You have provided wrong input")
        continue
    if command[0] != 'newcd':
        print ("You have provided wrong cdcommand")
        continue

    current_path = command[1]
    new_path = command[2]
    while current_path.find("//") != -1:
        current_path = current_path.replace("//", "/")
        print (current_path)
    while new_path.find("//") != -1:
        new_path = new_path.replace("//", "/")

    current_path = current_path.replace("/", "@/@").split("@")
    current_path = [item for item in current_path if item != '']
    new_path = new_path.replace("/", "@/@").split("@")
    new_path = [item for item in new_path if item != '']

    if new_path[0] == '/':  
        current_path = ''.join(new_path)
        print (current_path)
        continue

    current_path = new_path_location(current_path, new_path)
    if not current_path:
        current_path = ['/']
    current_path = ''.join(current_path)
    print (current_path)

