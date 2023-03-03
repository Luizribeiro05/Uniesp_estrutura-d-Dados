notas = int(input("Quantas notas? "))
aluno = input("Nome do aluno: ")

count = 1; soma_nota = 0.0
while count <= notas:
    print('Nota do aluno', count,":")
    nota = float(input())
    if nota >= 0 and nota <= 10:
        print("----------")
        soma_nota += nota
        count += 1
    else:
        print("###########")
        print("Nota errada ", nota,":")
        print("DIgite novamente a nota do aluno", count,":")
        nota = float(input())
        nota += soma_nota
        count =+ 1
print("Media do Aluno:",aluno,"-",(soma/notas))
