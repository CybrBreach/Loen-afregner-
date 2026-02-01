filePath = ""



with open(filePath, 'rb') as penge:
    Penge = penge.read()
    penge.close()
tjent = int.from_bytes(Penge, byteorder='little')
print(tjent)
løn = 64

def logKøb():
   global tjent 
   pris = float(input("Hvor mange penge har du brugt? "))
   tjent = (tjent - pris)
   print("Dette er det der står tilbage " + str(tjent))
   menu()



def logLøn():
    global tjent 
    Timer = int(input("Hvor mange timer har du Arbejdet? "))
    Minutter = int(input("Hvor mange minutter har du Arbejdet? "))
    total = int((Timer + (Minutter/60)) * løn)
    tjent = (tjent + total)
    print("Dette er hvad der nu står " + str(tjent))
    with open(filePath, 'wb') as writeb:
        writeb.write(tjent.to_bytes(2, 'little'))
        print(tjent)
    menu()


def menu():
    global løn
    print("Hvad vile du Logge? ")
    svar = input("hvis du ville logge løn tryk 1, hvis du ville logge køb tryk 2.og hvis du ville se hvad der sår lige nu tryk 3 ")
    if(svar == '1'):
        logLøn()
    elif(svar == '2'):
        logKøb()
    elif(svar == '3'):
        with open(filePath, 'rb') as penge:
            Penge = penge.read()
            print(Penge)
            menu()

menu()




