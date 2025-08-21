#set problem with updation


set1={10,30,"yes","no"}
print("Before update",set1)
set2={5,10}
set1.update(set2)
print(set1)


#Dictionary
D={"kumar","mayank","chiku","Pankaj"}
print("before update",D)
D1={"June","May","April"}
D.update(D1)
print("After Update",D)


#Integer with udate function
a=500
print("before update",id(a))
a=200
print("after update",id(a))