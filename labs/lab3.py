## Write 6 functions for conversion 
def days2years(days):
    return days / 365.25

def days2weeks(days):
    return days / 7.0

def days2hours(days):
    return days * 24.0

def days2minutes(days):
    return days * 24 * 60.0

def days2seconds(days):
    return days * 24 * 60 * 60.0

def days2milliseconds(days):
    return days * 24 * 60 * 60 * 1000.0

def print_conversions(days):
    print(days2years(days), "years")
    print(days2weeks(days), "weeks")
    print(days2hours(days), "hours")
    print(days2minutes(days), "minutes")
    print(days2seconds(days), "seconds")
    print(days2milliseconds(days), "milliseconds")
    
    

## Write print_conversions

# Write main
def main():
    print("days?")
    days = int(input())
    print_conversions(days)

# Make sure main gets called first
if __name__ == "__main__":
    main()
