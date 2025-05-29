def resultadoComIf(mediaFinal):
    if mediaFinal >= 7:
        return "APROVADO"
    elif mediaFinal >= 5:
        return "RECUPERAÇÃO"
    else:
        return "REPROVADO"

def resultadoComTernario(mediaFinal):
    return (
        "APROVADO" if mediaFinal >= 7
        else "RECUPERAÇÃO" if mediaFinal >= 5
        else "REPROVADO"
    )

def resultadoComSwitch(mediaFinal):
    match mediaFinal:
        case n if n >= 7:
            return "APROVADO"
        case n if n >= 5:
            return "RECUPERAÇÃO"
        case _:
            return "REPROVADO"

def media(n1, n2):
    return (n1 + n2) / 2

def main():
    print(resultadoComIf(media(10, 7)))
    print(resultadoComTernario(media(5, 5)))
    print(resultadoComSwitch(media(4, 3)))

main()
