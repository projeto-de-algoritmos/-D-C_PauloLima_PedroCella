from utils import perfil as p
from utils import pessoa as pe


# Perfis cadastrados.
perfilList = []
perfilList.append(p.perfil("Rock Metal", [7, 19, 8, 25, 31, 21, 26, 13, 14, 9, 26, 1, 22, 15, 10, 27, 2, 16, 23, 3, 32, 33, 4, 11, 28, 5, 24, 34, 29, 12, 35, 17, 6, 36, 18, 30]))
perfilList.append(p.perfil("Rock", [1, 19, 2, 25, 31, 21, 26, 13, 14, 3, 26, 7, 22, 15, 4, 27, 8, 16, 23, 9, 32, 33, 10, 5, 28, 11, 24, 34, 29, 6, 35, 17, 12, 36, 18, 30]))
perfilList.append(p.perfil("Pagode", [25, 13, 26, 7, 14, 15, 8, 19, 20, 27, 1, 31, 16, 21, 28, 9, 32, 22, 17, 33, 2, 3, 34, 29, 10, 35, 18, 4, 11, 30, 5, 23, 36, 6, 24, 12]))
perfilList.append(p.perfil("Samba", [25, 13, 26, 1, 14, 15, 2, 19, 20, 27, 7, 31, 16, 21, 28, 3, 32, 22, 17, 33, 8, 9, 34, 29, 4, 35, 18, 10, 5, 30, 11, 23, 36, 12, 24, 6]))
perfilList.append(p.perfil("Sertanejo", [25, 1, 26, 7, 2, 3, 8, 19, 20, 27, 13, 31, 4, 21, 28, 9, 32, 22, 5, 33, 14, 15, 34, 29, 10, 35, 6, 16, 11, 30, 17, 23, 36, 18, 24, 12]))
perfilList.append(p.perfil("Eletrônica", [7, 8, 9, 10, 11, 12, 13, 1, 2, 14, 15, 16, 17, 3, 18, 19, 20, 4, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 5, 34, 35, 6, 36]))


print("\n\n\nBem vindo ao GG (Great guess), onde a você vai ter uma lista de musicas e ter que  colocar um rank para cada musica, para que possamos, tentar descobrir o seu perfil musical!!!")
print("OBS:. Caso você não tenha escutado alguma musica, fizemos uma playlist no spotify. (https://open.spotify.com/playlist/7IgnJCnLnhLo1DkkNOIoXN?si=4a13a056f74144fe)\n\n\n")
input("Aperte enter para continuar...")



# Leitura do input para cada musica listada, no arquivo de Musicas.
with open('Musicas.txt', 'r') as f:
  Lines = f.readlines()
  totalLines = len(Lines)

  print("As musicas, cadastradas são: \n")
  for line in Lines:
    print(line, end="")

  print("\n\nDe uma pequena olhada nas musica para poder ter uma noção de como vai ficar o seu rank de musicas.")
  input("Aperte enter para continuar...")
  nome = input("Coloque o seu nome: ")

  pessoa = pe.pessoa(nome)

  for line in Lines:
    print("")
    print(line, end="")
    currValue = int(input(f"No rank de 1 até {totalLines}, onde você colocaria essa musica? "))

    while currValue > totalLines or currValue < 1:
      print("!!!!! <<<<< Numero incorreto >>>>>>!!!!")
      print(line)
      currValue = int(input(f"No rank de 1 até {totalLines}, onde você colocaria essa musica? "))

    while pessoa.appendInRank(currValue) == ValueError:
      print("\n\n!!!!! <<<<< Numero já inserido >>>>>>!!!!")
      print("Os numeros já inseridos, foram: \n")
      pessoa.rank.sort()
      print(", ".join([str(x) for x in pessoa.rank]), end="\n\n")
      print(line)
      currValue = int(input(f"No rank de 1 até {totalLines}, onde você colocaria essa musica? "))


# Faz o calculo de inversoes para cada perfil cadastrado.
for i in perfilList:
  pessoa.checkPerfil(i)


# Print Final.
print("\n\nInversoes: ")

for i in pessoa.perfis:
  print("{} - {:.2f}% ({} inversões).".format(i[0].nome, float(10000/i[1]), i[1]))


# Contagem dos casos onde deu o mesmo numero de inversões.
mesmosCasos = [x[1] for x in pessoa.perfis].count(pessoa.perfis[0][1])

if mesmosCasos > 1:
  print("\n\nCom isso sabemos que de acordo com as musicas apresentadas, você tem um perfil de que gosta dos estilos de musica:")
else:
  print("\n\nCom isso sabemos que de acordo com as musicas apresentadas, você tem um perfil de que gosta do estilo de musica:")
print(", ".join([x[0].nome for x in pessoa.perfis[0:mesmosCasos]]))
