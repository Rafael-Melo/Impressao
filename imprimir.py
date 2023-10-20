import win32print
import win32api
import os

# Escolher impressora
lista_impressoras = win32print.EnumPrinters(2)
impressora = lista_impressoras[0]
    
win32print.SetDefaultPrinter(impressora[2])

# Imprimir todos os arquivos de uma pasta
caminho = r"C:\Users\rmelo\Documents\TESTES PYTHON\Impressao\imprimir"
lista_arquivos = os.listdir(caminho)

# https://docs.microsoft.com/en-us/windows/win32/api/shellapi/nf-shellapi-shellexecutea
for arquivo in lista_arquivos:
    win32api.ShellExecute(0, "print", arquivo, None, caminho, 0)

print(impressora[2])
