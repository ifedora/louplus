#!/usr/bin/env python3

def ins(num):
    res = num*(0.08+0.02+0.005+0.06)
    return format(res,".2f")

def self_tax(income):
    instr=income*(0.08+0.02+0.005+0.06)
    tax_part=income-instr-3500
    if tax_part <= 0:
        return "0.00"
    income_tab = [
(80000,0.45,13505),
(55000,0.35,5505),
(35000,0.3,2755),
(9000,0.25,1005),
(4500,0.2,555),
(1500,0.1,105),
(0,0.03,0)
]
    for i in income_tab:
        if tax_part >= i[0]:
            result = tax_part*i[1]-i[2]
            return format(result,".2f")
def after_tax():
    import sys
    if len(sys.argv) != 2:
        print("Parameter Error")
        exit(1)
    try:
        goods = int(sys.argv[1])
    except:
        print("Parameter Error")
    result =goods-float(self_tax(goods))-float(ins(goods))
    print(format(result,".2f"))

if __name__=="__main__":
    after_tax()    

