def main():
    users = [("Amina", "pass123"), ("Erland", "pass456")]
    logged_in_user = None
    state = "start"

    while state != "quit":
        if state == "start":
            state, logged_in_user = vis_start_meny(users)
        elif state == "login":
            state = vis_innlogget_meny(logged_in_user)
        else:
            print("Ugyldig valg, prøv igjen.")
            state = "start"


def vis_start_meny(users):
    print("\n=== STARTMENY ===")
    print("1. Logg inn")
    print("2. Registrer NY bruker")
    print("3. Avslutt")

    valg = input("Hva ønsker du å gjøre? ")

    if valg == "1":
        bruker = logg_inn(users)
        if bruker is not None:
            return "login", bruker
        else:
            return "start", None
    elif valg == "2":
        registrer_bruker(users)
        return "start", None
    elif valg == "3":
        print("Ha det!")
        return "quit", None
    else:
        print("Ugyldig valg.")
        return "start", None


def logg_inn(users):
    print("=== LOGG INN ===")
    brukernavn = input("Skriv brukernavn: ")
    passord = input("Skriv passord: ")

    for navn, pw in users:
        if navn == brukernavn and pw == passord:
            print("Du er logget inn som", brukernavn)
            return brukernavn

    print("Feil brukernavn eller passord!")
    return None


def registrer_bruker(users):
    print("=== REGISTRER NY BRUKER ===")
    nytt_navn = input("Velg brukernavn: ")

    for navn, pw in users:
        if navn == nytt_navn:
            print("Brukernavn finnes allerede!")
            return

    nytt_pass = input("Velg passord: ")
    users.append((nytt_navn, nytt_pass))
    print("Ny bruker registrert!")


def vis_innlogget_meny(bruker):
    print(f"\n=== INNLOGGET SOM {bruker} ===")
    print("1. Fortell en vits")
    print("2. Logg ut")
    print("3. Avslutt")

    valg = input("Hva vil du gjøre? ")

    if valg == "1":
        print("Haha, hvorfor krysset høna veien? For å komme til den andre siden!")
        input("Trykk ENTER for å fortsette...")
        return "login"
    elif valg == "2":
        print("Du er nå logget ut.")
        return "start"
    elif valg == "3":
        print("Ha det!")
        return "quit"
    else:
        print("Ugyldig valg.")
        return "login"


main()
