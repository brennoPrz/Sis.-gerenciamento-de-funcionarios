from Data import *

class Funcionario():
  def __init__(self, id, nome, ano, ocupação, salario):
    self.id = int(id)
    self.nome = nome
    self.ano = int(ano)
    self.ocupação = ocupação
    self.salario = float(salario)
    self.horas = []


  def begin(self):  # Retorna true se validado, false ao contrário
    if len(self.horas) == 0:
      self.horas.append([Data(), -1])
      return True
    elif self.horas[-1][1]!= -1:
      self.horas.append([Data(), -1])
      return True
    else:
      return False

  def end(self):  # # Retorna true se validado, false ao contrário
    if len(self.horas) > 0 and self.horas[-1][1] == -1:
      self.horas[-1][1] = Data()
      return True
    else:
      return False

  def getAttributes(self, all=False):
    if all:
      hours = []
      for pair in self.horas:
        if pair[1] != -1:
          hours.append([pair[0].getAttributes(), pair[1].getAttributes()])
      
      return [self.id, self.nome, self.ano, self.ocupação, self.salario, hours]
    else:
      return [self.id, self.nome, self.ano, self.ocupação, self.salario]
    
  def getAttributesDict(self, all=False):
    if all:
      hours = []
      for pair in self.horas:
        if pair[1] != -1:
          hours.append([pair[0].getAttributes(), pair[1].getAttributes()])
      
      return {'ID':self.id, 'Name':self.nome, 'Birth Year':self.ano, 'ocupação':self.ocupação, 'Wage':self.salario, 'Working hours':hours}
    else:
      return {'ID':self.id, 'Name':self.nome, 'Birth Year':self.ano, 'ocupação':self.ocupação, 'Wage':self.salario}
      