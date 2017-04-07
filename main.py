

value1=sys.argv[1]
value2=sys.argv[2]

from check import check
from progress import progress


print """This are the options:
1. Check my progress
2. Modify my progress
3.exit
"""

value3 = raw_input("What would you want to do" )
count = 1

if value3 == "1":
    progress = progress()
    menu = """"""



    for key in progress:
        menu += """
Task""" + count + """ """ + key + """: """ + progress[key] + """
"""
    count += 1

    print menu

elif value3 == "2":
    print "What task would you want modified: "

    progress = progress()

    menu = """"""
    for key in progress:
        menu += """
Task""" + count + """ """ + key + """: """ + progress[key] + """
"""
    count += 1

    value1 = raw_input("What task would you want to modify: ")

    result = check(value1)

    if result == "true":
        print "The task has been marked as achieved"

    elif result == "false":
        print "The task was already marked as done"

    else:
        print "This task was already done"

else:
    print "Thank you, have a nice day"
    exit(0)
