from random import randrange
print("Odpovídej prší/neprší.")
body = 0
while True:
    odpoved=input("Prší, nebo neprší?")
    if odpoved =="prší" or odpoved == "neprší":
        spravna_odpoved = randrange(0,2)
        if spravna_odpoved == 0:
            spravna_odpoved = "neprší"
        else:
            spravna_odpoved = "prší"
        if odpoved == spravna_odpoved:
            body +=10
            print("Počítám objem vody...")
            print("Máš celkem " + str(body) + " bodů, zbývá ti " + str(1000 - body) + " bodů.")
        else:
            print("BOSS")
            odpoved=input("Prší, nebo neprší?")
            spravna_odpoved = randrange(0,2)
            if spravna_odpoved == 0:
                spravna_odpoved = "neprší"
            else:
                spravna_odpoved = "prší"
            if odpoved == spravna_odpoved:
                body +=10
                print("Počítám objem vody...")
                print("Máš celkem " + str(body) + " bodů, zbývá ti " + str(1000 - body) + " bodů, přičelt jsem ti 10 bodů.")
            else:
                body -= 10
                print("Odebral jem ti 10 bodů,protože jsi neodpoveděl správně.")
    else:
        print("Nerozumím!")
    if body == 1000:
        print("Dostal si perlu od mušle, můžeš si koupit co chceš!")
        break
