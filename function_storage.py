from player_class import *

#Bubble sorting
def bubble_sorting(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if int(array[j].time) > int(array[j+1].time):#This if will sort by Player.time
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

def time_check(time_in,name_in):
    while int(time_in) <= 0:
        print ("Invalid time entry. Try again.")
        time_in = input("Please enter "+ name_in +"'s finish time (in minutes): ")


def user_input(player_amount,player_array):
    for i in range (player_amount):
        i = i+1
        name_in = input("Please enter the name of runner #%d:" % i)
        time_in = input("Please enter "+ name_in + "s finish time (in minutes): ")
        time_check(time_in,name_in)
        player_array[i-1] = Player(name_in,time_in)

def output_result(Medal_array,player_array):
    for i in range(3):
        print (Medal_array[i]," Medal Winner: ",player_array[i].name)
