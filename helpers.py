def format_date(date_obj):
    # Define lists for month names and day ordinal numbers
    months = ["null","January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    ordinal_numbers = ["zeroth", "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth",
                    "thirteenth", "fourteenth", "fifteenth", "sixteenth", "seventeenth", "eighteenth", "nineteenth", "twentieth", "twenty-first",
                    "twenty-second", "twenty-third", "twenty-fourth", "twenty-fifth", "twenty-sixth", "twenty-seventh", "twenty-eighth", "twenty-ninth", "thirtieth", "thirty-first"]
    # Extract components from the date object
    year = date_obj.year
    month = date_obj.month
    day = date_obj.day
    # Format the date as a readable text
    return f"{months[month]} the {ordinal_numbers[day]} of {year}"


def format_hour(date,obj):

    return 0