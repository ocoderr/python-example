from collections import ChainMap

dict1 = {'a': '1'}
dict2 = {'b': '2'}

dict_all = ChainMap(dict1, dict2)
for key, value in dict_all.items():
    print(key, value)
