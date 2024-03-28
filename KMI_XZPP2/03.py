def over_spravnost_hesla(heslo):
    if len(heslo) < 8:
        raise ValueError('Heslo musí mít alespoň 8 znaků')
    elif not any(ele.isupper() for ele in heslo):
        raise ValueError('Heslo musí obsahovat alespoň jedno velké písmeno.')
    elif not any(ele.islower() for ele in heslo):
        raise ValueError('Heslo musí obsahovat alespoň jedno malé písmeno.')
    elif not any(ele.isdigit() for ele in heslo):
        raise ValueError('Heslo musí obsahovat alespoň jednu číslici.')
    else:
        print('Heslo má správný tvar.')
    return heslo

def over_heslo(zadano, heslo='Upol1234'):
    if zadano != heslo:
        raise ValueError('Nesprávné heslo')
    else:
        print('Gratuluji')
    return False


if __name__ == '__main__':

    trefa = True
    while trefa:
        heslo = input('Zadej heslo: ')
        overene_heslo = over_spravnost_hesla(heslo)
        try:
            trefa = over_heslo(overene_heslo)
        except:
            print('..., ale zadané heslo se neshoduje')



