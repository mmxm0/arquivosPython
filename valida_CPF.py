def validaCPF(cpf):
    cpf = cpf.replace("\n","")
    lista_CPF = []
    for i in cpf:
        lista_CPF.append(int(i))
    dig2 = lista_CPF.pop(-1)
    dig1 = lista_CPF.pop(-1)
    soma1=0
    for digito,peso in zip(lista_CPF,range(10,1,-1)):
        soma1 +=digito*peso
    digverificador1 = soma1%11
    digverificador1 = 11-digverificador1
    if digverificador1 >9:
        digverificador1 = 0
    lista_CPF.append(digverificador1)
    soma2=0
    for digito,peso in zip(lista_CPF,range(11,1,-1)):
        soma2 +=digito*peso
    digverificador2 = soma2%11
    digverificador2 = 11-digverificador2
    if digverificador2 >9:
        digverificador2 = 0
    if dig2==digverificador2 and dig1==digverificador1:
        return True
    else:
        return False
