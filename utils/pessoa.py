from utils import inverMerge
from utils import perfil as p


class pessoa:
  def __init__(self, nome:str) -> None:
    self.nome = nome
    self.rank = []
    self.perfis = []

  def appendInRank(self, valor:int):
    """
    Adiciona um novo valor no rank de musicas.
    """
    if valor in self.rank:
      return ValueError

    self.rank.append(valor)


  def checkPerfil(self, perfil: p.perfil):
    """
    Faz o check do rank feito pela pessoa, e o perfil, que for passado.
    """

    # Copias dos ranks para que não tenha um ordenamento do rank.
    perfilRank = perfil.rank.copy()
    myRankcp = self.rank.copy()

    # Inversões.
    perfilInversao = inverMerge.inversoes(perfilRank.copy(), len(perfilRank))
    myRankInversao = inverMerge.inversoes(myRankcp.copy(), len(myRankcp))

    myRankcp.sort()
    perfilRank.sort()
    
    perfilAndMyInversoes = inverMerge.inversoes(myRankcp + perfilRank, len(perfilRank) + len(myRankcp))

    # A inversão entre A e B, decidimos fazer sendo resultante de: inversoes([A, B]) - (inversoes(A) + inversoes(B))
    totalInversoes = perfilAndMyInversoes - (perfilInversao + myRankInversao)

    self.perfis.append((perfil, totalInversoes))

    self.perfis.sort(key=lambda x: x[1]) # Ordenamento da menor quantidade de inversões

    # print(self.perfis)
    
