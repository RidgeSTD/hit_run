import os
import os.path
import sys

hard_code_token = "winlandiano"
hard_code_stuff_lenth = 1600



def operate(in_filepath, out_filepath, stuff):
    global finish_size
    global total_size
    in_file = open(in_filepath, "rb")
    out_dir = os.path.dirname(out_filepath)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    out_file = open(out_filepath, "wb")
    out_file.write(stuff)
    while True:
        buff = in_file.read(1048576)
        finish_size += len(buff)
        sys.stdout.write("\r"+str(finish_size) + "/" + str(total_size)+" Bytes finished!")
        sys.stdout.flush()
        out_file.write(buff)
        if len(buff) != 1048576:
            break
    in_file.close()
    out_file.close()


def cal_total_size(file_path):
    global total_size
    total_size += os.path.getsize(filename)


if __name__ == '__main__':
    total_size = 0
    finish_size = 0

    print('here is to ADD some stuff in a file or directory')
    buf1 = bytearray(source=hard_code_token, encoding="utf8")
    stuff = bytearray(hard_code_stuff_lenth)
    for i in range(0, min(len(buf1), len(stuff))):
        stuff[i] = buf1[i]

    inputpath = input("input file path=>")
    outputpath = input("input output path(without name!)=>")
    if not (os.path.isdir(inputpath) or os.path.isfile(inputpath)):
        print('no file or directory found!')
        exit()

    if os.path.isdir(inputpath):
        print("directory detected")
        print("calculating directory size...")
        for root, dirs, files in os.walk(inputpath):
            for filename in files:
                cal_total_size(os.path.joinroot, filename)

        print("total size = %d", total_size)

        for root, dirs, files in os.walk(inputpath):
            for filename in files:
                in_filepath = os.path.join(root, filename)
                out_filepath = os.path.join(outputpath, in_filepath[len(inputpath)+1:len(in_filepath)])
                operate(in_filepath, out_filepath, stuff)
    else:
        print("file detected")
        total_size = os.path.getsize(inputpath)
        out_filepath = os.path.join(outputpath, os.path.basename(inputpath))
        operate(inputpath, out_filepath, stuff)

    print("\nhitted and run away!")