import csv
import statistics
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    # """Takes a temperature and returns it in string format with the degrees
    #     and celsius symbols.

    # Args:
    #     temp: A string representing a temperature.
    # Returns:
    #     A string contain the temperature and "degrees celsius."
    # """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    return datetime.fromisoformat(iso_string).strftime("%A %d %B %Y")
    # """Converts and ISO formatted date into a human readable format.

    # Args:
    #     iso_string: An ISO date string..
    # Returns:
    #     A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    # """
    # pass


def convert_f_to_c(temp_in_fahrenheit):
    return round(((float(temp_in_fahrenheit) - 32) * 5/ 9), 1)

    # """Converts an temperature from Fahrenheit to celsius.

    # Args:
    #     temp_in_fahrenheit: float representing a temperature.
    # Returns:
    #     A float representing a temperature in degrees celsius, rounded to 1dp.
    # """
    # pass

def calculate_mean(weather_data):
    # return statistics.mean(map(float,weather_data))
    data = list(map(float, weather_data))
    total = 0.0
    for i in data:
        total += i
    mean = total / len(data)
    return mean

# """Calculates the mean wdata from a list of numbers.

# Args:
#     weather_data: a list of numbers.
# Returns:
#     A float representing the mean wdata.
# """
# pass

def load_data_from_csv(csv_file):
    with open(csv_file) as file:
        reader = csv.reader(file)
        next(file)
        data_list = []
        for row in reader:
            if row != []:
                list = [row[0], int(row[1]), int(row[2])]
                data_list.append(list)
        return data_list

# print(load_data_from_csv("example_one"))
# """Reads a csv file and stores the data in a list.

# Args:
#     csv_file: a string representing the file path to a csv file.
# Returns:
#     A list of lists, where each sublist is a (non-empty) line in the csv file.
# """
# pass


def find_min(weather_data):
    # min_number = min(data)
    # index = data.index(min_number)
    # return min_number, index
    data = list(map(float, weather_data))
    if weather_data:
        min_number = None
        for i in data:
            if min_number is None or i < min_number:
                min_number = i
        for j in range(len(data)):
            if data[j] == min_number:
                index = j
        return min_number, index            
    else:
        return()

# print(find_min([3, 7, 5, 3, 2, 8, 2]))

#     """Calculates the minimum wdata in a list of numbers.

#     Args:
#         weather_data: A list of numbers.
#     Returns:
#         The minium wdata and it's position in the list.
#     """
#     pass


def find_max(weather_data):
    data = list(map(float, weather_data))
    if weather_data:
        max_number = None
        for i in data:
            if max_number is None or i > max_number:
                max_number = i
        for j in range(len(data)):
            if data[j] == max_number:
                index = j
        return max_number, index            
    else:
        return()

# print(find_max([3, 7, 8, 3, 2, 8, 2]))

    # """Calculates the maximum wdata in a list of numbers.

    # Args:
    #     weather_data: A list of numbers.
    # Returns:
    #     The maximum wdata and it's position in the list.
    # """
    # pass

def generate_summary(weather_data):
    num_days = len(weather_data)
    # date_list = []
    # min_list = []
    # max_list = []
    # for value in weather_data:
    #     date_list.append(value[0])
    #     min_list.append(value[1])
    #     max_list.append(value[2])
    date_list = [value[0] for value in weather_data]
    min_list = [value[1] for value in weather_data]
    max_list = [value[2] for value in weather_data]
    min_val, min_index = find_min(min_list)
    max_val, max_index = find_max(max_list)
    min_temp = format_temperature(convert_f_to_c(min_val))
    max_temp = format_temperature(convert_f_to_c(max_val))
    min_date = convert_date(date_list[min_index])
    max_date = convert_date(date_list[max_index])
    min_mean = format_temperature(convert_f_to_c(calculate_mean(min_list)))
    max_mean = format_temperature(convert_f_to_c(calculate_mean(max_list)))
    return f"{num_days} Day Overview\n  The lowest temperature will be {min_temp}, and will occur on {min_date}.\n  The highest temperature will be {max_temp}, and will occur on {max_date}.\n  The average low this week is {min_mean}.\n  The average high this week is {max_mean}.\n"

doc = load_data_from_csv('./tests/data/example_one.csv')
print(generate_summary(doc))
print(len(doc))

#     """Outputs a summary for the given weather data.

#     Args:
#         weather_data: A list of lists, where each sublist represents a day of weather data.
#     Returns:
#         A string containing the summary information.
#     """
#     pass


def generate_daily_summary(weather_data):
    summary = ""
    for wdata in weather_data:
        date = convert_date(wdata[0])
        min_temp = format_temperature(convert_f_to_c(wdata[1]))
        max_temp = format_temperature(convert_f_to_c(wdata[2]))
        summary += f"---- {date} ----\n  Minimum Temperature: {min_temp}\n  Maximum Temperature: {max_temp}\n\n"
    return summary

doc = load_data_from_csv('./tests/data/example_one.csv')
generate_daily_summary(doc)

#     """Outputs a daily summary for the given weather data.

#     Args:
#         weather_data: A list of lists, where each sublist represents a day of weather data.
#     Returns:
#         A string containing the summary information.
#     """
#     pass
