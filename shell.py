import time
import core
import disk
import time,sys

typing_speed = 15
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(typing_speed / 970.0)
    return input()

def main():
    print("\t\tWelcome to AZ's Canopy Party Tents Rental!\n")
    time.sleep(1.5)
    slow_type("Canopy tents are a light weight structure, they are great for protection from sun or light rain. They are to be installed and removed by you, the renter. Press 'Enter' to continue.\n")
    tent = input('Canopy tents are available to rent up to 2 days. Would you like to rent a tent or tents today? 1: yes 2: no\n')
    if tent == '2' or tent.lower() == 'no':
        print("That's fine, come back again if you change your mind!")
     
    elif tent == '1' or tent.lower() == 'yes':
            print('\nGreat, here are the tent sizes we have available. You can choose to just rent the tent or have chairs and tables included with them.\n')
            print('\n'.join(core.type_of_tents()))
            tent1 = input('Tent: \n')
            not1 = core.cost_of_tents(tent1)
            tents = core.cost_of_tents(tent1)
            amount = input('\n How many tents of this type would you like?')
            tent_1 = float(amount) * float(tents)
            if not disk.take_away(tent1, amount):
                print('Sorry, we do not have this type of tent available.')
                return None
            con = input('\nTent ' + tent1 + ' price is $' + str(tent_1) + ' dollars. Would you like to continue?\n')
            tent2 = core.deposit(tent_1)
            tent3 = core.total(tent_1)
            tent4 = tent_1 * 2
            if con == 'yes':
                days = input('\nHow many days will you be renting this? Only up to 2 days.\n')
                total = (float(tent2) + float(tent3)) + float(tent_1)
                total2 = (float(tent2) + float(tent3)) + float(tent4)
                if days == '1':
                    print('Your renting this for 1 day, your total with deposit and tax is $' + str(float(total)))
                    history = disk.keep_history(tent1, total)
                    print('Thank you')
                elif days == '2':
                    print('\nYour renting this for 2 days, your total with deposit and tax is $' + str(float(total2)))
                    history = disk.keep_history(tent1, total2)
                    print('Thank you')
                    

        




if __name__ == '__main__':
    main() 