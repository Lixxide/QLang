from math import *
from random import *
import os
import sys

def tr(xs, ys):
    if xs == 1:
        ys = -1
        xs = 0
        return xs, ys
    elif xs == -1:
        ys = 1
        xs = 0
        return xs, ys
    elif ys == 1:
        ys = 0
        xs = 1
        return xs, ys
    elif ys == 1:
        ys = 0
        xs = -1
        return xs, ys


def tl(xs, ys):
    if xs == 1:
        ys = 1
        xs = 0
        return xs, ys
    elif xs == -1:
        ys = -1
        xs = 0
        return xs, ys
    elif ys == 1:
        ys = 0
        xs = -1
        return xs, ys
    elif ys == -1:
        ys = 0
        xs = 1
        return xs, ys

def interpret(c, w, h):
    x = 0
    y = 0
    xs = 1
    ys = 0
    data = [0] * 10
    noa = 1
    ret_stack = []

    while True:
        try:
            char = c[y][x]
        except:
            char = " "
        try:
            nchr = c[y + ys][x + xs]
        except:
            nchr = " "
        try:
            anchr = c[y + 2 * ys][x + 2 * xs]
        except:
            anchr = " "
        #print([char,nchr,anchr])

        if char == ">":
            xs = 1
            ys = 0
            noa = 1
        elif char == "<":
            xs = -1
            ys = 0
            noa = 1
        elif char == "v":
            xs = 0
            ys = 1
            noa = 1
        elif char == "^":
            xs = 0
            ys = -1
            noa = 1
        elif char == "{":
            data[int(nchr)] = ord(anchr)
            noa = 3
        elif char == "}":
            print(chr(data[int(nchr)]))
            noa = 2
        elif char == "@":
            data[int(nchr)] = ord(input("")[0])
            noa = 2
        elif char == "S":
            data[int(nchr)] = int(anchr)
            noa = 3
        elif char == "#":
            print(data[int(nchr)])
            noa = 2
        elif char == "E":
            data[int(nchr)] = int((input("")))
            noa = 2
        elif char == "i":
            data[int(nchr)] += 1
            noa = 2
        elif char == "d":
            data[int(nchr)] -= 1
            noa = 2
        elif char == "+":
            data[int(nchr)] += data[int(nchr)]
            noa = 3
        elif char == "-":
            data[int(nchr)] -= data[int(anchr)]
            noa = 3
        elif char == "*":
            data[int(nchr)] = data[int(nchr)] * data[int(anchr)]
            noa = 3
        elif char == "/":
            data[int(nchr)] = data[int(nchr)] // data[int(anchr)]
            noa = 3
        elif char == ";":
            if data[int(nchr)] == 0:
                noa = 3
            else:
                noa = 2
        elif char == "?":
            if data[int(nchr)] == data[int(anchr)]:
                noa = 3
            elif data[int(nchr)] > data[int(anchr)]:
                noa = 1
                xs, ys = tl(xs, ys)
            elif data[int(nchr)] < data[int(anchr)]:
                noa = 1
                xs, ys = tr(xs, ys)
        elif char == "=":
            if data[int(nchr)] == ord(anchr):
                noa = 3
            elif data[int(nchr)] > ord(anchr):
                noa = 1
                xs, ys = tl(xs, ys)
            elif data[int(nchr)] < ord(anchr):
                noa = 1
                xs, ys = tr(xs, ys)
        elif char == "N":
            if data[int(nchr)] == 0:
                noa = 3
            elif data[int(nchr)] > 0:
                noa = 1
                xs, ys = tr(xs, ys)
            elif data[int(nchr)] < 0:
                noa = 1
                xs, ys = tl(xs, ys)
        if char == "P":
            px = data[int(nchr)]
            py = data[int(anchr)]
            pc = c[py][px]
            while pc != "§":
                print(pc, end="")
                px += 1
                pc = c[py][px]
            noa = 3
            print("\n")
        elif char == "!":
            if data[int(nchr)] == 0:
                data[int(nchr)] = 1
            else:
                data[int(nchr)] = 0
            noa = 2
        elif char == "I":
            data[1] += 1
            noa = 1
        elif char == "i":
            data[0] += 1
            noa = 1
        elif char == "D":
            data[1] -= 1
            noa = 1
        elif char == "d":
            data[0] -= 1
            noa = 1
        elif char == "w":
            x = data[int(nchr)]
            y = data[int(anchr)]
            noa = 0
        elif char == "s":
            ret_stack.append((x,y))
            x = data[int(nchr)]
            y = data[int(anchr)]
            noa = 0
        elif char == ":":
            coo = ret_stack[-1]
            x = coo[0]
            y = coo[1]
            ret_stack.pop()
            noa = 3
        elif char == "%":
            n = randint(0, 3)
            for i in range(0, n):
                xs, ys = tl(xs, ys)
        elif char == "r":
            new_data = interpret(c,w,h)
            data[0] = new_data[5]
            data[1] = new_data[6]
            data[2] = new_data[7]
            data[3] = new_data[8]
            data[4] = new_data[9]
        elif char == "(":
            zeroth = data[0]
            data.pop(0)
            data.append(zeroth)
            noa = 1
        elif char == "[":
            data.pop(0)
            data.append(0)
            noa = 1
        elif char == ")":
            last = data[-1]
            data.pop()
            data.insert(0, last)
            noa = 1
        elif char == "]":
            data.pop()
            data.insert(0,0)
            noa = 1
        elif char == "x":
            temp = data[int(nchr)]
            data[int(nchr)] = data[int(anchr)]
            data[int(anchr)] = temp
            noa = 3
        elif char == "g":
            data[0] = ord(c[data[int(anchr)]][data[int(nchr)]])
            noa = 3
        elif char == "G":
            data[1] = ord(c[data[int(anchr)]][data[int(nchr)]])
            noa = 3
        elif char == "a":
            c[data[int(anchr)]][data[int(nchr)]] = chr(data[0])
            noa = 3
        elif char == "A":
            data[1] = chr(c[data[int(anchr)]][data[int(nchr)]])
            noa = 3
        if char == "c":
            px = data[int(nchr)]
            py = data[int(anchr)]
            pc = c[py][px]
            cmd = ""
            while pc != "§":
                cmd = cmd + pc
                px += 1
                pc = c[py][px]
            os.system(cmd)
            noa = 3
        if char == "F":
            px = data[0]
            py = data[1]
            pc = c[py][px]
            filename = ""
            while pc != "§":
                filename = filename + pc
                px += 1
                pc = c[py][px]
            if (chr(data[2]) != "d"):
                f = open(filename, chr(data[2]), encoding='utf-8')
            if (chr(data[2]) == "a" or chr(data[2]) == "w"):
                content=""
                px = data[3]
                py = data[4]
                pc = c[py][px]
                while pc != "§":
                    content = filename + pc
                    px += 1
                    pc = c[py][px]
            elif (chr(data[2]) == "r"):
                data[5] = f.read()[data[6]]
            elif (chr(data[2]) == "d"):
                os.remove(filename)
            noa = 1
        elif char == "Q":
            return data
        else:
            noa = 1
        x += noa * xs
        y += noa * ys


if len(sys.argv) != 2:
    print("Usage: python q.py <filename>")
    sys.exit(1)

code_file = sys.argv[1]

try:
    with open(code_file, 'r', encoding='utf-8') as file:
        code = file.read()
except FileNotFoundError:
    print("the file '", code_file, "' doesn't exist")
    sys.exit(1)

code = code.split("\n")
width = len(code[1])
height = len(code)

interpret(code, width, height)
