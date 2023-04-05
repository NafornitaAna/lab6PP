import os

def get_freq(content:bytes):
    freq=[0 for i in range(256)]
    for i in content:
        freq[i]+=1
    return freq

def isASCII(freq):
    mx = max(freq)
    mn = min(freq)
    average = (mn + mx) / 2
    ok = 1
    for i in [9, 10, 13] + list(range(32, 128)):
        if freq[i] < average:
            ok = 0
    for i in list(range(0, 9)) + [11, 12, 14] + list(range(15, 32)) + list(range(128, 256)):
        if freq[i] > average:
            ok = 0
    return ok

def isUNICODE(freq):
    suma=sum(freq)
    if(freq[0]==30*suma/100):
        return 1
    return 0

def isBINAR(freq):
    mx = max(freq)
    mn = min(freq)
    average = (mn + mx) / 2
    for i in range(0,256):
        if abs(freq[i]-average)>average*40/100:
            return 0
        return 1

if __name__ == '__main__':
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    for root, subdirs, files in os.walk(ROOT_DIR):
        for file in os.listdir(root):
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                # deschide fișierul spre acces binar
                f = open(file_path, 'rb')
                try:
                    # în content se va depune o listă de octeți
                    content = f.read()
                    freq=get_freq(content)
                    #print(file_path)
                    if isASCII(freq)==1:
                        print("ASCII")
                    elif(isUNICODE(freq)==1):
                        print("UNICODE")
                    elif(isBINAR(freq)==1):
                        print("BINAR")
                finally:
                    f.close()


