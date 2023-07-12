from zipfile import ZipFile
import sys

# Cria um objeto zip, futuramente esse objeto se tornará o arquivo zip
# Arg1: Caminho aonde o arquivo zip será criado ou lido
# Arg2: w, é escrita, o arquivo será criado no caminho especificado no arg1.
# r, é read, leitura, o arquivo deve existir no caminho especificado. Será
# retornado uma referencia para o arquivo. Após todas as manipulações, o objeto 
# zipFile deve ser fechado usando o método close
arquivoZip = ZipFile('./files/zip2.zip', 'w')

# O que eu quero escrever dentro do arquivo
# Arg1: Caminho para o arquivo que vai ser adicionado dentro do zip
# Arg2: Nome do arquivo dentro do zip
arquivoZip.write('./files/txt.txt', 'txt-alterado.txt')

# Fechando o arquivo zip (sempre é necessário fechar o arquivo)
arquivoZip.close()

