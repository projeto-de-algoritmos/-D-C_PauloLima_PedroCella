from utils import perfil as p
from utils import pessoa as pe



perfilList = ["Desenvolvedor Web", "Desenvolvedor Mobile", "DevOps", "Scrum Master"]


perfilList.append(p.perfil("Desenvolvedor Web", [14, 1, 2, 3, 13, 4, 5, 12, 11, 10, 9, 8, 7, 6]))
perfilList.append(p.perfil("Desenvolvedor Mobile", [12, 1, 13, 12, 2, 3, 11, 10, 9, 8, 7, 6, 4, 5]))
perfilList.append(p.perfil("DevOps", [1, 2, 14, 13, 12, 11, 10, 3, 9, 4, 8, 5, 7, 6]))
perfilList.append(p.perfil("Scrum Master", [1, 14, 13, 12, 11, 10, 9, 2, 3, 4, 5, 8, 7, 6]))

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

