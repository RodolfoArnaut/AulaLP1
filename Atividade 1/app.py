IdadeDias = int(input("Por favor, insira a sua idade expressa em dias "))


def CalcularIdade(IdadeDias):


    DiasAno = 365.25 # .25 inserido para contabilizar anos bisextos
    DiasMês = 30.5 # .5 usado para contabilizar dias 31  


    Anos = int (IdadeDias // DiasAno)



    DiasRestantes = int (IdadeDias % DiasAno)
    Meses = int ( DiasRestantes // DiasMês)


    Dias = int (DiasRestantes % DiasMês)

    return (Anos, Meses, Dias)



Anos, Meses, Dias = CalcularIdade(IdadeDias)
print(f"{IdadeDias} dias equivalem a {Anos} anos, {Meses} meses e {Dias} dias.") 


