import os

__path__ = 'C:/Users/rosen/Downloads/Notebooks-master/Notebooks-master/week05/images'


def func():
    returnList = []
    for entry in os.listdir(__path__):
        # print(entry)
        if entry[:4] == "deep":
            returnList.append(entry)
    return returnList


# Checking whether the specified path exists
isExisting = os.path.exists(__path__)
if isExisting:
    print(func())
else:
    print("path does not exist")
