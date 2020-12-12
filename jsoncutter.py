import json
import os

#10122020200031_200
#just for copy, ignore it
json_list = []
maparray = []
list_num = 0
rline = ''
file = "./" + input("input file name:") 
filemaptxt = file + '/map.txt'
newmaptxt = file + '/newmap.txt'
x = 0
y = 0


if not os.path.exists(file):
    print("ERROR")
    input()
    exit(0)


with open(filemaptxt,"r") as map:
    for i in map.readlines():
        rline = rline + i
        if i.endswith("]]\n"):
            json_list.append(rline)
            print(json_list[list_num])

            list_num += 1
            rline = ''


print(len(json_list))


def check(direction):
    cut = True
    if direction <= 1:
        if direction == 0:
            y = 0
        else:
            y = len(maparray) - 2

        for i in range(len(maparray[0])):
            if maparray[y][i] != '' or maparray[y + 1][i] != '':
                cut = False
                break

        if cut == True:
            if y == 0:
                print("len " + str(len(maparray)))
                for i in range(len(maparray) - 1):
                    maparray[i] = maparray[i + 1]
                del maparray[len(maparray) - 1]
            else:
                del maparray[y + 1]
            print("cut", maparray)
            #input()
            return True
    
    if direction >= 2:
        if direction == 2:
            x = 0
        else:
            x = len(maparray[0]) - 2

        for i in range(len(maparray)):
            if maparray[i][x] != '' or maparray[i][x + 1] != '':
                cut = False
                break

        if cut == True:
            if x == 0:
                print("len " + str(len(maparray[0])))
                for i in range(len(maparray)):
                    for j in range(len(maparray[0]) - 1):
                        maparray[i][j] = maparray[i][j + 1]
                    del maparray[i][len(maparray[0]) - 1]

            else:
                for i in range(len(maparray)):
                    del maparray[i][len(maparray[0]) - 1]
            print("cut", maparray)
            #input()
            return True
    return False
    

def process(): 
    if check(0) or check(1) or check(2) or check(3):#up down left right
        process()


def output():
    with open(newmaptxt, 'a') as map2:
        #for i in range(len(json_list)):
        map2.write(str(json.dumps(maparray)).replace('],','],\n'))
        map2.write("\n\n")


if os.path.exists(newmaptxt):
    os.remove(newmaptxt)


for i in range(len(json_list)):
    del maparray
    maparray = json.loads(json_list[i])
    print(maparray)
    print("No " + str(i + 1))
    print('\n')
    process()
    output()

input("finish")
