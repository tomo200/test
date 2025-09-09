# -*- coding: utf-8 --*
def cal_coinn(amout):
    amout=int(amout)
    coin=[500,100,50,10,5,1]
    result={} #辞書型
    sums=0

    for c in coin:
        result[c],amout=divmod(amout,c)
        sums+=result[c]
        
    
    return sums

change=input()
ret=cal_coinn(change)
print(f"{ret}がおつりの数!!")


    


