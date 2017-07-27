import time
import core

def main():
    print("\t\tWelcome to AZ's Canopy Party Tents Rental!\n")
    time.sleep(1)
    print("Canopy tents are a light weight structure, they are great for protection from sun or light rain. They are to be installed and removed by you, the renter.\n")
    time.sleep(1)
    tent = input('Canopy tents are available to rent up to 3 days. Would you like to rent a tent or tents today? 1: yes 2: no\n')
    if tent == '2':
        print("That's fine, come back again if you change your mind!")
     
    elif tent == '1':
            print('Great, here are the tent sizes we have available. You can choose to just rent the tent or have chairs and tables included with them.\n')
            print('\n'.join(core.type_of_tents()))
            tent1 = input('Tent:')
            tents = core.cost_of_tents(tent1)
            print('Tent ' + tent1 + ' price is $' + str(tents) + ' dollars.\n')
            


    








if __name__ == '__main__':
    main() 