import xmltodict
with open("33241147723162000200570030000042621000042624.xml",'rb') as arquivo:
    dictionari = xmltodict.parse(arquivo)
emitente = dictionari['cteProc']['CTe']['infCte']['emit']
registro ="70"

registro = registro + emitente['CNPJ'] + emitente["IE"]
print(len(registro))
for i in range(0,13):
    if len(registro) < 31:
        registro = registro + ' '
        print(registro + str(i))
print(len(registro))
data_emi =  dictionari['cteProc']['CTe']['infCte']['ide']['dhEmi'].replace('-','')[:8]
registro = registro + data_emi
uf = dictionari['cteProc']['CTe']['infCte']['ide']['UFEnv']
registro = registro + uf
modelo = dictionari['cteProc']['CTe']['infCte']['ide']['mod']
registro = registro + modelo
serie = dictionari['cteProc']['CTe']['infCte']['ide']['serie']
registro = registro + serie
numero = dictionari['cteProc']['CTe']['infCte']['ide']['nCT']
num=''
if len(numero) < 6:
    for i in range(0, (6-len(numero))):
        num = num + "0"
    num = num+ numero
registro = registro + "  "+ num
cfop_n = dictionari['cteProc']['CTe']['infCte']['ide']['CFOP']

if cfop_n[0] == "6":
    cfop_n = str(cfop_n).replace("6","2")
else:
    if cfop_n[0] == "5":
        cfop_n = str(cfop_n).replace("5", "1")
registro = registro+cfop_n
esq = ''
preco = dictionari['cteProc']['CTe']['infCte']['vPrest']['vRec'].replace(".","")
if len(preco) < 12:
    for i in range(0, (12-len(preco))):
        esq = esq + "0"
    preco = esq+ preco
registro = registro + preco
#Ainda a confirmar se é desta forma que gera este campo do sintegra

imposto = dictionari['cteProc']['CTe']['infCte']['vPrest']['vRec'].replace(".","")
if len(imposto) < 12:
    for i in range(0, (12-len(imposto))):
        esq = esq + "0"
    imposto = esq+ imposto
registro = registro + imposto
print(registro)

