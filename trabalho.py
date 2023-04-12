# RAD PYTHON - Daniel Silva de Lima 202108028576 | Henrique Gomes 202108637823

import sys
from os import path

dirname = path.dirname(__file__)

def readFile(filename):
  try:
    filepath = path.join(dirname, 'in', filename)
    with open(filepath) as file:
        data = file.readlines()
        return data
  except:
    print('Falha ao ler arquivo!')

def criarArquivoDiciplina(filename, data): 
  try:
    with open(path.join(dirname, 'out', filename), 'w') as file:
      for line in data:
        file.write(f'{line[0]};{line[1]}')
        file.write('\n')
  except :
    print('Falha ao criar o arquivo!')

def criarArquivoMedias(filename, data): 
  try:
    with open(path.join(dirname, 'out', filename), 'w') as file:
      for line in data:
        av1 = float(f'{line[3][0:2]}.{line[3][2:3]}')
        av2 = float(f'{line[3][3:5]}.{line[3][5:6]}')
        av3 = float(f'{line[3][6:8]}.{line[3][8:9]}')
        file.write(f'{line[0]};{line[1]};{av1};{av2};{av3};{media(av1, av2, av3)}')
        file.write('\n')
  except :
    e = sys.exc_info()[0]
    print('Falha ao criar o arquivo!', e)

def obterAluno(disciplina):
  try:
    listaAlunos = []
    data = readFile('2023.csv')
    for line in data:
      item = line.strip().split(';')
      if item[2] == disciplina:
        listaAlunos.append(item)
    return listaAlunos
  except: 
    return []   
  
def obterDisciplinas():
  try:
    listaDisciplinas = []
    data = readFile('2023.csv')
    for line in data:
      item = line.strip().split(';')
      if item[2] not in listaDisciplinas:
        listaDisciplinas.append(item[2])
    return listaDisciplinas
  except: 
    return []
  

def media(av1, av2, av3):
  if av1 >= av2 and av2 >= av3:
    return (av1 + av2 ) / 2
  elif av1 >= av2 and av2 <= av3:
    return (av1 + av3 ) / 2
  else:
    return (av2 + av3 ) / 2

for d in obterDisciplinas():
  s = obterAluno(d)

  criarArquivoDiciplina(f'{d}.csv', s)
  criarArquivoMedias(f'{d}_notas.csv', s)