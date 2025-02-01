#Dictionary
#creating dictionary
my_list = [{"name":"Tom","age":13},{"name":"Peter","age":23},{"name":"Manual","age":17},{"name":"Emil","age":26},{"name":"Ray","age":20}]
#Filtering people less than 18
result1=filter(lambda people:people["age"]>=18,my_list)
#Maping the remaining names to new list
result2=list(map(lambda people:people["name"],result1))
print(result2)