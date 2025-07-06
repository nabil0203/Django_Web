import collections


word_dic = collections.defaultdict(list)                # each key of the Dictionary will have values as a LIST


word_dic['Python'].append("PROGRAMMING")                # key: Python---->value: PROGRAMMING, LANGUAGE
word_dic['Python'].append("LANGUAGE")

word_dic['Name'].append("Nabil")                        # key: Name---->value: Nabil, Ahmed
word_dic['Name'].append("Ahmed")


print(word_dic)