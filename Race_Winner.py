from function_storage import *

# def decide_playerAmount(player_amount = 0):
#     amount = input("Please enter the amount of players: ")
#     player_amount = int(amount)
#     while player_amount <= 2:
#         print("Invalid amount entry. Please enter amount >= 3. Try again.")
#         amount = input("Please enter the amount of players: ")
#         player_amount = int(amount)
player_amount = 0
# decide_playerAmount(player_amount)
amount = input("Please enter the amount of players: ")
player_amount = int(amount)
while player_amount <= 2:
    print("Invalid amount entry. Please enter amount >= 3. Try again.")
    amount = input("Please enter the amount of players: ")
    player_amount = int(amount)

player_array = [Player("",0)] * player_amount

user_input(player_amount,player_array)
bubble_sorting(player_array)

Medal = ["Gold","Silver","Bronze"]
output_result(Medal,player_array)
