#programa para ler nome do usuario e dar ola

#1- perguntar nome do usuario (usamos a variavel name para guardar o nome)
name = input("What´s your name? ")

#FUNCAO --> nome_da_string.strip()     --> remove espaços
name = name.strip()         
#var = nome_da_string.strip()

#FUNCAO --> nome_da_string.capitalize()     --> Coloca letra maíscula no primeiro caracter (ex: vini fica Vini)
name = name.capitalize()         
#var = nome_da_string.capitalize()


#2- diz hello para o user
print(f"hello, {name}")