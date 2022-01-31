
# coding: utf-8

# # Replace IMG on Typora
# 
# Muitas vezes, em meu estudo,eu tiro o print da tela, apra economizar tempo (print de texto0, ou para pega uma imagem)
# 
# Acontece que gosto de colcoar isso no typora, par aisos, eu tenho que fazer por exemplo de
# 
# ````
# img-c2-7-37
# ````
# 
# ````
# ![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-37.png)
# ````
# 
# # Qual o Objetivo
# 
# Ao invez de faer manualmente, criar um programr que ler onde começa com 'img-' e substitui por um path + img + .png. QUe todo o processo seje editável e asism altere o md, economiznaod meu tempo

# In[3]:


import sys
import re
import fileinput


# In[2]:


# CONSTANTS
extension = '.png'
root_dir = '![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/'
final_string = ')'


# In[4]:


# afile = '06-data-lake-aws-messages-kafka-zookeeper.md'
if(len(sys.argv) != 2):
	exit()
afile = sys.argv[1]


# In[16]:


c  = 0
for line in fileinput.input(afile, inplace=True):
	# Inserir path para a imagem
    if(line.startswith('img-')):
        print(root_dir + line.strip() + extension + final_string, end='')
        c = c + 1
	# Colocar trecho de CTRL+SHIF+K do Typora (trecho DE UMA LINHA código)
    # Para cada linha que começa com $ (símbolo para indicar o terminal
    # Lembre-se: '$' é para trecho de códdigo de APENAS UMA ÚNICA LINHA
    elif(line.startswith('$')):
        print("````programing_language")
        print(line, end='')
        print("````")
    else:
        print(line, end='')
	

print(c, 'lines modify', '\nSuccess')

