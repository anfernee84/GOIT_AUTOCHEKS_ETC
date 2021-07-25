import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    
    cats_list = []


    if isinstance(cats[0], dict):
        for i in cats:
            cats_list.append(Cat(**i))
        return cats_list()
    for i in cats:
        cats_list.append(i._asdict())
    return(cats_list)
            

   
        


s = [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]

# s = [
#     {"nickname": "Mick", "age": 5, "owner": "Sara"},
#     {"nickname": "Barsik", "age": 7, "owner": "Olga"},
#     {"nickname": "Simon", "age": 3, "owner": "Yura"},
# ]

print(convert_list(s))                
            
   
  

        
    