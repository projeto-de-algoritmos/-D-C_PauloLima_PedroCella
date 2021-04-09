from utils import inverMerge
from utils import perfil as p


class pessoa:
  def __init__(self, nome:str) -> None:
    self.nome = nome
    self.rank = []
    self.perfis = []

  def appendInRank(self, valor:int):
    if valor in self.rank:
      return ValueError

    self.rank.append(valor)


  def checkPerfil(self, perfil: p.perfil):

    if len(self.perfis):
      perfilRank = perfil.rank.copy()
      myRankcp = self.rank.copy()
      lastPerfilRank = self.perfis[-1].rank.copy()

      lastInversao = inverMerge.inversoes(myRankcp + lastPerfilRank, len(lastPerfilRank) + len(myRankcp))
      currInversao = inverMerge.inversoes(myRankcp + perfilRank,     len(perfilRank)     + len(myRankcp))
      print(lastInversao, currInversao)
      
      if currInversao == lastInversao:
          self.perfis.append(perfil)
      
      elif currInversao < lastInversao:
        self.perfis = [perfil]

    else:
      self.perfis = [perfil]

    
