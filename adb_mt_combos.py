
# run this in the same dir as adb.exe
# this might take 23k days ... 
# TODO: fix `adb shell input` issue, not parsing command correctly

from itertools import product 
from sys import argv
from os.path import dirname, realpath 
import subprocess 

length = int(argv[1])
all_chars = "ZE0123456789ABCDFGHIJKLMNOPQRSTUVWXY"

def compute_codes(length):
    return product(all_chars, repeat=length) 

def format_code_tuple(tup):
    f"{''.join(tup)}\n"

def has_passed(stdout):
    return 'invalid.' not in stdout

def try_code(code):
    cmd = f'./adb.exe shell input keyboard text "{code}"; ./adb.exe shell input touchscreen tap 573.0 510.0'
    try:
        p1=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, env={'PATH': get_path()})
        p1.communicate() # block till return 
    except Exception as e:
        print(e)

def tap_got_it():
    cmd = './adb.exe shell input touchscreen tap 360.0 788.0;'
    try:
        p1=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, env={'PATH': get_path()})
        p1.communicate() # block till return 
    except Exception as e:
        print(e)

def get_path():
    return dirname(realpath(__file__))

def brute_force():
    codes = compute_codes(length)
    finished = False 
    while not finished:
        try: 
            code = format_code_tuple(codes.__next__())
            try_code(code)
            print(get_path())
            dump_cmd = 'adb exec-out uiautomator dump /dev/tty | awk \'{gsub("UI hierchary dumped to: /dev/tty", "");print}\''.split()
            dump = subprocess.run(dump_cmd, env={'PATH': get_path()}) # run in current dir
            finished = has_passed(dump.stdout)
            if not finished:
                tap_got_it()
            else:
                print(f"SUCCESS: {code}")

        except StopIteration as e:
            print(e)
            print("NO MATCHING CODES FOUND")
            return
            
# brute_force()

# dump_cmd = 'adb exec-out uiautomator dump'.split()
# print(dump_cmd)
# dump = subprocess.run(dump_cmd, env={'PATH': get_path()}) # run in current dir
# print(dump.stdout)