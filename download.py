import requests

def download_video(url, endereco="video.mp4"):

    resposta = requests.get(url, stream=True)
    
    if resposta.status_code == requests.codes.OK:
    
        with open(f'{endereco}', 'b+w') as video:
    
                for parte in resposta.iter_content(chunk_size=256):
                    video.write(parte)

        print(f"Download do vídeo finalizado.")
    else:
    
        resposta.raise_for_status()
    
def download_cover(url, endereco='capa_do_video.jpg'):
     
    resposta = requests.get(url, stream=True)
    
    if resposta.status_code == requests.codes.OK:
    
        with open(f'{endereco}', 'wb') as image:
    
                for parte in resposta.iter_content(chunk_size=256):
                    image.write(parte)

        print(f"Download da capa finalizado.")
    else:
    
        resposta.raise_for_status()