import os
import time

fPath = 'C:\\python_projects\\' # setting fPath as my actual file path

def checking(): # function to list full directory from fPath
    check = os.listdir(path = fPath)
    return check


def timestamp():
    check = checking()
    i = 0
    while i < len(check):
        abPath = os.path.join(fPath,check[i]) # set abPath to join fPath and file extension from index of check
        mod_time = os.path.getmtime(abPath) # mod_time gets time stamp for abPath
        local_time=time.ctime(mod_time) # local_time converts mod_time to current time
        print(abPath, local_time) #prints full path from index of check and current time for last time modified
        i += 1 # increase index by 1 and repeat while loop
timestamp()



