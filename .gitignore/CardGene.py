import sys
import random
import time
import os
time.sleep(1)
print"""
+=====================+=====================+
|           CODED BY : AbdXSlayer69         |
|           E-mail : As8apple@gmail.com     |
+=====================+=====================+
\n"""
time.sleep(1)
def cardgenerator():
    binn = raw_input("Enter Bin (Ex :483745) : ")
    mm = raw_input("Month (MM) : ")
    yy = raw_input("Year (YY) : ")
    i=1
    for i in range(0,100):
            i=i+1
	    geneccv = random.randint(100,999)
	    genenum = random.randint(1000000000,9999999999)
	    creditcard = (binn,genenum)
	    creditcardstr = "%s%s"%(creditcard)
	    all = creditcardstr,"|",mm,"|",yy,"|",geneccv
	    allstring = "%s%s%s%s%s%s%s"%(all)
	    print allstring

cardgenerator()
	
