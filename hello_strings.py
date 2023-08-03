#programa para ler nome do usuario e dar ola

#1- perguntar nome do usuario (usamos a variavel name para guardar o nome)
name = input("What´s your name? ")

#remove os espaços em branco da string 
name = name.strip()         #nome_da_string.strip()

#diz hello para o user
print(f"hello, {name}")