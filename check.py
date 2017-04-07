
def check(task):

    with open('data.txt', 'r') as my_file:
        for line in my_file:
            find_task = line.split(":")
            if task == find_task[0]:
                new_line = ("\n{}:{}:true".format(find_task[:2][0], find_task[:2][1]))
                print new_line

    with open('data.txt', 'a') as f:
        f.write(new_line)

check('task_1')
