def main():
    nome =  input("Digite o nome do aluno: ")
    nota =  float(input("Digite a nota do aluno: "))
    dic={nome:nota}
    for i in range(4):
        nome =  input("Digite o nome do aluno: ")
        nota =  float(input("Digite a nota do aluno: "))
        dic[nome]=nota
    notam=max(dic.values())
    nome_associado = [item for item, valor in dic.items() if valor == notam]
    print("Nome do aluno com maior nota:",nome_associado[0],"e sua respectiva nota:",notam)
main()