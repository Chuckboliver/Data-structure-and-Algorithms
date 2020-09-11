import os
def diskUsage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childPath = os.path.join(path,filename)
            total += diskUsage(childPath)
    print(f"{total:<7}",path)
    return total

diskUsage("E:")