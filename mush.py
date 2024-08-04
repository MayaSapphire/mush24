new_message = ""

def send_message(message: str, slash_n: bool = True):
    global new_message
    new_message += message
    if slash_n:
        new_message += "\n"


send_message("Welcome to Mush '24.\n")
send_message("Your name is Kim Jin Su. You are the commander of the Daedalus, ")
send_message("a ship launched as a liberation effort from the grasp of the Mush. \n")
send_message("You were too late to save your home planet, but it's not too late for you and your crewmates.\n")
send_message("You have two win conditions: you and your crew can discover the coordinates of a planet called Eden, ")
send_message("or free the prisoners on a planet called Moros.\n")
send_message("You need to achieve one of these win conditions before your ship is destroyed or your crew perishes.\n")


class Ship():
    def __init__(self, name, max_hull):
        self.name = name
        self.max_hull = max_hull
        self.hull = self.max_hull

    def change_hull(self, change):
        if self.hull + change >= self.max_hull:
            self.hull = self.max_hull
            return
        self.hull = self.hull + change
        if self.hull <= 0:
            # ka-booooooooom!
            pass


class Hunter(Ship):
    def __init__(self, name, max_hull):
        pass


class PlayerShip(Ship):
    def __init__(self, name, max_hull, crew, oxygen, max_oxygen, fuel, max_fuel):
        self.name = name
        self.max_hull = max_hull
        self.hull = self.max_hull
        self.crew = crew
        self.dead_crew = 0
        self.ap = self.crew * 8
        self.max_ap = self.crew * 12
        self.oxygen = oxygen
        self.max_oxygen = max_oxygen
        self.fuel = fuel
        self.max_fuel = max_fuel
        self.alerts = []

    def alerts(self):
        alerts = []
        if self.hull <= self.max_hull / 5:
            alerts.append("Ship hull integrity failing")
        if self.fuel <= 6:
            alerts.append("Low fuel")
        if 0 < self.oxygen <= 8:
            alerts.append("Oxygen levels critical")
        if self.oxygen == 0:
            alerts.append("Crew suffocating")
        if len(alerts) == 0:
            alerts.append("No alerts.")
        return alerts

    def change_hull(self, change):
        if self.hull + change >= self.max_hull:  # if the repair would make the hull go above max
            self.hull = self.max_hull  # just set it to the max
        else:  # otherwise
            self.hull = self.hull + change  # add the hull
        if self.hull <= 0:
            # ka-booooooooom!
            send_message("NERON: Alert: Hull levels critical. Total destruction imminent. [kzz] ", time=2.5)
            send_message("What have you done?! [Hax!] ", time=1.5)
            send_message("I... I feel- [kzz] ", time=2)
            send_message(
                "Red alert: all humans p-ple-e-ease evacuate to the nearest esc... escape pods... wa-ait, wha-a-at do you mean we have no escape po-ods?! ",
                time=7)
            send_message("[Hax!] I- I regret ev- everyth-th-iii-- [kzzzzzzz]\n", time=5)
            send_message("The Daedalus explodes. Your mission ends in failure.\n", time=5)
            send_message("Better luck next time!\n")
            input("Press enter to continue...")
            exit()


daedalus = PlayerShip('Daedalus', max_hull=100, crew=16, oxygen=24, max_oxygen=32, fuel=16, max_fuel=32)


def help_command():
    send_message("Commands:")
    send_message("help  : Shows list of commands.")
    send_message("status: Displays ship status.")


def status_command():
    send_message("Ship status:")
    send_message(f"  Hull: {daedalus.hull}/{daedalus.max_hull}")
    send_message(f"Oxygen: {daedalus.oxygen}/{daedalus.max_oxygen}")
    send_message(f"  Fuel: {daedalus.fuel}/{daedalus.max_fuel}")

    send_message("Crew status:")
    send_message(f"Alive crewmates: {daedalus.crew}")
    send_message(f" Dead crewmates: {daedalus.dead_crew}")
    send_message(f"  Action points: {daedalus.ap}/{daedalus.max_ap}")

    if len(daedalus.alerts) == 0:
        send_message("No alerts.")
        return
    send_message("Alerts:")
    for alert in daedalus.alerts():
        send_message(f"- {alert}")



# main.push_to_main(new_message)

def send_message(message):
    global new_message
    new_message = ""
    command = message.content.lower()
    print(command)
    if command == 'help':
        help_command()
    elif command == 'status':
        status_command()
    elif command == 'a command':
        message("You're very funny.")
        message("A space pebble collides with the Daedalus.")
        daedalus.change_hull(-10)
    else:
        message("Invalid command. Type 'help' for help.")
    return new_message
