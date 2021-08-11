from collections import UserDict, UserList, UserString


# class VSD(UserDict):
#     def has_in_values(self,value):
#         return value in self.data.values()



# as_dict = VSD()
# as_dict["a"] = 1
# print(as_dict.has_in_values(1))
# print(as_dict.has_in_values(2))


# class CountableList(UserList):
#     def summ(self):
#         return sum(map(lambda x: int(x), self.data))
    

# cntble = CountableList ([1,"2",3,"4"])
# cntble.append("5")
# print(cntble.summ())


# class TruncatedString(UserString):
#     MAX_LEN = 7
#     def truncate(self):
#         self.data = self.data[:self.MAX_LEN]
    
# ts = TruncatedString("abcdefghijklmnop")
# ts.truncate()
# print(ts)


class LookUpKeyDict(UserDict):
    def lookup_key(self,value):
        return list(filter(lambda x: self.data[x] == value, self.data))

lookdict = LookUpKeyDict({12:18, 11:34})
print(lookdict.lookup_key(18))


class AmountPaymentList(UserList):
    def amount_payment(self):
        # return sum(list(x for x in self.data if x >0))
        return sum(list(filter(lambda x: x > 0, self.data)))

amount = AmountPaymentList([1,-3,4])
print(amount.amount_payment())


class NumberString(UserString):
    def number_count(self):
        #return len(list(x for x in self.data if x.isdigit()))
        return len(list(filter(lambda x: x.isdigit(), self.data)))


string = NumberString("wgf34g39")
print(string.number_count())