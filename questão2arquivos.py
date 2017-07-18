from valida_CPF import *

arq = open("listaCPFs.txt","r")
arq2 = open("CPFsValidos.txt","w")
cpfs = arq.read()
cpfs = cpfs.split("\n")
cpfs.pop(-1)
for i in cpfs:
    if validaCPF(i):
        arq2.write(i+"\n")
arq.close()
arq2.close()
