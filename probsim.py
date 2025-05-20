import numpy as np

#dictionaries for easily adding more function and move options
function_dict = {
"1": "Use Until Miss",
"2": "Use Until Hit",
"3": "Average Hits",
"4": "Average Misses",
"5": "Safety Calculator"
}
move_dict = {
"1": "Hydro Pump",
"2": "Thunder Wave",
"3": "Fissure",
"4": "Tackle",
"5": "Air Slash",
"6": "Dark Void",
"7": "Blizzard"
}
acc_dict = {
"Hydro Pump": 80,
"Thunder Wave": 90,
"Fissure": 30,
"Tackle": 100,
"Air Slash": 95,
"Dark Void": 50,
"Blizzard": 70
}

#mode switcher for functions later
data_only = False

#simple dice roll | parameter is number of faces | used for every probability function
def roll(dice):
    return np.random.randint(dice) + 1

#try-except block to allow only integer input
#not used
def input_check(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

#checks that item exists in given dictionary | 1st parameter is item to look for, 2nd is the dict ot look in
def dict_check(item, dict):
    return any(x in item for x in dict)

#averages hit rate of moves | 1st parameter is accuracy of move, 2nd is times executed
#the value just approaches the move's accuracy as rolls reach infinity
#not used
def hit_test(accuracy, rolls):
    tries = 0
    hit_list = 0
    while tries < rolls:
        roll_check = roll(100)
        if roll_check <= accuracy:
            hit_list += 1
        tries += 1
    return hit_list / rolls * 100

#runs a "safety test of a move" | 1st parameter is accuracy of move, 2nd is times executed
#returns True only if every instance of the move hits
#building block for "Safety Calculator" function
def safe_test(accuracy, rolls):
    miss = False
    tries = 0
    while tries < rolls:
        roll_check = roll(100)
        if  roll_check > accuracy:
            miss = True
        tries += 1
    return not miss

#averages the amount of positive "safety checks"
#1st accuracy of move, 2nd times executed in safety check,
#3rd is the scrutiny or amount of safety checks executed
def safe_calc(accuracy, rolls, scrutiny):
    print("a move is 'safe' if it hits 10 time in succession")
    print("working...")
    safeties = 0
    trial = 0
    while trial < scrutiny:
        if safe_test(accuracy, rolls):
            safeties += 1
        trial += 1
    print(move + " is 'safe' " + str(round((safeties / scrutiny * 100),3)) + "% of the time")

#simulates how many tries until a miss | parameter is accuracy of move
#this function is "Use Until Miss" and a building block for "Average Hits"
def first_miss(accuracy):
    if accuracy == 100:
        print("move will not miss")
        return
    times_hit = 0
    miss = False
    while miss == False:
        roll_check = roll(100)
        if  roll_check > accuracy:
            miss = True
        else:
            times_hit += 1
    if data_only == False:
        print(move + " successfully hit " + str(times_hit) + " times")
    else:
        return times_hit
    
#simulates how many tries until a hit | parameter is accuracy of move
#this function is "Use Until Hit" and a building block for "Average Misses"
def first_hit(accuracy):
    if accuracy == 0:
        print("move will always miss")
        return
    times_missed = 0
    miss = True
    while miss == True:
        roll_check = roll(100)
        if  roll_check > accuracy:
            times_missed += 1
        else:
            miss = False
    if data_only == False:
        print(move + " missed " + str(times_missed) + " times until successful hit")
    else:
        return times_missed

#averages how many times a move hits before it misses
def avg_hit(accuracy, scrutiny):
    print("working...")
    misses = 0
    trial = 0
    while trial < scrutiny:
        misses += first_miss(accuracy)
        trial += 1
    print(move + " hits successfully an average of " + str(round((misses / scrutiny),3)) + " times before missing")

#averages how many times a move misses before it hits
def avg_miss(accuracy, scrutiny):
    print("working...")
    hits = 0
    trial = 0
    while trial < scrutiny:
        hits += first_hit(accuracy)
        trial += 1
    print(move + " misses an average of " + str(round((hits / scrutiny),3)) + " times before hitting successfully")

#loops for prompting and checking function and move input
Selecting = 0
list_value = 1
print("select a function: ")
for x in function_dict:
    print(str(list_value) + ". " + str(function_dict[x]))
    list_value += 1
while Selecting < 1:
    function = input("function: ")
    if not dict_check(function, function_dict):
        print("invalid selection")
        continue
    Selecting += 1
print("select a move: ")
list_value = 1
for x in move_dict:
    print(str(list_value) + ". " + str(move_dict[x]))
    list_value += 1
while Selecting < 2:
    move = input("move: ")
    if not dict_check(move, move_dict):
        print("invalid selection")
        continue
    Selecting += 1
 
#executes function based on selection
move = move_dict[move]
move_acc = acc_dict[move]
if function == "1":
    data_only = False
    first_miss(move_acc)
elif function == "2":
    data_only = False
    first_hit(move_acc)
elif function == "3":
    data_only = True
    avg_hit(move_acc, 100000)
elif function == "4":
    data_only = True
    avg_miss(move_acc, 100000)
elif function == "5":
    safe_calc(move_acc, 10, 100000)
else:
    print("function undefined")
    
input("Press enter to close window")