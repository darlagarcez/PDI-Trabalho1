# PDI-Trabalho1
## Implementação de um algoritmo de esteganografia em imagens digitais.

### 1. Como executar
* **Para executar o código de codificação `codificar.py`**, é necessário que a imagem (png) e a mensagem (txt) que será codificada ambos estejam na mesma pasta do arquivo do código. A execução do programa deve ser:
``` python codificar.py imagem_entrada.png texto_entrada.txt plano_bits imagem_saida.png```
Onde os parâmetros:
	* imagem_entrada.png: deve ser o nome do arquivo da imagem que será codificada.
	* texto_entrada.txt: deve ser o nome do arquivo da mensagem que será codificada.
	* plano_bits: deve ser o plano (RGB)da imagem que a mensagem será codificada:
		* 0: plano R.
		* 1: plano G.
		* 2: plano B.
	* imagem_saida.png: deve ser o nome do arquivo da imagem codificada terá.
* **Para executar o código de decodificação `decodificar.py`**, é necessário que a imagem (png) codificada esteja na mesma pasta do arquivo do código. A execução do programa deve ser:
``` python decodificar.py imagem_saida.png plano_bits texto_saida.txt```
Onde os parâmetros:
	* imagem_saida.png: deve ser o nome do arquivo da imagem codificada.
	* plano_bits: deve ser o plano (RGB) da imagem que a mensagem foi codificada:
		* 0: plano R.
		* 1: plano G.
		* 2: plano B.
	* texto_saida.txt: deve ser o nome do arquivo da mensagem que será decodificada.

### 2. Descrição dos códigos
Em ambos os códigos, de codificação e decodificação, foram utilizadas as biblioteca `PIL` para fins de processamento da imagem em uma matriz e manipulação dos pixels e `sys` para acessar os parâmetros da execução e manipular arquivos. 
* **No código `codificar.py`** a função `codificandoImagem` acessa a imagem `imagem = Image.open(imagem)`, acessa os pixels da imagem `pixels = imagem.load()` e utiliza duas iterações *for* para percorrer as coordenadas x e y dos pixels e alterar o bit menos significado do plano especificado de cada um. A biblioteca `PIL` transforma a matriz da imagem em uma tupla, por isso, para alterar o valor do pixel, foi necessário criar um *array* contendo os valores da tupla de cada pixel `pixel_list = list(pixels[x, y])`, alterar apenas o valor do plano alterado no *array* `pixel_list[int(plano_bits)] = int(plano_pixel_binario, 2)` e depois voltar os valores para a tupla `pixels[x,y] = tuple(pixel_list)`. Já as funções `mensagemParaBin` e `zerosAEsquerda` servem para, respectivamente, converter a mensagem contida no arquivo txt em uma *string* binária e adicionar zeros a esquerda de cada uma dos códigos binários de cada caractere da mensagem (a fim de manter o formato de 8 bits padrão para cada um). por fim, após acessar e ler o arquivo txt com a mensagem, é necessário adicionar um `\0` para marcar o fim da mensagem `texto = texto + '\0'`, assim ao decodificar a mensagem, o código irá identificar quando a mensagem termina.
* **No código `decodificar.py`** a função `lendoMensagemOculta` acessa a imagem `imagem = Image.open(imagem)`, acessa os pixels da imagem `pixels = imagem.load()` e utiliza duas iterações *for* para percorrer as coordenadas x e y dos pixels e acessar o bit menos significativo do plano especificado de cada um. Para dividir os bits em 8 e verificar se o código binário capturado e do `\0`, foram utilizados dos *if*. Já a função `binParaString` transforma o código binário, armazenado em um *array*, em uma *string*.

### 3. Problemas encontrados e suas soluções:
*  **Acessar os pixels da imagem:** No início, o maior problema de desenvolver os códigos foi como acessar e manipular os pixels da  da imagem. Primeiro, foi encontrada a biblioteca `stegano`, porém ela realiza todo o trabalho de codificação e decodificação. Depois, foi encontrada a biblioteca `PIL` que só realiza o trabalho de transformar a imagem em uma matriz, acessar seus pixels e salvar a imagem alterada.
* **Acessando todos os pixels da imagem e alterando apenas um pixel:** As iterações *for* na função `codificandoImagem` estavam acessando todos os pixels da imagem e alterando apenas o primeiro pixel. Para isso, foi necessário criar um contador `contagem_codificacao` que armazena a quantidade de codificações realizadas e é comparado com o tamanha da *string* binária, e transformar a mensagem em *string* binária (antes era armazenada em um *array*).

### 4. Testes executados
Os testes executados foram feitos com a imagem `imagem_entrada.png` contida na pasta do código e, inicialmente, com mensagens curtas até mensagem mais longas, armazenadas no arquivo txt `texto_entrada.txt`. Em quase todos os testes, as mensagem foram codificadas e decodificas de forma eficiente, tirando os testes:
* **Quando a função `codificandoImagem` estava alterando apenas o primeiro pixel:** A mensagem não era codificada da forma correta.
* **Quando a função `binParaString` foi apagada:** Sem essa função, o que era escrito no arquivo da mensagem de saída era uma a *string* binária da mensagem.
