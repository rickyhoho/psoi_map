# -*- coding:utf-8 -*-
import os
from os.path import split
import shutil


#12122020160911_200
#just for copy, ignore it
draw = False #important
star = False #important
if draw and star:
    print("ERROR")
    input()
    exit(0)

file = "./" + input("input file name:")
filemap = file + "/map"
filecode = file + "/code"
filequestion = file + "/question"
file_ans = file + "/ans.txt"
dir_remove = file + "/removed"
dir_remove_map = dir_remove + "/map"
dir_remove_code = dir_remove + "/code"
dir_remove_question = dir_remove + "/question"

if draw == True:
    if not os.path.exists(filequestion) or not os.path.exists(filecode):
        print("ERROR")
        input()
        exit(0)
else:
    if not os.path.exists(filemap) or not os.path.exists(filecode):
        print("ERROR")
        input()
        exit(0)


if not os.path.exists(dir_remove):
    os.mkdir(dir_remove)
    os.mkdir(dir_remove_code)
    if draw == True:
        os.mkdir(dir_remove_question)
    else:
        os.mkdir(dir_remove_map)
else:
    print("file created")


def process_ans(input_num, filenum):
    if star == True:
        with open(file + "/question.txt", "r") as f1:
            lines2 = f1.read().splitlines()
            print(lines2)

        with open(dir_remove + '/question.txt', "a") as f2:
            f2.write(lines2[input_num - 1] + "\n")

        with open(file + "/question.txt", "w") as f1:
            for i in range(filenum):
                if i == input_num - 1:
                    continue
                f1.write(lines2[i] + "\n")

    with open(file_ans, "r") as f1:
        lines = f1.read().splitlines()
        print(lines)

    with open(dir_remove + '/ans.txt', "a") as f2:
        f2.write(lines[input_num] + "\n")

    with open(file_ans, "w") as f1:
        for i in range(filenum + 1):
            if i == input_num:
                continue
            f1.write(lines[i] + "\n")


def process(input_num):
    all_file = next(os.walk(filecode))
    filenum = len(all_file[2])

    png_path = "/" + "%05d" % input_num + ".png"
    qpng_path = "/" + str(input_num)

    if draw == True:
            shutil.move(filequestion + qpng_path + "A.png", dir_remove_question + qpng_path + "A.png")
            shutil.move(filequestion + qpng_path + "B.png", dir_remove_question + qpng_path + "B.png")
            shutil.move(filequestion + qpng_path + "C.png", dir_remove_question + qpng_path + "C.png")
            shutil.move(filequestion + qpng_path + "D.png", dir_remove_question + qpng_path + "D.png")
    else:
        shutil.move(filemap + png_path, dir_remove_map + png_path)
    shutil.move(filecode + png_path, dir_remove_code + png_path)

    process_ans(input_num, filenum)

    for i in range(input_num, filenum):
        qpng_path = "/" + str(i)
        qpng_path1 = "/" + str(i + 1)
        png_path = "/" + "%05d" % i + ".png"
        png_path1 = "/" + "%05d" % (i + 1) + ".png"

        if draw == True:
            os.rename(filequestion + qpng_path1 + "A.png", filequestion + qpng_path + "A.png")
            os.rename(filequestion + qpng_path1 + "B.png", filequestion + qpng_path + "B.png")
            os.rename(filequestion + qpng_path1 + "C.png", filequestion + qpng_path + "C.png")
            os.rename(filequestion + qpng_path1 + "D.png", filequestion + qpng_path + "D.png")
        else:
            os.rename(filemap + png_path1, filemap + png_path)
        os.rename(filecode + png_path1, filecode + png_path)#old->new
    print("del " + str(input_num))


def multi_input():
    list1 = []
    start = 0
    end = 0
    find = 0
    while True:
        inp = input("enter show, del 1, 0 or add num or run or single to process:")
        args = inp.split(' ')

        if inp.startswith("del") and not len(args) > 2:
            for i in range(start, end):
                if list1[i] == int(args[1]):
                    list1[i] = 0
                    list1.sort()
                    start += 1
                    find = 1
                    break
            if find == 0:
                print("ERROR:404 not find")
            else:
                find = 0

        elif inp.startswith("run"):
            list1.sort()
            for i in range(end - 1, start - 1, -1):
                process(list1[i])
            return 0
                
        elif inp.startswith("show"):
            list1.sort()
            for i in range(start, end):
                print(str(list1[i]) + ' ')

        elif inp.startswith("single"):
            single_mode()

        elif len(args) < 2:
            if int(inp) == 0:
                return 0
            list1.append(int(inp))
            end += 1


def single_mode():
    while True:
        inputnum = int(input("input number for remove or -1 for multi number mode or 0 to exit:"))
        if inputnum == 0:
            break
        if inputnum == -1:
            multi_input()
            break
        process(inputnum)


multi_input()


with open(dir_remove + "/ans.txt", "r") as f1:
    lines = f1.read().splitlines()

with open(dir_remove + "/ans.txt", "w") as f1:
        for i in range(len(lines) - 1, -1, -1):
            f1.write(lines[i] + "\n")

if star == True:
    with open(dir_remove + "/question.txt", "r") as f1:
        lines = f1.read().splitlines()

    with open(dir_remove + "/question.txt", "w") as f1:
            for i in range(len(lines) - 1, -1, -1):
                f1.write(lines[i] + "\n")


print("finish")
input()
