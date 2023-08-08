#programa para ler nome do usuario e dar ola

#1- perguntar nome do usuario (usamos a variavel name para guardar o nome)
name = input("What´s your name? ")

#2- printar hello e nome do usuario FUNCIONOU?

print("ex1: hello, " + name)

print("ex2: hello,",name, sep=" ") #sep é o q defini para separar o hello do name (no caso um espaço )

#(MAIS COMUM)
print(f"ex3: hello, {name}")

#---------------------------------------------------------------------------------------------------------
# IMPORTANTE -- SYTAXE DO PRINT EM PHYTON --
#--> print(object(s), sep=separator, end=end, file=file, flush=flush)

#object(s)--> Qualquer objeto, e quantos você quiser. Será convertido em string antes de impresso

#sep='separator'--> Opcional - Especifique como separar os objetos, se houver mais de um. Padrão é ' ' (ex 2: print("ex2: hello,",name, sep=" "))

#end='end' --> Opcional. Especifique o que imprimir no final. O padrão é '\n' (alimentação de linha)

#file --> Um objeto com um método de gravação. O padrão é sys.stdout

#flush --> Opcional. Um booleano, especificando se a saída é liberada (True) ou armazenada em buffer (False). O padrão é falso
