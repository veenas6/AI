def vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location =="A":
        return "Move Right"
    elif location =="B":
        return "Move Left"

print ("Vacuum Cleaner World")

location = input("Enter current location(A/B): ").upper()
status = input("Enter room status (Clean/Dirty): ").capitalize()

action = vacuum_agent(location,status)

print("\nCurrent Location :", location)
print("Room Status :", status)
print("Action Performed :", action)