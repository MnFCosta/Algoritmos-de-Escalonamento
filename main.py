#variáveis
avg_TAT = 0
avg_WT = 0
var = 0
ct = []
tat = []
wt = []

#lê arquivo como input
input = open("input.txt").readlines()
np = int(input[0])
algo = input[1]
id_list = []
AT_list = []
BT_list = []

#Algoritmos
def FCFS():
    for i in range(np):
        if id_list[i] == 0:
            var = AT_list[i] + BT_list[i]
            ct.append(var)
        else:
            var = var + BT_list[i]
            ct.append(var)

def SJF():
    print("SJF")

def RR():
    print("RR")




#Atribui Id, AT e BT a cada processo
for i in range(np):
    id = int(input[i+(2+i)+i])
    id_list.append(id)
    at = int(input[i+(3+i)+i])
    AT_list.append(at)
    bt = int(input[i+(4+i)+i])
    BT_list.append(bt)



# Calcula o CT
if algo.strip() == "FCFS":
    FCFS()
if algo.strip() == "SJF":
    SJF()
else:
    RR()



# Calcula o TAT e o WT
for i in range(np):
    tat.append(ct[i] - AT_list[i])
    wt.append(tat[i] - BT_list[i])

#Faz output do resultado do algoritmo
output = open("output.txt", 'w')

#TABELA DE PROCESSOS
for i in range(np):
    text = f"Processo {id_list[i]}: AT = {AT_list[i]} BT = {BT_list[i]} CT = {ct[i]} TAT = {tat[i]} WT = {wt[i]}\n"
    avg_TAT = avg_TAT + tat[i]
    avg_WT = avg_WT + wt[i]
    output.write(text)

#TAT E WT MÉDIO
avg_TAT = avg_TAT/np
avg_WT = avg_WT/np
tat = f"\nTempo médio no sistema: {avg_TAT}\n"
wt = f"Tempo médio de espera: {avg_WT}\n\n"
output.write(tat)
output.write(wt)


#GRÁFICO DE GANT
output.write("GRÁFICO DE GANT:")
space = f"\n"
output.write(space)
output.write(space)
for i in range(np):
    gantOn = f"#" * BT_list[i]
    gantOff = f"-" * ct[i-1]
    if i == 0:
        output.write(f"P{i}: ")
        output.write(gantOn)
        output.write(space)
    else:
        output.write(f"P{i}: ")
        output.write(gantOff)
        output.write(gantOn)
        output.write(space)

