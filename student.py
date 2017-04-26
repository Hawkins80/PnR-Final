import pigo
import time
import random

'''
MR. A's Final Project Student Helper
'''

class GoPiggy(pigo.Pigo):

    ########################
    ### CONTSTRUCTOR - this special method auto-runs when we instantiate a class
    #### (your constructor lasted about 9 months)
    ########################

    def __init__(self):
        print("Your piggy has be instantiated!")
        # Our servo turns the sensor. What angle of the servo( ) method sets it straight?
        self.MIDPOINT = 90
        # distance before Dex decides to stop
        self.STOP_DIST = 30
        # speed chosen to allow Dex to properly cruise and scan
        self.LEFT_SPEED = 125
        # speed chosen to allow Dex to properly cruise and scan
        self.RIGHT_SPEED = 125
        # This one isn't capitalized because it changes during runtime, the others don't
        self.turn_track = 0
        # Our scan list! The index will be the degree and it will store distance
        self.scan = [None] * 180
        self.set_speed(self.LEFT_SPEED, self.RIGHT_SPEED)
        # let's use an event-driven model, make a handler of sorts to listen for "events"
        while True:
            self.stop()
            self.menu()


    ########################
    ### CLASS METHODS - these are the actions that your object can run
    #### (they can take parameters can return stuff to you, too)
    #### (they all take self as a param because they're not static methods)
    ########################


    ##### DISPLAY THE MENU, CALL METHODS BASED ON RESPONSE
    def menu(self):
        ## This is a DICTIONARY, it's a list with custom index values
        # You may change the menu if you'd like to add an experimental method
        menu = {"n": ("Navigate forward", self.nav),
                "d": ("Dance", self.dance),
                "c": ("Calibrate", self.calibrate),
                "w": ("Sweep", self.sweep),
                "o": ("Count Obstacle", self.count_obstacles),
                "s": ("Check status", self.status),
                "q": ("Quit", quit)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        # store the user's answer
        ans = raw_input("Your selection: ")
        # activate the item selected
        menu.get(ans, [None, error])[1]()

    def count_obstacles(self):
        # run a scan
        self.wide_scan()
        # count how many obstacles found
        counter = 0
        # starting state assumes no obstacle
        found_something = False
        # loop through all my scan data
        for x in self.scan:
            # if x is not None and really close
            if x and x <= self.STOP_DIST:
                # if I've already found something
                if found_something:
                    print("obstacle continues")
                    # if this is a new obstacle
                else:
                    # switch my tracker
                    found_something = True
                    print("start of new obstacle")
            # if my data shows safe distances...
            if x and x > self.STOP_DIST:
                # if my tracker had been triggered
                if found_something:
                    print("end of obstacle")
                    # reset tracker
                    found_something = False
                    # increase count of obstacles
                    counter += 1
        print('Total number of obstacles inn this scan: ' + str(counter))
        return counter

    # full 360 degree sweep with obstacle counter
    def total_obstacles(self):
        counter = 0
        for x in range(4):
            counter += self.count_obstacles()
            self.encR(9)
        print('Total number of obstacles in this scan: ' + str(counter))

    def sweep(self):
        for x in range(self.MIDPOINT - 60, self.MIDPOINT + 60, 2):
            self.servo(x)
            self.scan[x] = self.dist()
        print("Here's what I saw")
        print(self.scan)

    def safety_dance(self):
        for y in range(3):
            for x in range(self.MIDPOINT - 60, self.MIDPOINT + 60,2):
                self.servo(x)
                if self.dist() > 30:
                    print("Lets dance!")
                if self.dist() < 30:
                    print("Abort mission")
                    return
                self.encR(7)
            self.dance()

    def turn_test(self):
        while True:
            ans = raw_input('Turn right, left or stop? (r/l/s): ')
            if ans == 'r':
                val = int(raw_input('/nBy how much?: '))
                self.encR(val)
            elif ans == 'l':
                val = int(raw_input('/nBy how much?: '))
                self.encL(val)
            else:
                break
        self.restore_heading()

    def restore_heading(self):
        print("Now I'll turn back to the starting postion.")
        # make self.turn_track go back to zero
        self.set_speed(90, 90)
        if self.turn_track > 0:
            print('I must have turned right a lot now I should turn left')
            self.encL(abs(self.turn_track))
        elif self.turn_track < 0:
            print('I must have turned left a lot and now I have to self.encR(??)')
            self.encR(abs(self.turn_track))
        self.set_speed(self.LEFT_SPEED, self.RIGHT_SPEED)

    def encR(self, enc):
        pigo.Pigo.encR(self, enc)
        self.turn_track += enc

    def encL(self, enc):
        pigo.Pigo.encL(self, enc)
        self.turn_track -= enc

    # YOU DECIDE: How does your GoPiggy dance?
    def dance(self):
        print("Piggy dance")
        ##### WRITE YOUR FIRST PROJECT HERE

    #YOU DECIDE: How does your GoPiggy dance?
    def dance(self):
        print("Piggy dance")
        ##### WRITE YOUR FIRST PROJECT HERE
        self.twirltwist()
        self.salsa()
        for x in range(3):
            self.getjiggywitit()
        self.rockford()

# start of twirltwist
    def twirltwist(self):
        print('twirltwist')
        for x in range(3):
            self.encL(52)
            self.encR(3)
            self.servo(30)
            self.encL(3)
            self.servo(140)
            self.encR(3)
            self.encL(3)
            self.encR(52)

# start of salsa
    def salsa(self):
        print('salsa')
        for x in range(2):
            self.encF(20)
            self.encR(3)
            self.encL(3)
            self.encR(3)
            self.encL(3)
            self.encB(20)
            self.encR(3)
            self.encL(3)
            self.encR(3)
            self.encL(3)
            self.encR(52)

# start of getjiggywitit
    def getjiggywitit(self):
        print('getjiggywitit')
        for y in range(2):
            for x in range(self.MIDPOINT - 60, self.MIDPOINT + 60,10):
                self.servo(x)
        self.encF(30)
        self.encR(20)
        self.encL(20)
        self.encB(30)

# start of rockford
    def rockford(self):
        print('rockford')
        for x in range(3):
            self.encF(20)
            self.encL(20)
            self.encB(20)
            self.encR(20)

    ########################
    ### MAIN LOGIC LOOP - the core algorithm of my navigation
    ### (kind of a big deal)
    ########################

# navigate forward for Dex
    def nav(self):
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        print("[ Press CTRL + C to stop me, then run stop.py ]\n")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        # this is the loop part of the "main logic loop"
        while True:
            # check if the path is clear
            if self.is_clear():
                self.cruise()
            # Dex chooses path
            answer = self.choose_path()
            # allows Dex to turn left
            if answer == "left":
                self.encL(3)
            # allows Dex to turn right
            elif answer == "right":
                self.encR(3)

# cruise method for Dex
    def cruise(self):
        # look forward
        self.servo(self.MIDPOINT)
        # start driving
        self.fwd()
        counter = 1
        # keep driving as long as distance is safe
        while self.dist() > self.STOP_DIST:
            # hand made counter that allows dex to check his shoulders while driving
            counter += 1
            # check middle if number is divisible by 4
            if counter % 4 == 0:
                self.servo(self.MIDPOINT)
            # check left if number is divisible by 3
            elif counter % 3 == 0:
                self.servo(self.MIDPOINT + 40)
            # check right if number is divisible by 2
            elif counter % 2 == 0:
                self.servo(self.MIDPOINT - 40)
            # if number is not divisible by 4,3, or 2 check middle
            else:
                self.servo(self.MIDPOINT)
        self.stop()
        # if something is seen, move backward
        self.encB(3)

####################################################
############### STATIC FUNCTIONS

def error():
    print('Error in input')


def quit():
    raise SystemExit

##################################################################
######## The app starts right here when we instantiate our GoPiggy

g = GoPiggy()