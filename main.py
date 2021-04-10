from utils import perfil as p
from utils import pessoa as pe



perfilList = []


perfilList.append(p.perfil("Metaleiro", [7, 19, 8, 25, 31, 21, 26, 13, 14, 9, 26, 1, 22, 15, 10, 27, 2, 16, 23, 3, 32, 33, 4, 11, 28, 5, 24, 34, 29, 12, 35, 17, 6, 36, 18, 30]))
perfilList.append(p.perfil("Rockeiro", [1, 19, 2, 25, 31, 21, 26, 13, 14, 3, 26, 7, 22, 15, 4, 27, 8, 16, 23, 9, 32, 33, 10, 5, 28, 11, 24, 34, 29, 6, 35, 17, 12, 36, 18, 30]))
perfilList.append(p.perfil("Pagodeiro", [25, 13, 26, 7, 14, 15, 8, 19, 20, 27, 1, 31, 16, 21, 28, 9, 32, 22, 17, 33, 2, 3, 34, 29, 10, 35, 18, 4, 11, 30, 5, 23, 36, 6, 24, 12]))
perfilList.append(p.perfil("Fã de Samba", [25, 13, 26, 1, 14, 15, 2, 19, 20, 27, 7, 31, 16, 21, 28, 3, 32, 22, 17, 33, 8, 9, 34, 29, 4, 35, 18, 10, 5, 30, 11, 23, 36, 12, 24, 6]))
perfilList.append(p.perfil("Fã de Sertanejo", [25, 1, 26, 7, 2, 3, 8, 19, 20, 27, 13, 31, 4, 21, 28, 9, 32, 22, 5, 33, 14, 15, 34, 29, 10, 35, 6, 16, 11, 30, 17, 23, 36, 18, 24, 12]))
perfilList.append(p.perfil("Fã de Eletrônica", [7, 8, 9, 10, 11, 12, 13, 1, 2, 14, 15, 16, 17, 3, 18, 19, 20, 4, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 5, 34, 35, 6, 36]))

print(perfilList)
with open("musicas.txt", 'r') as f:
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

