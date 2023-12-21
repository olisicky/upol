logs = {
    'jídlo': [],
    'bydlení': [],
    'domáctnost': []
}

def pridej_polozku(den, mesic, rok, castka, kategorie):
    if kategorie not in ['jídlo', 'bydlení', 'domáctnost']:
        return False
    else:
        logs[kategorie].append((den, mesic, rok, castka))
        return True


def prehled(mesic, rok):
    
    souhrn = {}
    for cat in logs.keys():
        total = 0
        if len(logs[cat]) > 0:
            for log in logs[cat]:
                d, m, r, v = log
                if m == mesic and r == rok:
                    total += v
        else:
            total = 0
        souhrn.update({
            cat: total
        })
    return  souhrn

pridej_polozku(15,10,2022,150,"jídlo")
pridej_polozku(16,11,2022,250,"jídlo")
pridej_polozku(17,11,2022,300,"bydlení")
pridej_polozku(18,11,2022,500,"jídlo")
pridej_polozku(19,11,2022,150,"domáctnost")
print(prehled(11,2022))