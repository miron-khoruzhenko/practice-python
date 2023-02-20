import os
from datetime import date
from distutils.dir_util import copy_tree


cwd     = os.getcwd()
source  = os.path.join(os.path.dirname(__file__), "2023.02.18-gnp-src")
todayDate = date.today().strftime("%Y.%m.%d")


allFirstSubdirs = os.listdir(source)
allFirstSubdirs.sort()
# allFirstSubdirs = allFirstSubdirs[:-1]

folderIndex = 0

class COLORS:
    DEFAULT = '\u001b[0m'
    DARKORANGE = '\u001b[38;5;202m'
    ORANGE  = '\u001b[38;5;214m'
    # YELLOW  = '\u001b[38;5;226m'
    YELLOW  = '\033[93m'
    ERROR   = '\033[91m'
    UNDERLINE = '\033[4m'


while True:
    print(f'{COLORS.DARKORANGE}Select project format:{COLORS.YELLOW}')

    for dir in allFirstSubdirs:
        print('  ->', dir)

    folderIndex = input(f'  {COLORS.ORANGE}Enter only number of project>{COLORS.DEFAULT} ')
    os.system('clear')

    if(not folderIndex.isnumeric()):
        print(f'{COLORS.ERROR}ERROR: Enter only {COLORS.UNDERLINE}number{COLORS.DEFAULT}{COLORS.ERROR} of folder{COLORS.DEFAULT}')
        continue

    folderIndex = int(folderIndex)
    if(0 > folderIndex or folderIndex > len(allFirstSubdirs) -1):
        print(f'{COLORS.ERROR}ERROR: Enter only {COLORS.UNDERLINE}number between{COLORS.DEFAULT}{COLORS.ERROR} 0 and ' + str(len(allFirstSubdirs) - 1) + f'{COLORS.DEFAULT}')
        continue
    break


selectedFolder = allFirstSubdirs[folderIndex]
source = os.path.join(source, selectedFolder)

while True:
    print(f'{COLORS.DARKORANGE}Enter a name or leave the field blank to use by default [{COLORS.YELLOW}' + todayDate + "-project-name" + f'{COLORS.DARKORANGE}]{COLORS.YELLOW}')
    name = todayDate + '-' + input(f'  {todayDate}-')

    if(name in os.listdir(cwd)):
        os.system('clear')
        print(f'{COLORS.ERROR}ERROR: This folder already exists, choose a different name{COLORS.DEFAULT}')
        continue

    if(name == todayDate + '-'):
        os.system('clear')
        dist    = os.path.join(cwd, todayDate + "-project-name")
        break
    
    else:
        sure = 0

        while sure != 'y' and sure != 'n':
            os.system('clear')
            sure = input(f'{COLORS.ORANGE}The name of the project folder {COLORS.UNDERLINE + COLORS.YELLOW}{name}{COLORS.DEFAULT}{COLORS.ORANGE} are you sure?[Y/n]{COLORS.DEFAULT} ').lower()
            os.system('clear')

        if(sure == 'y'):
            dist = os.path.join(cwd, name)
            break



while True:
    print(f'{COLORS.YELLOW} !!! WARNING !!! {COLORS.DEFAULT}\n')
    print(f'     {COLORS.YELLOW}Source:{COLORS.DEFAULT} ' + source)
    print(f'{COLORS.YELLOW}Destination:{COLORS.DEFAULT} ' + dist)
    x = input(f'\n{COLORS.YELLOW}Are you sure?[Y/n]{COLORS.DEFAULT} ').lower()
    
    os.system('clear')

    if(x == 'y'):
        copy_tree(source, dist)
        break
    elif(x == 'n'):
        quit()
    else:
        print(f'{COLORS.ERROR}ERROR try again{COLORS.DEFAULT}')
