logo_path = 'C:/Users/rosen/Downloads/Notebooks-master/Notebooks-master/week05/resources/logo.jpg'


def read_binary_file(filename):
    with open(filename, "rb") as f:
        x = ''
        while chunk := f.read():
            i = 0
            mone = 0
            while i < len(chunk):
                if (str(chunk)[i] >= 'a' and str(chunk)[i] <= 'z'):
                    x = x + str(chunk)[i]
                    mone = mone+1
                elif str(chunk)[i] == '!':
                    x = x + '!'
                    mone = mone+1
                else:
                    mone =0
                    x = ''
                if mone >= 5 and x[len(x)-1] == '!':
                    yield x
                    x = ''
                i = i + 1


for i in read_binary_file(logo_path):
    print("The message is:  " + i)
