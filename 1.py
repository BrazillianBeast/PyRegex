from skip import skip_line

import re

#findall search sub
#compile

string = 'Este é um teste de expressões teste regulares'


#acha somente a primeira
print(re.search(r'teste', string)) 

skip_line()

#acha todas
print(re.findall(r'teste', string)) 

skip_line()

#substiti todas 
print(re.sub(r'teste', 'ABCD',string, count=0)) 

skip_line()
#substiti uma 
print(re.sub(r'teste', 'ABCD',string, count=1)) 

skip_line()

#2° e melhor forma
#Compilando apenas uma vez e reutilizando
regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('DEF', string))
