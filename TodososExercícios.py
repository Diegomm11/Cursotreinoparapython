print('EXERCÍCIO 001')
print('Olá Mundo!')
print('---------------------------')
print('EXERCÍCIO 002')
print('FORMATO 1')
name = input ('Qual o seu nome? ')
print('Olá', name, 'seja bem vindo!')
print('---------------------------')
print('FORMATO 2')
name1 = input ('Qual o seu nome? ')
print('É um prazer te conhecer, {}! '.format(name1))
print('---------------------------')
print('EXERCÍCIO 003')
print('FORMATO 1')
m1 = float(input('Qual o primeiro valor?'))
m2 = float(input('Qual o segundo valor?'))
m3 = float(input('Qual o terceiro valor?'))
m4 = float(input('Qual o quarto valor?'))
s = (m1+m2+m3+m4)
print('a soma entre', m1, ' + ', m2, ' + ', m3, ' + ', m4, ' vale ', s)
print('---------------------------')
print(type(m1))
print(type(m2))
print(type(m3))
print(type(m4))
print(type(s))
print('---------------------------')
print ('FORMATO 2')
n1 = float (input ('Qual o primeiro valor?'))
n2 = float (input ('Qual o segundo valor?'))
n3 = float (input ('Qual o terceiro valor?'))
n4 = float (input ('Qual o quarto valor?'))
s = (n1+n2+n3+n4)
print('a soma entre {} + {} + {} + {} vale {}'.format(n1, n2, n3, n4, s))
print('---------------------------')
print(type(n1))
print(type(n2))
print(type(n3))
print(type(n4))
print(type(s))
print('---------------------------')
print('EXERCÍCIO 004')
print('REFERENTO AO EXERCÍCIO 001 - NAME')
print('O tipo primitivo desse valor é ', type(name))
print('Só tem espaços? ', name.isspace())
print('É um número? ', name.isnumeric())
print('É alfabético? ', name.isalpha())
print('É alfanumérico? ', name.isalnum())
print('Está em maiúsculas? ', name.isupper())
print('Está em minusculo? ', name.islower())
print('Está capitalizada? ', name.istitle())
print('---------------------------')