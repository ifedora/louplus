#!/usr/bin/env python3

import sys

try:
    gongzi = int(sys.argv[1])
    if len(sys.argv) !=2:
        raise ValueError()
    pre_tax = gongzi-3500
    if pre_tax>0 and pre_tax <= 1500:
        tax=format((pre_tax*0.03 - 0),".2f")
        print (tax)
    elif pre_tax >1500 and pre_tax<=4500:
        tax = format((pre_tax*0.1 - 105),".2f")
        print (tax)
    elif pre_tax >4500 and pre_tax <=9000:
        tax = format((pre_tax*0.2 - 555),".2f")
        print (tax)
    elif pre_tax > 9000 and pre_tax<=35000:
        tax = format((pre_tax*0.25 - 1005),".2f")
        print (tax)
    elif pre_tax >35000 and pre_tax<=55000:
        tax = format((pre_tax*0.30 - 2755),".2f")
        print (tax)
    elif pre_tax >55000 and pre_tax<=80000:
        tax = format((pre_tax*0.35 - 5505),".2f")
        print (tax)
    elif pre_tax <= 0:
        tax = format(0,".2f")
        print (tax)
    else:
        tax = format((pre_tax*0.45 - 13505),".2f")
        print (tax)
except:
    print("Parameter Error")
