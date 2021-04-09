from utils import perfil as p
from utils import pessoa as pe



perfilList = []


perfilList.append(p.perfil("Front End", [1,2, 3, 5,6,7,8,9,4,10,11,12, 13]))
perfilList.append(p.perfil("Back End", [1,2,5,3,6,7,8,9,4,10,11,12, 13]))

print(perfilList)
with open("perguntas.txt", 'r') as f:
  Lines = f.readlines(  )
  totalLines = len(Lines)

  nome = input("Coloque o seu nome: ")

  pessoa = pe.pessoa(nome)

  for line in Lines:
    line = line.rstrip('\n')
    print(line)
    currValue = int(input(f"Qual a sua ?????? (entre 1 e {totalLines}): "))

    while currValue > totalLines or currValue < 1:
      print("!!!!! <<<<< Numero incorreto >>>>>>!!!!")
      print(line)
      currValue = int(input(f"Qual a sua ?????? (entre 1 e {totalLines}): "))

    while pessoa.appendInRank(currValue) == ValueError:
      print("!!!!! <<<<< Numero já inserido >>>>>>!!!!")
      print(line)
      currValue = int(input(f"Qual a sua ?????? (entre 1 e {totalLines}): "))

    
for i in perfilList:
  pessoa.checkPerfil(i)

print(len(pessoa.rank), pessoa.rank, [x.nome for x in pessoa.perfis]) # Print errado, fazer um mais bonito.

