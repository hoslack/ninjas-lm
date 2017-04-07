def progress():
    my_file = open("data.txt", "r+")
    payload = {}
    for line in my_file:
        task = line.split(':')
        if task[3] == 'True\n':
            status = task[3][:4]
            payload[task[1]] = status
        elif task[3] == 'False\n':
            status = task[3][:5]
            payload[task[1]] = status
    return payload
