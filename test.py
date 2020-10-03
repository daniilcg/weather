#Free bashkort colorfull weather 4u! ))
from colorama import Fore, Back
from colorama import init
from pyowm import OWM

owm = OWM('8f6611365be0d454706879c56e08b956')
def calculate():
    init()
    print ( Back.CYAN, Fore.BLACK )
    place = input ( "Hi, I can show you the weather today. Just type here - where? city/region: " )
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]
    wi = w.wind()
    hum = w.humidity
    print ( Back.WHITE, Fore.BLACK )
    print ( "In " + place + " now: ")
    print ( "Temperature: " + str (temp)) 
    print ( "Wind: " + str (wi))
    print ( "Humidity: " + str (hum))

    print ( Back.GREEN, Fore.BLACK )
    if temp < 0:
        print ("It's cold, take a vodka and sit at home!")
    elif temp < 15:
        print ("Now it's cold, but you can walk, just take a jacket!")
    elif temp < 30:
        print ("Temperature is warm! Go walk and don't care about wear!")
    else:
        print ("WOW ITS HOT! Looks like BBQ! =)")
    
    return play_again()

def play_again():
    while True:
        again = input('More? [y/n]: ')
        if again not in {"y","n"}:
            print("Error! Please enter valid input!")
        elif again == "n":
            print ("Thank you, bye! Copyright by")
        elif again == "y":
    # call function to start the calc again
            return calculate()
calculate()