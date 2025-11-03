# innloggingsprogram 

def main():
    state = "start"
    while state != "quit":
        if state == "start":
            pass
        elif state == "innLogget":
            pass

def vis_startmeny():
    print("\n === Startmeny ===")
    print("1)  Logg inn")
    print("2)  Registrer ny bruker")
    print("3)  Avslutt")
    valg = input ("hva ønsker du å gjøre")
    if valg == "1":
        print("Du er nå logget inn.")
        return "innLogget"
    elif valg == "2":
        print("Ny bruker registrert.")
        return "start"
    elif valg == "3":
        return "quit"
    else:
        print("Ugyldig valg, prøv igjen.")
        return "start"
    while state != "quit":
        if state == "start":
            state = vis_startmeny()
       
