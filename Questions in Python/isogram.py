def is_isogram(string):
  stringls = string.lower().strip()
  retorno=1
  for i in range(0,len(stringls)):
    if stringls[i] != " " and stringls[i]!= "-":
      if stringls.count(stringls[i]) > 1:
        return False
      else:
        retorno = 1
  if retorno == 1:
    return True        



print(is_isogram(""))

'''
Determine if a word or phrase is an isogram.

An isogram (also known as a "nonpattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.

Examples of isograms:

- lumberjacks
- background
- downstream
- six-year-old

The word *isograms*, however, is not an isogram, because the s repeats.
'''

