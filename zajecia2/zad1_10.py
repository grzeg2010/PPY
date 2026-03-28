def main():
    wins = {"Adam": 5, "Bartek": 3, "Cezary": 5, "Damian": 1, "Edward": 2, "Franek": 3, "Grzegorz": 4, "Henryk": 7}

    winners_by_wins_count = {}

    for name, count in wins.items():
        if count not in winners_by_wins_count:
            winners_by_wins_count[count] = []
        winners_by_wins_count[count].append(name)

    print(winners_by_wins_count)

    for count, names in sorted(winners_by_wins_count.items()):
        print(f"{count} zwycięstw: {', '.join(names)}")

    # TODO another half of the task

if __name__ == "__main__":
    main()
