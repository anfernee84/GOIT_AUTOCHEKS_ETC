import difflib
from operator import itemgetter


def tag_search(tags):

    taglist = []
    for i in map(lambda x: x['tag'], tags):
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


def note_search(notes):
    find_notes = []
    searchstring = input("Enter a name of your note: ")
    for note in notes:
        for i,j in note.items():
            ratio = int(difflib.SequenceMatcher(None, str(searchstring), str(j)).ratio()*100)
            if ratio == 100 and len(j) == len(searchstring):
                find_notes.append(note)
    if len(find_notes) > 0:
        return(find_notes)
    return f"No such notes"


def edit_note(notes):
    searchID = int(input("Enter an ID of note you want to edit: "))
    new_tag_list = []
    for note in notes:
        for i,j in note.items():
            if searchID == j:
                note["note"] = input("Input new information: ")
                tag_string = input("Input new tags, separated with space (' '): ")
                for word in tag_string.split(' '):
                    new_tag_list.append(word)
                note["tag"] = new_tag_list
                return(notes)
    return f"No such ID`s"

       

def note_remove(notes):

    searchID = int(input("Enter an ID of note you want to delete: "))
    for note in notes:
        for i,j in note.items():
            if searchID == j:
                notes.remove(note)
                return(notes)
    return f"No such ID`s"

      

notes_list = [{
        "id" : 1,
        "note":"Next Tuesday is chief`s birthday",
        "tag": ["debt", "hryvnia", 150]},
    {
        "id" : 2,
        "note":"Next Tuesday is chief`s birthday",
        "tag": ["birthday", "Tuesday", "Next"]},
    {   
        "id" : 3,
        "note": "We need to cooperate by 1000 dollars and make a bribe for governor`s birthday next month",
        "tag" : ["next", "Birthday", 1000]}]
        
print (edit_note(notes_list))


