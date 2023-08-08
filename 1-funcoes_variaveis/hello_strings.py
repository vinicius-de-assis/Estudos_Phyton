#=============================PROGRAMA PARA DAR OLA AO USUARIO EM PHYTON==================================

#1- perguntar nome do usuario (usamos a variavel name para guardar o nome)
#name = input("What´s your name? ") 

#Como já sabemos algumas funções podemos coloocar elas no input, como por exemplo pedindo o nome do usuário

name = input("What´s your name? ")      #aq pedimos o nome de usuario e a resposta bem sem espaços
#.                                                            e com maiusculas em cada palavra


#==================================ALGUMAS FUNCOES============================================================
#para testar as funções é necessário escrever a linha de código antes: name = input("What´s your name? ")
#=============================================================================================================
#FUNCAO --> nome_da_string.strip()     --> remove espaços
name_strip = name.strip()         
#var = nome_da_string.strip()
print(f"\nSTRIP = hello, {name_strip}")               #--> hello sem espaços
#---------------------------------------------------------------------------------------------------------
#FUNCAO --> nome_da_string.capitalize()   --> Coloca letra maíscula no primeiro caracter (ex: vini fica Vini)
name_capitalize = name.capitalize()         
#var = nome_da_string.capitalize()
print(f"CAPITALIZE = hello, {name_capitalize}")                  #--> hello com primeiro caracter maisculo
#---------------------------------------------------------------------------------------------------------
#FUNCAO --> nome_da_string.title()   --> Coloca letra maíscula em cada palavra (ex: vini assis  fica Vini Assis)
name_title = name.title()         
#var = nome_da_string.title()
print(f"TITLE = hello, {name_title}")              #--> hello com letra maíscula em cada palavra
#==============================================================================================================
#TAMBEM É POSSIVEL USAR MAIS DE UMA FUNCAO EX: VAMOS REMOVER ESPACO E COLOCAR LETRA MAISCULA EM CADA PALAVRA
name_strip_title = name.strip().title()       
#var = nome_da_string.strip().title()
print(f"STRIP AND TITLE = hello, {name_strip_title}")              #--> hello com letra maíscula em cada palavra e sem considerar espaços
#---------------------------------------------------------------------------------------------------------
#FUNCAO --> nome_da_string.split("caractere que quero que divida a partir")   --> separa as palavras a partir de determinado caractere
first, last = name.split(" ")         
#var = nome_da_string.split(" ") #separa a partir do "espaço"
print(f"SPLIT = hello, {last, first}")              #--> hello com letra maíscula em cada palavra
#==============================================================================================================
