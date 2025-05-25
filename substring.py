
def longest(input_str):

  longest = ""
  current = ""

  for char in input_str:
    if not current or char >= current[-1]:
      current += char
    else:
      if len(current) > len(longest):
        longest = current
      current = char

  if len(current) > len(longest):
    longest = current

  return longest

string = 'abdelwahab'
output = longest(string)
print(f"Longest substring : {output}")


