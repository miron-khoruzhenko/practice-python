import sys
from subprocess import Popen, PIPE


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")

allColors = []
for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        sys.stdout.write("\u001b[38;5;" + code + "m" + code.ljust(4))
        allColors.append("\u001b[38;5;" + code + "m")
        

    print("\u001b[0m")

print(len(allColors))

#* 0 - 255
showList = ''
while True:
    print('\nEnter \033[4mcolor index\u001b[0m to see color code \033[4mAll\u001b[0m to see all codes or \033[4mq\u001b[0m to quit:')
    showList = input('> ').lower()

    if(showList.isnumeric()):
        index = int(showList)

        if(0 <= index and index <= 255 ):
            print(allColors[index], "\\u001b" + allColors[index][1:], "some text" + "\u001b[0m", "\\u001b[0m")
            break
        else:
            print('Out of range')

    if(showList == 'all'):
        # for i in range(0, 16):
        #     for j in range(0, 16):
        #         code = str(i * 16 + j)
        #         sys.stdout.write("\u001b[38;5;" + code + "m" + code.ljust(4))
        #         print("\\u001b[38;5;" + code + "m")
        #     print("\u001b[0m", end='')
        for color in allColors:
            print(color, "\\u001b" + color[1:], "some text" + "\u001b[0m", "\\u001b[0m")
        break

    elif(showList == 'q'):
        quit()

# print("\u001b[38;5;2mHelloWorld")
# print('test')