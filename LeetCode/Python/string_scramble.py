def StringScramble(str1,str2):

  list1 = set(list(str1))
  list2 = set(list(str2))
  list3 = list1.intersection(list2)
  s = "".join(sorted(list3))
  s1 = "".join(sorted(list2))
  if s == s1:
    return "true"
  else:
    return "false"

# keep this function call here 
s1 = str(input())
s2 = str(input())
print(StringScramble(s1, s2))