#pip install --upgrade google-api-python-client

#from googleapiclient.discovery import build
#from datetime import datetime
#import time

def Registro(log):
    #O código criará um log com as informações do vídeo, e irá registra-lo num arquivo de texto
    #O código irá mostrar no console as mesmas coisas que registrar no arquivo.
    data_atual = datetime.today().strftime("%D %H:%M:%S")
    #A data e o horário serão adicionados ao relátorio.
    arq = open('log.txt', 'a')
    arq.write(data_atual +'\n'+ log +'\n\n')
    arq.close()
    retorno = f'{log}\n{data_atual}'
    print(retorno)
    return

youtube = build('youtube','v3',developerKey='INSIRA SUA CHAVE API')
#O programa requer que o usuário insira sua própria chave API

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
    #favoritos = estatisticas['favoriteCount']
    #comentarios = estatisticas['commentCount']

    saida = f'''Quantidade de visualizações: {view}
Quantidade de curtidas: {like}
Quantidade de comentários: {comentarios}\n'''
    Registro(saida) 

    time.sleep(delay)
    #final do for

  difView = int(view)-viewInicial
  difLike = int(like)-likeInicial
  delta = (time.time() - inicio)/60

  diff = f'A diferença de visualizações ao longo da análise foi de {difView}, e a de curtidas foi {difLike} ao longo de {delta} minutos'
    #No final do processo o código ira dizer e registrar no arquivo a diferença das estatísticas do vídeo do início até a última análise, além do tempo decorrido do programa.
  Registro(diff)
    
  return(Registro('Coleta de dados concluída\n'))

ytID = 'olDCJ1w3FLM'
#Insira a parte final do link do vídeo do youtube que quiser analisar

AnaliseYT(ytID, 60, 10)
#O usúario então define o tempo, em minutos, que o programa vai ficar coletando os dados, e também o intervalo entre cada coleta. No final de cada intervalo será registrado num arquivo .txt os valores de curtidas e visualizações do vídeo, além do momento em que os dados foram coletados.
