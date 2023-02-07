perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

correct = 0

for question in perguntas:

    print(question["Pergunta"])
    print("\nOpções: ")

    for ind, val in enumerate(question["Opções"]):
        print(str(ind) + ") " + val)
    
    answer = input("Option: ")

    if answer == question["Resposta"]:
        print("Acertou\n")
        correct += 1
    else:
        print("Errou\n")

print(f"Você acertou {correct} perguntas")