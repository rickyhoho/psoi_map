# -*- coding:utf-8 -*-
import os
from os.path import split
import shutil


file = "./" + input("input file name:")
filemap = file + "/map"
filecode = file + "/code"
dir_remove = file + "/removed"
dir_remove_code = dir_remove + "/code"
dir_remove_map = dir_remove + "/map"
star = False #important


if not os.path.exists(filemap) or not os.path.exists(filecode):
    print("ERROR")
    input()
    exit(0)


if not os.path.exists(dir_remove):
    os.mkdir(dir_remove)
    os.mkdir(dir_remove + "/map")
    os.mkdir(dir_remove + "/code")
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
            for i in range(filenum + 1):
                if i == input_num - 1:
                    continue
                f1.write(lines2[i] + "\n")

    with open(file + "/ans.txt", "r") as f1:
        lines = f1.read().splitlines()
        print(lines)

    with open(dir_remove + '/ans.txt', "a") as f2:
        f2.write(lines[input_num] + "\n")

    with open(file + "/ans.txt", "w") as f1:
        for i in range(filenum + 1):
            if i == input_num:
                continue
            f1.write(lines[i] + "\n")


def process(input_num):
    all_file = next(os.walk(filemap))
    filenum = len(all_file[2])

    png_path = "/" + "%05d" % input_num + ".png"
    shutil.move(filemap + png_path, dir_remove_map + png_path)
    shutil.move(filecode + png_path, dir_remove_code + png_path)

    process_ans(input_num, filenum)
    for i in range(input_num, filenum):
        png_path = "/" + "%05d" % i + ".png"
        png_path1 = "/" + "%05d" % (i + 1) + ".png"

        os.rename(filemap + png_path1, filemap + png_path)
        os.rename(filecode + png_path1, filecode + png_path)#old->new


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
            input()
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


with open(file + "/ans.txt", "r") as f1:
    lines = f1.read().splitlines()

with open(file + "/ans.txt", "w") as f1:
        for i in range(len(lines) - 1, -1, -1):
            f1.write(lines[i] + "\n")
            
if star == True:
    with open(file + "/question.txt", "r") as f1:
        lines = f1.read().splitlines()

    with open(file + "/question.txt", "w") as f1:
            for i in range(len(lines) - 1, -1, -1):
                f1.write(lines[i] + "\n")


print("finish")
input()
