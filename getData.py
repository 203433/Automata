from array import array
from tkinter import filedialog
import pandas as pd


def getDataTxt():
    array = []
    arrayCopy = []
    getTxt = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
    with open(getTxt) as f:
        for line in f:
            x = (line.strip())
            c = x.split()
            print (c)
            for j in c:
                print (j)
                if j != ' ':
                    array.append(j)

    return array            

def getPracticas():
    dataframe1 = pd.read_excel('buenasPracticas.xlsx')
    declaraciones = dataframe1['declaracion']
    return declaraciones

if __name__ == "__main__":
    print(getDataTxt())