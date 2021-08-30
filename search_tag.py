import difflib
from operator import itemgetter


def tag_search(tags):

    taglist = []
    for i in map(lambda x: x['tag'], notes_list):
        taglist.extend(i)
    taglist = set(taglist)  
    user_tag = input("Enter the tag of notes you would like to find: ")
    tag_list_of_dict = []
    for item in taglist:
        ratio = int(difflib.SequenceMatcher(None, str(user_tag), str(item)).ratio()*100)
        if ratio > 50:
            user_tag = item
            for i in notes_list:
                if user_tag in i['tag']:
                    tag_list_of_dict.append ({ratio : i['note']})
    sort_list = []
    for tag in tag_list_of_dict:
        for key,value in tag.items():
            sort_list.append ({"ratio" : key, "tag" : value})
    newlist = sorted(sort_list, key=itemgetter('ratio'), reverse=True)
    return ([d["tag"] for d in newlist]) if len(newlist) > 0 else f"No such tags in notes"
        

notes_list = [{
        "note":"Information about Vasya`s debt for 150 hryvnias",
        "tag": ["debt", "hryvnia", 150]},
    {
        "note":"Next Tuesday is chief`s birthday",
        "tag": ["birthday", "Tuesday", "Next"]},
    {
        "note": "We need to cooperate by 1000 dollars and make a bribe for governor`s birthday next month",
        "tag" : ["next", "Birthday", 1000]}]
print (tag_search(notes_list))

