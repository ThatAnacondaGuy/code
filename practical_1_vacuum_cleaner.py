def simple_reflex_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Move Right"
    else:
        return "Move Left"


rooms = {"A": "Dirty", "B": "Dirty"}
location = "A"

while "Dirty" in rooms.values():
    status = rooms[location]
    action = simple_reflex_agent(location, status)

    print("Location:", location)
    print("Action:", action)

    if action == "Suck":
        rooms[location] = "Clean"
    elif action == "Move Right":
        location = "B"
    elif action == "Move Left":
        location = "A"

print("Final Room Status:", rooms)
print("Both rooms are clean!")
