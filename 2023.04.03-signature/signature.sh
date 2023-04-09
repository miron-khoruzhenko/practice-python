#!/bin/bash
# python /home/strewen/Desktop/vscode_projects/Python/2023.04.03-signature/sign.py > /home/strewen/Desktop/vscode_projects/Python/2023.04.03-signature/tmp.txt


python /home/strewen/Desktop/vscode_projects/Python/2023.04.03-signature/sign.py $1 | cat - $1 > temp && mv temp $1