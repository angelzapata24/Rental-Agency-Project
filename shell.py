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
    time.sleep(1)
    slow_type("Canopy tents are a light weight structure, they are great for protection from sun or light rain. They are to be installed and removed by you, the renter. Press 'Enter' or any key to continue.\n")
    while True:
        rent_return = input("Press '1' if you want to rent Tents. Press '2' if you are returning tents.\n" )    
        if rent_return == '1' or rent_return == '2':
            break
        else:
            print('\nInvalid answer')
    if rent_return == '1':
        while True:
            tent = input('Canopy tents are available to rent up to 2 days. Would you like to rent a tent or tents today? 1: yes 2: no\n')
            if tent == '2' or tent.lower() == 'no':
                print("That's fine, come back again if you change your mind!")
                break 
            elif tent == '1' or tent.lower() == 'yes':
                print('\nGreat, here are the tent sizes we have available. Tents 1-6 are just the tents its self, tents 7-12 have chairs and tables included.\n')
                print('\n'.join(core.type_of_tents()))
                while True:
                    tent1 = input('Tent: \n')
                    if tent1.strip().isnumeric() and int(tent1) < 13 and int(tent1) > int(0):
                        break
                    elif not tent1.strip().isnumeric():
                        print("\nSorry, invalid choice!")
                        continue
                    elif int(tent1) >= int(13) or int(tent1) <= int(0):
                        print('\nInvalid Tent number.')
                        continue
                    else:
                        print('\nInvalid Choice')
                tents = core.cost_of_tents(tent1)
                actual_price = core.actual_cost(tent1)
                while True:
                    amount = input('\nHow many tents of this type would you like?\n')
                    if not amount.strip().isnumeric():
                        print("\nSorry, invalid choice!")
                        continue
                    elif not disk.take_away(tent1, amount):
                        print('\nSorry we dont have this much tents available.')
                        continue
                    elif amount.strip().isnumeric():
                        break
                    else:
                        print('\nInvalid Choice')
                tent_1 = float(amount) * float(tents)
                tent_actual = float(amount) * float(actual_price)
                while True:
                    con = input('\nTent ' + tent1 + ' price is $' + str(tent_1) + ' dollars. Press "1" to continue.\n')
                    if not con.strip().isnumeric():
                        print('\nInvalid Choice')
                        continue
                    elif con != '1':
                        print("\nInvalid Choice, please enter '1'")
                        continue
                    elif disk.take_away(tent1, amount):
                        break
                    elif con == '1':
                        break
                    else:
                        print('\nInvalid choice')
                tent2 = core.deposit(tent_actual)
                tent3 = core.total(tent_1)
                tent4 = tent_1 * 2
                while True:  
                    days = input('\nHow many days will you be renting this? Only up to 2 days. Please type "1" or "2"\n')
                    total = (float(tent2) + float(tent3)) + float(tent_1)
                    total2 = (float(tent2) + float(tent3)) + float(tent4)
                    if days == '1':
                        print('\nYou are renting this for 1 day')
                        print('Deposit is **10%** of original price which is: $' + str(float(tent2)))
                        print('Sales tax is **7%**: $' + str(float(tent3)))
                        print('Your total with deposit and tax included is: $' + str(float(total)))
                        history = disk.keep_history(tent1, total)
                        print('Thank you')
                        return None
                    elif days == '2':
                        print('\nYou are renting this for 2 days')
                        print('Deposit is **10%** of original price which is: $' + str(float(tent2)))
                        print('Sales tax is **7%**: $' + str(float(tent3)))
                        print('Your total with deposit and tax included is: $' + str(float(total2)))
                        history = disk.keep_history(tent1, total2)
                        print('Thank you')
                        return None
                    else:
                        print('Invalid choice')
    elif rent_return == '2':
        while True:
            type_tent = input('What tents are you returning? From type 1-12.\nTent: ')
            if not type_tent.strip().isnumeric():
                print("Sorry, invalid choice!")
                break
            tents = core.actual_cost(type_tent)
            how_many = input('How many of this tents are you returning?\n')
            if not how_many.strip().isnumeric():
                print("Sorry, invalid choice!")
                break
            u = float(how_many) * float(tents) 
            deposit = core.deposit(u)
            disk.refill(type_tent, how_many)
            print('Thank you! your deposit that you are getting back is $' + str(float(deposit)) + '. Come back for more tents soon!')
            return None







if __name__ == '__main__':
    main() 