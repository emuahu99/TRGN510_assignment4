#!/usr/bin/python
import sys
import argparse
import fileinput
import re

from optparse import OptionParser

a_file = open("Homo_sapiens.GRCh37.75.gtf")
lines = a_file.readlines()
thisdict={}
for line in lines:
    splitcolumn_array = re.split('\t',line)
    if "gene" in splitcolumn_array:
        a = re.split(';',splitcolumn_array[8])
        b=re.split(" ",a[1])
        c=re.split(" ",a[0])
        thisdict[c[1].strip("\"")]=b[2].strip("\"")

if len(sys.argv)>2: 
    column = int(sys.argv[1][-1])-1
else:
    column = 1 
my_dict_file= sys.argv[-1]
i=0
file1 = open("expression_analysis.hugo.tsv", "w")
for line in fileinput.FileInput(my_dict_file):
    try:
        i = i+1
        if i ==1:
            file1.write(line)
        if i>1:
            w=re.split(",",line)
            q=re.findall(r'EN.*?\.',w[column],re.I)[0][:-1]
            l=[]
            l.append(w[0])
            l.append(thisdict[q])
            l.append(w[2])
            l.append(w[3])
            l.append(w[4])
            m=l[0]+","+l[1]+","+l[2]+","+l[3]+","+l[4]
            file1.write(m)
    except KeyError:
        continue
file1.close()
