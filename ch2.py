
#ounces = input('Weight in ounces?')
#grams = int(ounces) 15
#x = grams * 28.3495 
#print('Weight in grams is ' + str(x)) 

#age = input('How old are you?')
#years = int(age)
#if years < 18:
 #   print('dang you a child')
#else:
 #   print('ok u old')



#valid = False
#while valid == False:
   # gender = input('Please enter Male, Female or Other' + '\n')
    #if gender.lower() == 'male':
        #print("Male entered")
        #valid = True
    #elif gender.lower() == 'female':
        #print("Female entered")
        #valid = True
   # elif gender.lower() == 'other':
        #print("Other entered")
        #valid = True
   # else:
  #      print("Please select a valid options")

valid = False
while valid == False : 
    movies = input('Do you prefer horror movies or romcoms?')
    genre = str(movies)
    if genre.lower() == 'horror':
        print('ooh spooky')
        valid = True
    elif genre.lower() == 'romcom':
        print('Hell yeah')
        valid = True 
    else:
        print('Pick from the list!!')
