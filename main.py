import os
import random
from abc import ABC, abstractmethod

class GenericFile(ABC):
    @abstractmethod
    def get_path(self,file):
        pass
    @abstractmethod
    def get_freq(content:bytes):
        pass


class TextASCII(GenericFile):
    def __init__(self,path_absolut,frecvtente):
        self.path_absolut=path_absolut
        self.frecvente=frecvtente

    def get_path(self):
        return self.path_absolut

    def get_freq(self):
        return self.frecvente

class TextUNICODE(GenericFile):
    def __init__(self,path_absolut,frecvtente):
        self.path_absolut=path_absolut
        self.frecvente=frecvtente

    def get_path(self):
        return self.path_absolut

    def get_freq(self):
        return self.frecvente

class BINARY(GenericFile):
    def __init__(self,path_absolut,frecvtente):
        self.path_absolut=path_absolut
        self.frecvente=frecvtente

    def get_path(self):
        return self.path_absolut

    def get_freq(self):
        return self.frecvente

class BMP(BINARY):
    def __init__(self, path_absolut, frecvtente):
        super().__init__(path_absolut, frecvtente)
        self.width=random.randint(100,200)
        self.height=random.randint(100,200)
        self.bpp=24

    def show_info(self):
        print(self.height,self.width,self.bpp)

class XMLFile(TextASCII):
    def __init__(self, path_absolut, frecvtente):
        super().__init__(path_absolut, frecvtente)
        self.first_tag="<xml>"
    def get_first_tag(self):
        return self.first_tag

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

def get_frecventa(content:bytes):
    freq=[0 for i in range(256)]
    for i in content:
        freq[i]+=1
    return freq

if __name__ == '__main__':
    listFile=[]
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
                    freq=get_frecventa(content)
                    #print(file_path)
                    if isASCII(freq)==1:
                        listFile.append(XMLFile(file_path,freq))
                        print(listFile[-1].get_first_tag())
                    elif(isUNICODE(freq)==1):
                        listFile.append(TextUNICODE(file_path, freq))
                    elif(isBINAR(freq)==1):
                        listFile.append(BMP(file_path, freq))
                        listFile[-1].show_info()
                finally:
                    f.close()
    print(listFile)


