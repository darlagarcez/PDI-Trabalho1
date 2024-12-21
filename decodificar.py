import sys

from PIL import Image

#
def lendoMensagemOculta(imagem_saida, plano_bits):
  # Abrindo a imagem
  imagem = Image.open(imagem_saida)
  # Acessando os pixels
  pixels = imagem.load()
  # Array para armazenar os códigos binários de cada caracter
  mensagem_bin = []
  # String para armazenar o código binário de cada caracter
  caracter_em_bin = ''
  
  for y in range(imagem.height):
    for x in range(imagem.width):
      # Acessando o valor do plano especificado do pixel
      plano_pixel = pixels[x, y][int(plano_bits)]
      # Trasformando o valor do plano do pixel em binário
      plano_pixel_binario = bin(plano_pixel)
      # Adicionando o último bit do código binário do plano do pixel na string
      caracter_em_bin = caracter_em_bin + plano_pixel_binario[-1]

      # Se a string atingir o limte de 8 bits
      if len(caracter_em_bin) == 8:
        # Se a string for igual ao código binário do '\0'
        if caracter_em_bin == '00000000':
          # Transformando a string binária em um texto
          texto = binParaString(mensagem_bin)
          return texto
        else:
          # Adicionando o código binário ao array
          mensagem_bin.append(caracter_em_bin)
          caracter_em_bin = ''

# Funçao para transformar a string binária em um texto
def binParaString(mensagem_bin):
  mensagem = ''
  # Iteração para cada elemento do array
  for i in range(len(mensagem_bin)):
    # Adicionando caracter por caracter a mensagem
    mensagem = mensagem + chr(int(mensagem_bin[i], 2))

  return mensagem

# Recebendo a mensagem decodificada
texto = lendoMensagemOculta(sys.argv[1], sys.argv[2])

# Escrevendo a mensagem decodificada no arquivo txt
with open(sys.argv[3], "w") as arquivo:
  arquivo.write(texto)