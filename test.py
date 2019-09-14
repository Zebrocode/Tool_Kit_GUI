str = "yang    shang"
list = str.split(' ')
print(list)

dict={'yang':'shang','xu':'shang','key':'shang'}
dict_reverse={}
#所有键对应的value都初始化成list
for key,value in dict.items():
    if value in dict_reverse.keys():
        dict_reverse[value].append(key)
    else:#未出现过则初始化成列表
        dict_reverse.setdefault(value,[]).append(key)


#这种初始化方法将只有一个value的键对应的这个value初始化成str
for key,value in dict.items():
    if value in dict_reverse.keys():
        if type(dict_reverse[value]) == type(" "):
            list = []
            list.append(dict_reverse[value])
            list.append(key)
        else:
            dict_reverse[value].append(key)
        dict_reverse.update({value:list})
    else:
        dict_reverse[value]=key
print(dict_reverse)
# if value in dict_reverse.keys:
            # dict_reverse[value].extend(key)
        # else:
            # dict_reverse[value]=key