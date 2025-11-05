def get_day_name(day_number):
    days = ["sunday", "monday", "Tuesday", "Wednesday", "Thursday", "Friday", "saturday"]
    if 1 <= day_number <= 7:
        return days[day_number - 1]
    else:
        return("Invalid day number please enter a number between 1 and 7")
