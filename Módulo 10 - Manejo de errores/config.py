#---------------------------------------------------
# def main():
#     try:
#         configuration = open('config.txt')
#     except FileNotFoundError:
#         print("Couldn't find the config.txt file!")


# # if __name__ == '__main__':
# main()
#---------------------------------------------------
# La instrucción en el módulo es confusa y no resulta,
# sigue marcando que no exontro el txt (claro buscar un 
# directorio es igual de raro...).
#---------------------------------------------------
# def main():
#     try:
#         configuration = open('config.txt')
#     except FileNotFoundError:
#         print("Couldn't find the config.txt file!")
#     except IsADirectoryError:
#         print("Found config.txt but it is a directory, couldn't read it")
# main()
#-----------------------------------------------------
# Lo mismo de arriba, no funciona bien...
# sepa que sucede por que de acuerdo a la instrucción, se debe
# de hacer config.py, un directorio con extensión .txt (idkw),
# y ninguno de los dos códigos detecta como directorio...
#------------------------------------------------------
# def main():
#     try:
#         configuration = open('config.txt')
#     except FileNotFoundError:
#         print("Couldn't find the config.txt file!")
#     except IsADirectoryError:
#         print("Found config.txt but it is a directory, couldn't read it")
#     except (BlockingIOError, TimeoutError):
#         print("Filesystem under heavy load, can't complete reading configuration file")
# main()
#---------------------------------------------------------
# guardé una captura de pantalla de como está configurado mi 
# directorio de trabajo como evidencia de que por alguna
# razón, aunque el código maneja la excepción 'IsADirectoryError',
# por alguna razón se va por default a que no existe...
#------------------------------------------------------------
# try:
#      open("mars.jpg")
# except FileNotFoundError as err:
#      print("got a problem trying to read the file:", err)
#-------------------------------------------------------------
# ¿no será que hay falla al definirlo en una función?
# no debería ser eso lo que cause el problema...
# CONTINÚA EN AGUA_ISS.PY
