#Functions Intermediate II
x = [ [5,2,3], [10,8,9] ] 
students_list = [
     {'first_name':  'Michael', 'last_name' : 'Bryant'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Andres', 'Ronaldo', 'Rooney']
}
z = [ {'x': 15, 'y': 30} ]
print(x)

#Iterate Through a List of Dictionaries
def iterateDictionary(some_list):
    for dictionary in some_list:
        for key, value in dictionary.items():
            print(f"{key} - {value}")

# Example list of dictionaries
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

# Call the function with the example list
iterateDictionary(students)

#Get Values From a List of Dictionaries

