# Nessa aula, vamos aprender como criar estruturas condicionais aninhadas, usando os comandos if.. elif.. else em programas Python.

nome = str(input('Qual é o seu nome? '))
if nome == 'Deus':
    print('Todo poderoso!!!')
elif nome == 'Maria' or nome == 'Pedro':
    print('Que Deus esteja contigo!')
elif nome in 'Ana Maria Bragra':
    print('Belo nome feminino')
else:
    print('Deus sabe de todas as coisas')
print('Tenha um bom dia {} '.format(nome))