names = ["Jarek", "Anna", "Jakub", "Bartosz", "Grzegorz", "Zuzanna", "Jarek", "Urszula", "Basia", "Marysia", "Basia", "Marysia", "Jarek"]

def get_names_lengths():
    lengths = []

    for name in names:
        lengths.append(len(name))

    return lengths
#end print_names_lengths

def get_names_list_map():
    names_map = dict()

    for name in names:
        length = len(name)
        if length not in names_map:
            names_map[length] = []
        names_map[length].append(name)

    return names_map

def get_names_set_map():
    names_map = {}

    for name in names:
        length = len(name)
        if length not in names_map:
            names_map[length] = set()
        names_map[length].add(name)

    return names_map

def get_name_occurrences():
    occurrences_map = {}

    for name in names:
        if name not in occurrences_map:
            occurrences_map[name] = 0
        occurrences_map[name] += 1

    return occurrences_map

def main():
    print(get_names_lengths())
    print(get_names_list_map())
    print(get_names_set_map())
    print(get_name_occurrences())
#end main

if __name__ == "__main__":
    main()