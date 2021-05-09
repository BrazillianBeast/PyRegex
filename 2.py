# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU

from skip import skip_line
import re


texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

print(re.findall(r'João|Maria|ad....s', texto))
print(re.findall(r'João|joão|Maria|ad....s', texto))  # Ou J ou j  forma simples
print(re.findall(r'[Jj]oão|[Mm]aria|ad....s', texto))  # Ou J ou j  forma inteligente
print(re.findall(r'[a-z]aria', texto))  # Qualquer letra entre a ate z minuscula
print(re.findall(r'[a-zA-Z]aria|[a-zA-Z]oão', texto))  # Qualquer letra entre a ate z minuscula e maisculo
print(re.findall(r'jOãO|mariA', texto, flags=re.I))  # Achar joao e  maria indenpendente de Maiusculo | Minusculo