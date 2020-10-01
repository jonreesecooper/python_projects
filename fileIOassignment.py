import os
import time

fPath = 'C:\\python_projects\\' # setting fPath as my actual file path

def checking(): # function to list full directory from fPath
    check = os.listdir(path = fPath)
    return check

def timestamp():
    check = checking()
    abPath = os.path.join(fPath,check[0]) # set abPath to join fPath and file extension from index 0 of check
    mod_time = os.path.getmtime(abPath) # mod_time gets time stamp for abPath
    local_time=time.ctime(mod_time) # local_time converts mod_time to current time
    print(abPath, local_time) #prints full path from index 0 of check and current time for last time modified

timestamp()

# this will print out the first index from the full directory from fPath with the time stamp of when it was last modified
# now I need to figure out how to parse through check, find each file that ends in .txt, then print that
# with the appropriate time stamp


