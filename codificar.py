import sys

from PIL import Image

# Função para codificar a imagem
def codificandoImagem(imagem, texto, plano_bits, imagem_saida):
  # Abrindo a imagem
  imagem = Image.open(imagem)
  # Acessando os pixels
  pixels = imagem.load()
  # Convertendo a mensagem para binário
  mensagem = mensagemParaBin(texto)
  # Contador sobre cada bit da mensagem em binário
  contagem_codificacao = 0
  
  # Iteração sobre cada pixel da imagem
  for y in range(imagem.height):
    for x in range(imagem.width):
        # Acessando o valor do plano especificado do pixel
        plano_pixel = pixels[x, y][int(plano_bits)]
        # Trasformando o valor do plano do pixel em binário
        plano_pixel_binario = bin(plano_pixel)
        # Adicionando o código em binário do pixel sem o último bit com um bit da mensagem
        plano_pixel_binario = plano_pixel_binario[0:len(plano_pixel_binario)-1] + mensagem[contagem_codificacao]
        contagem_codificacao += 1
        
        # Criando um array a partir da tupla RGB
        pixel_list = list(pixels[x, y])
        # Alterando o valor do plano especificado
        pixel_list[int(plano_bits)] = int(plano_pixel_binario, 2)
        # Alterando a tupla RGB a partir do array
        pixels[x,y] = tuple(pixel_list)

        # Se a mensagem foi toda codificada
        if contagem_codificacao >= len(mensagem):
          # Salva a imagem
          imagem.save(imagem_saida)
          quit()

# Função para transformar mensagem em binário
def mensagemParaBin(mensagem):
  mensagem_bin = []
  
  # Iteração para cada caracter da mensagem
  for i in list(mensagem):
    # Transformando o caracter da mensagem em ASCII (ord) e depois em binário (bin)
    caracter_em_bin = bin(ord(i))
    # Adicionando o código binário do caracter no array
    mensagem_bin.append(caracter_em_bin[2:len(caracter_em_bin)])
  
  # Adicionando 0's a esquerda para manter a formatação de 8 bits      
  zerosAEsquerda(mensagem_bin)
  
  return "".join(mensagem_bin)

# Função para adicionar 0's a esquerda do código binário
def zerosAEsquerda(mensagem_bin):
  # Iteração para cada elemento do array de códigos binários
  for i in range(len(mensagem_bin)):
    # Se o código for menor que 8 bits
    if len(mensagem_bin[i]) < 8:
      zeros_que_faltam = 8-len(mensagem_bin[i])
      # Adicionando os 0's que faltam
      mensagem_bin[i] = (zeros_que_faltam*'0') + mensagem_bin[i]

# Lendo o contéudo do arquivo txt
with open(sys.argv[2], "r") as arquivo:
  texto = arquivo.read()

# Adicionando o '\0' no final do texto
texto = texto + '\0'

# Codificando a imagem
codificandoImagem(sys.argv[1], texto, sys.argv[3], sys.argv[4])