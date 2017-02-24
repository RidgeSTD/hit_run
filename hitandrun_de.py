import os
import os.path
import sys

hard_code_stuff_lenth = 1600


def operate(in_filepath, out_filepath):
    global finish_size
    global total_size
    in_file = open(in_filepath, "rb")
    out_dir = os.path.dirname(out_filepath)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    out_file = open(out_filepath, "wb")

    in_file.read(hard_code_stuff_lenth)
    while True:
        buff = in_file.read(1048576)
        finish_size += len(buff)
        sys.stdout.write("\r" + str(finish_size) + "/" + str(total_size) + " Bytes finished!")
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

    print('here is to REMOVE the stuff in a file or directory')

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

        for root, dirs, files in os.walk(inputpath):
            for filename in files:
                in_filepath = os.path.join(root, filename)
                out_filepath = os.path.join(outputpath, in_filepath[len(inputpath) + 1:len(in_filepath)])
                operate(in_filepath, out_filepath)
    else:
        print("file detected")
        total_size = os.path.getsize(inputpath)
        out_filepath = os.path.join(outputpath, os.path.basename(inputpath))
        operate(inputpath, out_filepath)

    print("\nThey've been back!")
