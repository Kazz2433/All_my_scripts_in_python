from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("Qual o seu nome ")
    if first == 'q':
        break
    last = input("last name ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first,last)
    print('\tFormatted name is '+formatted_name)