
# Find Duplicate in the list 

# def main(list1):
#  print("Original List is")
#  print(list1)
#  distinct_list=list(set(list1))
#  print("Distinct list is ")
#  print(distinct_list)




# main([1,2,4,3,4,4])


# print dictionaries with key

# def main():
#  students=[
#     {'name':'alice','age':23,'major':'Physics','key':'NU'},
#     {'name':'bob','age':12,'major':'Math','key':'NU'},
#     {'name':'trisca','age':34,'major':'Nothing'},
#  ]
#  new=[]
#  for student in students:
#   if 'key' in student:
#    new.append(student)
 
#  print(new)



# Combine dictionaries


# def main(d1,d2):
#  print("In main function")
#  d3=d2.copy()
#  print("1")
#  print(d3)
#  d3.update(d1)
#  print("2")
#  print(d3)




# if __name__=="__main__":
#     students={'name':'alice','age':23,'major':'Physics','key':'NU','num':2323}
#     teachers={'name':'oll','age':23,'major':'Physics1','key':'NU'}
 
#     main(students,teachers)    

# most often values in dictionary

# ????


# uniqe values in dictionary

# def main(d1):

#    values=d1.values()
#    new=set(values)
#    print(new)



# if __name__=="__main__":
#     students={'name':'alice','age':23,'major':'Physics','key':'NU','num':23}
    

#     main(students) 





# Union and Intersection of Sets



# def main(st,tech):
#     new=st | tech
#     print("U")
#     print(new)
#     new= st & tech
#     print("I")
#     print(new)
    

# if __name__=="__main__":
#     students={'alice',23,'Physics','key',23}
#     tech={'alice',56,'Math','new',34}
    

#     main(students,tech) 



# Count Distinct Elements

from collections import Counter
def main(list):

    nums=Counter(list)
    for element,count in nums.items():
        if count==1:
            print(element)
    





main([1,2,3,2,2,4])