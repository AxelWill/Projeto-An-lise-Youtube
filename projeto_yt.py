# -*- coding: utf-8 -*-

#pip install --upgrade google-api-python-client

#from googleapiclient.discovery import build
#from datetime import datetime
#import time

def Registro(log):
    data_atual = datetime.today().strftime("%D %H:%M:%S")
    arq = open('log.txt', 'a')
    arq.write(data_atual +'\n'+ log +'\n\n')
    arq.close()
    retorno = f'{log}\n{data_atual}'
    print(retorno)
    return

youtube = build('youtube','v3',developerKey='INSIRA SUA CHAVE API')

def AnaliseYT(ytID, tempo, delay):
  inicio = time.time()

  res = youtube.videos().list(part='statistics', id = ytID).execute()
  info = res['items'][0]

  snip = youtube.videos().list(part='snippet', id = ytID).execute()
  titulo = snip['items'][0]['snippet']['title']

  Registro(f'Análise de {titulo}')

  estatisticas = info['statistics']

  viewInicial=int(estatisticas['viewCount'])
  likeInicial=int(estatisticas['likeCount'])

  for i in range(tempo * (60//delay)):
    res = youtube.videos().list(part='statistics', id = ytID).execute()

    estatisticas = res['items'][0]['statistics']

    view=estatisticas['viewCount']
    like=estatisticas['likeCount']
    favoritos = estatisticas['favoriteCount']
    comentarios = estatisticas['commentCount']

    saida = f'''Quantidade de visualizações: {view}
Quantidade de curtidas: {like}
Quantidade de comentários: {comentarios}\n'''
    Registro(saida)

    time.sleep(delay)

    #End of For

  difView = int(view)-viewInicial
  difLike = int(like)-likeInicial
  delta = (time.time() - inicio)/60

  diff = f'A diferença de visualizações ao longo da análise foi de {difView}, e a de curtidas foi {difLike} ao longo de {delta} minutos'

  Registro(diff)
  return(Registro('Coleta de dados concluída\n'))

ytID = 'ay2ZPX8vgG8'#Insira a parte final do link do vídeo do youtube que quiser analisar
AnaliseYT(ytID, 60, 10)