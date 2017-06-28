print("Hello World!")
start = '''
As you were taking a hike, you realized that you had gone off the trail. You
begin to walk back when all of a sudden, you stumble across a river which
holds a bridge. It's up to you to find your way back.
You could either walk straight across the bridge or swim across the river.
'''


print(start)


print("Type 'walk' to go over bridge or 'swim' to go across water.")
user_input = input()
while not (user_input == "walk" or user_input == "swim"):
    print("Error:Type 'walk' to go over bridge or 'swim' to go across water.")
    user_input = input()
if user_input == "walk":
        print("You decide to walk over bridge and face a bear") # finished the story by writing what happens
        print("attack or run?")
        user_input = input()
        while not (user_input == "attack" or user_input == "run"):
            print ("Error: attack or run?")
            user_input = input()
        if user_input =="attack":
            print("Congratulations!The bear was no match for you. SAVAGE.")
        elif user_input =="run":
            print("You can't outrun a bear!R.I.P. TO THE PERSON WHO THOUGHT THEY WERE BETTER THAN A BEAR.RAWR.")
elif user_input == "swim":
    print("You choose to swim under the bridge and face a shark.") # finished the story writing what happens
    print("swim or attack?")
    user_input = input()
    while not(user_input == "swim" or user_input == "attack"):
        print ("Error: swim or attack?")
        user_input = input()
    if user_input == "swim":
        print("Congratulations! You outswam the shark. Michael Phelps is that you?!")
    elif user_input =="attack":
        print("You can't beat a shark,you thought! R.I.P. GAME OVER")
