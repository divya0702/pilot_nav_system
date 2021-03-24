#Pilot nav system
#You are the pilot, your need to land it in the upcoming airport
#For landing the plane, you need to attain the altitude of 3000ft, which is safe for landing
#If your plane is above 3000ft and below 6000ft, atleast allow the pilot to try for landing "Come down to 3000 and open landing gear!"
#If your plane is above 6000ft, don't allow the pilot to land the plane and ask "Go around"
#The user will enter the altitude of the plane
print('Hello Pilot! Ready to land? Provide us with the info of the altitude for optimal landing')
altitude = input('Enter the altitude (in ft):')
al = int(altitude)
if al == 3000:
    print("You are good to go! It is safe for landing.")
elif al > 3000 and al < 6000:
    print ("Come to 3000ft and open landing gear!")
elif al > 6000:
    print("Go around.")