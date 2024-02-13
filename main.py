with open('books/frankenstein.txt') as f:
  file_contents = f.read()
  words = file_contents.split()
  print(f'--- Begin report of books/frankenstein.txt ---\n{len(words)} words found in the document\n')

  def charsCount(str):
    chars = {}
    for char in str:
      low = char.lower()
      if low in chars and low.isalpha():
        chars[low] += 1
      elif low.isalpha():
        chars[low] = 1
    charsList = []
    for char in chars:
      charsList.append({'char': char, 'count': chars[char]})
    return charsList

  def sort_on(dict):
    return dict['count']

  characters = charsCount(file_contents)
  characters.sort(reverse=True, key=sort_on)
  for c in characters:
    print(f"The '{c['char']}' character was found {c['count']} times")
  print('--- End of Report ---')