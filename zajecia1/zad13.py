# XIII. Policz, ile cyfr znajduje się w tekście podanym przez użytkownika.
import re

user_input = str(input())

digit_count = len(re.findall("\d", user_input))

print(digit_count)
