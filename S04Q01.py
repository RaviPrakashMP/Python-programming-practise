Tank_capacity = 900

current_level = int(input("Enter the current Ethanol value:"))

def tank_reading(current_level):
    if 0 < current_level < 180:
        print("send SMS to buy more liquid")

    elif 180 < current_level < 720:
            print("raise an alaram to close the valve")
    
tank_reading(current_level)
