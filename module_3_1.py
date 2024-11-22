calls = 0

def count_calls():
    global calls
    calls += 4
    return


def string_info(string):
    length = len(string)
    uppercase = string.upper()
    lowercase = string.lower()

    result = (length, uppercase, lowercase)
    return result


def is_contains(string, list_to_search):
    for i in list_to_search:
        if string in i:
            return True
    return False


count_calls()
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)



