from array import array
from tkinter import filedialog
import pandas as pd
 

def getReservados():
    # read by default 1st sheet of an excel file
    dataframe1 = pd.read_excel('reservados.xlsx')
    reservadas = dataframe1['reservadas']
    return reservadas

def getDataTxt():
    array = []
    getTxt = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
    with open(getTxt) as f:
        for line in f:
            array.append(line.strip())
    return array            

def getDeclarations():
    arrayDatos = []
    for line in getDataTxt():
        if line.startswith("int") or line.startswith("String") or line.startswith("float") or line.startswith("double")  or line.startswith("char") or line.startswith("boolean"):
            if line.endswith(";"):
                i = line.split( )[1]
                arrayDatos.append(i.split(";")[0])
            else:
                arrayDatos.append(line.split( )[1])
            
            
    return arrayDatos

def getPracticas():
    dataframe1 = pd.read_excel('buenasPracticas.xlsx')
    declaraciones = dataframe1['declaracion']
    return declaraciones

if __name__ == "__main__":
    print(getDeclarations())