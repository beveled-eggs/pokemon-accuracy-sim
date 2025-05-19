import numpy as np

function_dict = {
"1": "Safety Calculator",
"2": "Use Until Miss"
}
move_dict = {
"1": "Hydro Pump",
"2": "Thunder Wave",
"3": "Fissure",
"4": "Tackle",
"5": "Air Slash",
"6": "Dark Void"
}
acc_dict = {
"Hydro Pump": 70,
"Thunder Wave": 90,
"Fissure": 30,
"Tackle": 100,
"Air Slash": 95,
"Dark Void": 50
}

#simple dice roll | parameter is number of faces
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
def first_miss(accuracy):
    if accuracy == 100:
        print("move will not miss")
        return
    hits = 0
    miss = False
    while miss == False:
        roll_check = roll(100)
        if  roll_check > accuracy:
            miss = True
        else:
            hits += 1
    print(move + " successfully hit " + str(hits) + " times")

move_list = {"hydro_pump", "tbolt", "fissure", "tackle"}

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
    safe_calc(move_acc,10,100000)
elif function == "2":
    first_miss(move_acc)
else:
    print("function undefined")
    
input("Press enter to close window")