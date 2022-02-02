import urllib.request as ul
from os import path
from fpdf import FPDF
import re
import os

judul = ""

def checkSource(link):

    #if not path.isfile("source.txt"):

        data_path = "source.txt"

        npath = open(data_path,'w+')

        get = ul.urlopen(link)

        content = get.read().decode()

        get.close()

        npath.write(content)

def getImage(link,i):

    if not path.exists("pdfimg"):

        os.mkdir("pdfimg")

    filename = link.split("/")[len(link.split("/"))-1]

    imgdir = "pdfimg/"+i

    if not path.exists(imgdir):

        get = ul.urlretrieve(link.replace(" ","%20"),imgdir)

def sortImg(path):

    fpdf = FPDF("L","mm",(200,300))

    listd = os.listdir(path)

    nlist = []

    for z in listd:

        zx = z.replace('.JPG','')

        nlist.append(zx)

    toPdf(sorted([int(x) for x in nlist]))

def cleanImg():

    imgls = os.listdir("pdfimg/")

    for a in imgls:

        os.remove("pdfimg/"+a)

def toPdf(plist):

    fpdf = FPDF("L","mm",(200,300))

    for img in plist:

        fpdf.add_page()

        fpdf.image("pdfimg/"+str(img)+".JPG",0,0,300,200)

    fpdf.output(judul+".pdf", "F")

    

def readyTo(link):

    if path.exists("pdfimg"):

        cleanImg()

    #os.mkdir("pdfimg")

    checkSource(link)

    file = open("source.txt",'r').read()

    spl1 = file.split("https://camp404.com/images/uploadcourse/uploaddetail")

    url = "https://camp404.com/images/uploadcourse/uploaddetail/"

    idx = 0

    for i in range(len(spl1)):

        idx = idx + 1

        if i % 2 == 0:

            continue

        spl2 = re.split("JPG",spl1[i],flags=re.IGNORECASE)
        if opt == 5:
            url1 = url+spl2[0]+"jpg"
        else:
            url1 = url+spl2[0]+"JPG"
        #print(url1)
        getImage(url1,str(i)+".JPG")

    sortImg("pdfimg")

    if path.exists("pdfimg"):

        cleanImg()

if __name__ == '__main__':

    print("1. Download all")

    print("2. Bekerja dengan Python")

    print("3. Pengolahan data")

    print("4. Dasar machine learning")
    print("5. Restfull api laravel")

    print("")

    opt = int(input("Ketikan angka sesui yang diinginkan>> "))

    #link = "https://raw.githubusercontent.com/khenop/ppt-maker/master/data.json?token=GHSAT0AAAAAABQ6LVMSDMXGKGS2OAYCMWYYYPYY4KQ"

    link1 = "https://raw.githubusercontent.com/khenop/pdfMaker404/master/source1.txt"

    link2 = "https://raw.githubusercontent.com/khenop/pdfMaker404/master/source2.txt"

    link3 = "https://raw.githubusercontent.com/khenop/pdfMaker404/master/source3.txt"
    link4 = "https://raw.githubusercontent.com/khenop/pdfMaker404/master/source4.txt"

    if opt == 2:
        print("Waiting to make pdf")
        judul = "Bekerja dengan Python"
        readyTo(link1)
        print("pdf generate success as: "+judul+".pdf")

    elif opt == 3:
        judul = "Pengolahan data"
        readyTo(link2)
        print("pdf generate success as: "+judul+".pdf")

    elif opt == 4:
        judul = "Dasar machine learning"
        readyTo(link3)
        print("pdf generate success as: "+judul+".pdf")

    elif opt == 5:
        judul = "Restful API Laravel"
        readyTo(link4)
        print("pdf generate success as: "+judul+".pdf")

    else:
        print("Waiting to make pdf")
        judul = "Bekerja dengan Python"
        readyTo(link1)
        print("pdf generate success as: "+judul+".pdf")
        judul = "Pengolahan data"
        readyTo(link2)
        print("pdf generate success as: "+judul+".pdf")
        judul = "Dasar Machine learning"
        readyTo(link3)
        print("pdf generate success as: "+judul+".pdf")
        judul = "Restful API Laravel"
        readyTo(link4)
        print("pdf generate success as: "+judul+".pdf")

