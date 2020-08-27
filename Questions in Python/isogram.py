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

