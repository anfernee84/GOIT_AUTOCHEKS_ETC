from collections import Counter


def get_count_visits_from_ip(ips):
    #cnt = {}
    # for i in ips:
    #     if i in cnt:
    #         cnt[i] += 1
    #     else: 
    #         cnt[i] =1
    # return (cnt)
    return dict(Counter(ips))

    


def get_frequent_visit_from_ip(ips):
    return Counter(ips).most_common(1)[0]

     


t = ["192.168.1.1","8.8.8.8", "95.125.18.12", "8.8.8.8", "192.168.1.1"]

print(get_count_visits_from_ip(t))
print(get_frequent_visit_from_ip(t))














# student_marks = [4, 2, 4, 6, 7, 4, 2 , 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]
# mark_counts = {}
# for mark in student_marks:
#     if mark in mark_counts:
#         mark_counts[mark] += 1
#     else:
#         mark_counts[mark] = 1
# print(mark_counts)  # {4: 4, 2: 2, 6: 3, 7: 2, 3: 2, 5: 2, 1: 3}

# from collections import Counter


# student_marks = [4, 2, 4, 6, 7, 4, 2 , 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]
# mark_counts = Counter(student_marks)
# print(mark_counts) 
# print(mark_counts.most_common(1))  # [(4, 4)]
# print(mark_counts.most_common(3))  # [(4, 4), (6, 3)]