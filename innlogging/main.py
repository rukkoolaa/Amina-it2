def main():
    state = "start"
    while state != "quit":
        if state == "start":
            state = vis_start_meny()
        elif state == "login":
            state = vis_innLogget_meny()
1
def vis_start_meny():
    print(" === STARTMENY === ")
    print("1. Logg inn")
    print("2. Registrer NY bruker")
    print("3. Avslutt ")
    valg = input("Hva ønsker du å gjøre? ")
    if valg == "1":
        print("Du er nå pålogget")
        return "login"
    elif valg == "2":
        print("Ny bruker registrert")
        return "start"
    elif valg == "3":
        return "quit"
    else:
        print("Ugyldig valg, prøv igjen.")
        return "start"

def vis_innLogget_meny():
    print(" === INNLOGGET MENY === ")
    print("1. Fortell en random vits")
    print("2. Logg ut")
    print("3. Avslutt ")
    valg = input("Hva ønsker du å gjøre? ")
    if valg == "1":
        return "innLogget"
    elif valg == "2":
        print("Du er nå logget ut")
        return "start"
    elif valg == "3":
        return "quit"
    else:
        print("Ugyldig valg, prøv igjen.")
        return "innLogget"
    
main()