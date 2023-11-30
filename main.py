p = int(input("请输入公开的质数p:"))
g = int(input("请输入p的原根g:"))
KA = int(input("请输入A传给B的公钥KA:"))
KB = int(input("请输入B传给A的公钥KB:"))
for i in range(p):
    # print("try i="+str(i))
    if (pow(g, i) - KA) % p == 0:
        XA = i
        # print("find XA="+str(i))
        break
for i in range(p):
    # print("try i="+str(i))
    if (pow(g, i) - KB) % p == 0:
        XB = i
        # print("find XB="+str(i))
        break
K1 = pow(KB, XA) % p
K2 = pow(KA, XB) % p
if(K1==K2):
    print("A的私钥为:", XA)
    print("B的私钥为:", XB)
    print("A和B交换的密钥为：", K1)
