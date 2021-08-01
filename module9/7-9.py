def normal_name(list_name):
    # s = []
    # for i in map(lambda x: x.capitalize(), list_name):
    #     s.append(i)
    return [i for i in map(lambda x: x.capitalize(), list_name)]





name = ["dan", "jane", "steve", "mike"]
print(normal_name(name))