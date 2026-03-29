def get_above_avg(lst):
    avg = sum(lst) / len(lst)
    print(f"Average: {avg}")
    for num in lst:
        if num > avg:
            yield num

program = get_above_avg([1,9,3,5,4,2])
for i in program:
    print(i)