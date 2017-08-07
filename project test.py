dic = {"A":"Cat","B":"Dog","C":"Fish","D":"Pig","E":"Duck"}
#note: I only defined 5 letters here, but we can define all 26 letters#

user_str=input("please enter a string")
list1=list(user_str)
list2=[[]]*len(list1)

def encrypt(str):
    for i in range (0, len(list1)):
        ## note: we can add some if conditions here since it is required for our final project ###
        list2[i]=(dic[list1[i]])
encrypt(str=user_str)
print(''.join(list2))



