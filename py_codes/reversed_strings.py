# Complete the solution so that it reverses the string passed into it.
# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

# executar este bloco se quiser receber a string antes da função
# frase = input("informe uma strig para reverte-la: ")

def inverter(string):
    return string[::-1]

print(inverter('world'))
print(inverter('word'))