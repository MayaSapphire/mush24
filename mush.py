from time import sleep
import random

default_message_time = 1

def message(message: str, time:float=default_message_time):
    for char in message:
        print(char, end='')
        sleep(time/len(message))
message("Welcome to Mush '24.\n")
message("Your name is Kim Jin Su. You are the commander of the Daedalus, ")
message("a ship launched as a liberation effort from the grasp of the Mush. \n")
message("You were too late to save your home planet, but it's not too late for you and your crewmates.\n")
message("You have two win conditions: you and your crew can discover the coordinates of a planet called Eden, ")
message("or free the prisoners on a planet called Moros.\n")
message("You need to achieve one of these win conditions before your ship is destroyed or your crew perishes.\n")

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
        self.ap = self.crew*8
        self.max_ap = self.crew*12
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
        if self.hull + change >= self.max_hull: # if the repair would make the hull go above max
            self.hull = self.max_hull # just set it to the max
        else: # otherwise
            self.hull = self.hull + change # add the hull
        if self.hull <= 0:
            # ka-booooooooom!
            message("NERON: Alert: Hull levels critical. Total destruction imminent. [kzz] ", time=2.5)
            message("What have you done?! [Hax!] ", time=1.5)
            message("I... I feel- [kzz] ", time=2)
            message("Red alert: all humans p-ple-e-ease evacuate to the nearest esc... escape pods... wa-ait, wha-a-at do you mean we have no escape po-ods?! ", time=7)
            message("[Hax!] I- I regret ev- everyth-th-iii-- [kzzzzzzz]\n", time=5)
            message("The Daedalus explodes. Your mission ends in failure.\n", time=5)
            message("Better luck next time!\n")
            input("Press enter to continue...")
            exit()



daedalus = PlayerShip('Daedalus', max_hull=100, crew=16, oxygen=24, max_oxygen=32, fuel=16, max_fuel=32)

def help_command():
    print("Commands:")
    print("help  : Shows list of commands.")
    print("status: Displays ship status.")

def status_command():
    print("Ship status:")
    print(f"  Hull: {daedalus.hull}/{daedalus.max_hull}")
    print(f"Oxygen: {daedalus.oxygen}/{daedalus.max_oxygen}")
    print(f"  Fuel: {daedalus.fuel}/{daedalus.max_fuel}")

    print("Crew status:")
    print(f"Alive crewmates: {daedalus.crew}")
    print(f" Dead crewmates: {daedalus.dead_crew}")
    print(f"  Action points: {daedalus.ap}/{daedalus.max_ap}")

    if len(daedalus.alerts) == 0:
        print("No alerts.")
        return
    print("Alerts:")
    for alert in daedalus.alerts():
        print(f"- {alert}")

playing = True
while playing:
    command = input("\nPlease enter a command: ").lower()
    if command == 'help':
        help_command()
    elif command == 'status':
        status_command()
    elif command == 'a command':
        print("You're very funny.")
        print("A space pebble collides with the Daedalus.")
        daedalus.change_hull(-10)
    else:
        print("Invalid command. Type 'help' for help.")
