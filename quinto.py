n1 = input("Digite a primeira nota do aluno:")
n2 = input("Digite a segunda nota do aluno:")
n3 = input("Digite a terceira nota do aluno:")
n4 = input("Digite a quarta nota do aluno:")

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = (n1 + n2 + n3 + n4) / 4

if media >= 6:
    print("APROVADO")
elif media <= 4:
    print("REPROVADO")
else:
    print("RECUPERAÇÃO")
