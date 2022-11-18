from practice1 import number_attributes
from practice2 import list_attributes
from practice3 import describe_person

#Indefinite Arguments (**kwargs) Practice #1
# Create a function called number_attributes that counts the number of parameters that are passed, and returns that number as the result.


print(number_attributes(x=1, c=2, d=3))



########################################################################################################################

# Indefinite Arguments (**kwargs) Practice #2
# Create a function called list_attributes that returns in the form of a list the values of the attributes given in the form of keywords. The function must expect to receive any number of arguments of this type.



print(list_attributes(a= 1, b= 2, c=3))



########################################################################################################################

# Indefinite Arguments (**kwargs) Practice #3
# Create a function called describe_person, which takes his name as parameters and then an indeterminate number of arguments. This function should display on the screen:

# Characteristics of {name}:
# {argument_name}: {argument_value}
# {argument_name}: {argument_value}
# etc...
# For example:

# describe_person("Ash", eye_color="brown", hair_color="black")

# Will print to the screen:

# Characteristics of Ash:
# eye_color: brown
# hair_color: black




describe_person("Ash", eye_color="brown", hair_color="black")
  