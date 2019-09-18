from function_storage import *

player_amount = 4
player_array = [Player("",0)] * player_amount

user_input(player_amount,player_array)
bubble_sorting(player_array)

Medal = ["Gold","Silver","Bronze"]
output_result(Medal,player_array)
