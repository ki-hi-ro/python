def is_anagram(a, b):
  if sorted(a) == sorted(b):
    print(a + 'は、' + b + 'のアナグラム')
  else:
    print(a + 'は、' + b + 'のアナグラムではない')

is_anagram('listen', 'silent')
is_anagram('cat', 'cats')