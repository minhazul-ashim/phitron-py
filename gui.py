import pyautogui as pgui;
n = int(input());

for i in range(0, n+1) :
    for j in range(0, i) :
        pgui.write('#');
    pgui.write('\n');