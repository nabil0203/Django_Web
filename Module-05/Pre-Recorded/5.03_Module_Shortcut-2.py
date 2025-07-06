# Same as 5.03_Collections_Module-4.py
# Change in import sytle



from collections import defaultdict as dct                      # imported 'defaultdict' as dct



word_dic = dct(list)                                             # imported 'defaultdict' as dct

word_dic['Python'].append("PROGRAMMING")                
word_dic['Python'].append("LANGUAGE")

word_dic['Name'].append("Nabil")                       
word_dic['Name'].append("Ahmed")


print(word_dic)