running = True
# prompt: A program addig fusson, amíg a felhasználó ki nem lép belőle.
# prompt: Ennek a kontrollja a running változó értékének változása.
while running:
    print("Opciók:")
    print("1. Összeadás")
    print("2. Kivonás")
    print("3. Megszorzás")
    print("4. Osztás")
    print("5. Kilépés")
    # prompt: A felhasználó választásait írjuk ki neki.

    choice = input("Válassz (1/2/3/4/5): ")
    # prompt: A felhasználó választását kérjük be.

    if choice in ("1", "2", "3", "4"):
        # prompt: Ha a választás érvényes, kérjük be a két számot.
        num1 = float(input("Írd be az első számot: "))
        num2 = float(input("Írd be a második számot: "))

        if choice == "1":
            print("Eredmény:", (num1 + num2))
        elif choice == "2":
            print("Eredmény:", (num1 - num2))
        elif choice == "3":
            print("Eredmény:", (num1 * num2))
        elif choice == "4":
            # prompt: Osztás esetén ellenőrizzük, hogy a második szám nem nulla-e.
            if num2 == 0:
                print("Nullával nem lehet osztani!")
            else:
                print("Eredmény:", (num1 / num2))
        # prompt: A választásnak megfelelően végezzük el a műveletet és írjuk ki az eredményt.
    elif choice == "5":
        print("Kilépés...")
        running = False
        # prompt: Ha a választás 5, akkor állítsuk le a programot.
    else:
        print("Érvénytelen választás! Kérlek válassz újra.")
