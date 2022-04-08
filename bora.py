from string import Template

nome, idade = 'reialdo', 45
print('Nome: {0} Idade: {1}'.format(nome, idade))

print(f'Nome: {nome} Idade: {idade}')

s = Template('Nome: $nome Idade: $idade')
print(s.substitute(nome=nome, idade=idade))
