""" 
print(curso.strip()) -> .strip retira todos os espaços antes e depois da palavra
print(curso.lstrip()) -> .lstrip retira todos os espaços do lado esquerdo
print(curso.rstrip()) -> .rstrip retira todos os espaços do lado direito
(Nenhum deles retira o espaço entre as palavra, apenas os desnecessários)

print(curso.center(10, "#")) -> Adiciona a variável curso caracteres definidos após a virgula suficientes para completar 10 casas e centraliza o valor da variável.
Resultado: "##Python##" Centralizou a palavra python e adicionou 4 # para completar 10 casas.
(Caso o segundo parâmetro não seja adicionado ele completa com espaços vazios.)

print(".".join(curso)) -> adiciona o valor "." entre cada letra da palavra definida na variável curso.
Resultado: "P.y.t.h.o.n"

###################################################################################
Exemplos de Fatiamento de string

nome = "Guilherme Arthur de Carvalho"  -> Variável

nome[0] -> Retorna o primeiro caractere da variável.
Resultado: "G"

nome[:9] -> Se não passar o primeiro parâmetro antes dos dois pontos ele considera como 0 (Primeiro caractere) e o segundo parametro é até qual casa da variável vc quer retornar.
Resultado: "Guilherme"

nome[10:] -> Se não passar o segundo parâmetro ele considera até o final da variável.
Resultado: "Arthur de Carvalho" **Ele começa na 11 casa e vai até o final

nome[10:16:2] -> o terceiro parametro faz ele pular as casas, no exemplo ele irá começão na casa 10, terminar na 16, pulando de 2 em 2 casas.
Resultado: "Atu"

nome[:] -> Retorna a variável inteira.

nome[::-1] -> Retorna a variável ao contrário
Resultado: ohlavraC ed ruhtrA emrehliuG

"""
