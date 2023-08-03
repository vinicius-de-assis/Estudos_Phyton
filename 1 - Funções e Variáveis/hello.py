#programa para ler nome do usuario e dar ola

#1- perguntar nome do usuario (usamos a variavel name para guardar o nome)
name = input("What´s your name? ")

#2- printar hello e nome do usuario

print("ex1: hello, " + name)

print("ex2: hello,",name, sep=" ") #sep é o q defini para separar o hello do name (no caso um espaço )

#(MAIS COMUM)
print(f"ex3: hello, {name}")
