import xlwings as xw
import shutil
import os

'''
maze
10122020200031_200
1
50
'''
'''
star
12122020004420_200
101
50
'''
'''
draw
12122020160911_200
151
50
'''
#just for copy, ignore it
question_type = input("question type:")
file = "./" + question_type + '/'
file = file + input("input file name:")
file_new = file + "/new"
file_ans = file + '/ans.txt'
maze_question = '以下哪個是程式運行後的最終目的地？'
star_question = '運行程式後總共可以獲取多少顆星星？'
draw_question = '以紅色突出為前方作起點，那個是運行程式後正確的圖形？'
lines = []
lines2 = []

if not os.path.exists(file_new) or not os.path.exists(file_ans):
    print("ERROR")
    input()
    exit(0)

start_row = int(input("Start question num:")) + 1
end_row = int(input("total question number:")) + start_row

app = xw.App(visible = True, add_book = False)
wb = xw.Book('2020hkpsoi_heat_question200.xlsx')
sht = wb.sheets[0]

with open(file + "/ans.txt", "r") as f1:
    lines = f1.read().splitlines()

if question_type == "star":
    with open(file + "/question.txt", "r") as f1:
        lines2 = f1.read().splitlines()

for i in range(start_row, end_row):
    sht.range("k" + str(i)).value = "0"
    sht.range("m" + str(i)).value = "0"
    sht.range("o" + str(i)).value = "0"
    sht.range("q" + str(i)).value = "0"
    print(lines[i - start_row + 1],end = ' ')
    if lines[i - start_row + 1] == 'A':
        sht.range("k" + str(i)).value = "10"
    elif lines[i - start_row + 1] == 'B':
        sht.range("M" + str(i)).value = "10"
    elif lines[i - start_row + 1] == 'C':
        sht.range("O" + str(i)).value = "10"
    elif lines[i - start_row + 1] == 'D':
        sht.range("Q" + str(i)).value = "10"
    if question_type == "maze":
        sht.range("j" + str(i)).value = "A"
        sht.range("l" + str(i)).value = "B"
        sht.range("n" + str(i)).value = "C"
        sht.range("p" + str(i)).value = "D"
        sht.range("i" + str(i)).value = maze_question + "<%05dmaze" % (i - 1) + ".png>"
        shutil.copy(file_new + "/" + "%05d" % (i - start_row + 1) + ".png", './final' + "/%05dmaze" % (i - 1) + ".png")
    elif question_type == "star":
        que = lines2[i - start_row].split(",")
        sht.range("j" + str(i)).value = que[0]
        sht.range("l" + str(i)).value = que[1]
        sht.range("n" + str(i)).value = que[2]
        sht.range("p" + str(i)).value = que[3]
        sht.range("i" + str(i)).value = star_question + "<%05dstar" % (i - 1) + ".png>"
        shutil.copy(file_new + "/" + "%05d" % (i - start_row + 1) + ".png", './final' + "/%05dstar" % (i - 1) + ".png")
    else:
        sht.range("j" + str(i)).value = "<%05ddraw_" % (i - 1) + "A.png>"
        sht.range("l" + str(i)).value = "<%05ddraw_" % (i - 1) + "B.png>"
        sht.range("n" + str(i)).value = "<%05ddraw_" % (i - 1) + "C.png>"
        sht.range("p" + str(i)).value = "<%05ddraw_" % (i - 1) + "D.png>"
        sht.range("i" + str(i)).value = draw_question + "<%05ddraw" % (i - 1) + ".png>"
        shutil.copy(file_new + "/" + "%05d" % (i - start_row + 1) + ".png", './final' + "/%05ddrraw" % (i - 1) + ".png")
        shutil.copy(file + "/question/" + str(i - start_row + 1) + "A.png", './final' + "/%05ddrraw" % (i - 1) + "_A.png")
        shutil.copy(file + "/question/" + str(i - start_row + 1) + "B.png", './final' + "/%05ddrraw" % (i - 1) + "_B.png")
        shutil.copy(file + "/question/" + str(i - start_row + 1) + "C.png", './final' + "/%05ddrraw" % (i - 1) + "_C.png")
        shutil.copy(file + "/question/" + str(i - start_row + 1) + "D.png", './final' + "/%05ddrraw" % (i - 1) + "_D.png")
    print(i - start_row + 1)

wb.save()
input("finish")