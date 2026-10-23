day = input("Inserire il giorno della settimana\n")

match (day):
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday": 
        print("Weekday")
    case "Saturday" | "Sunday":
        print("Weekend")