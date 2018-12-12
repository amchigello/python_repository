import json

menu = '''{
   "food":[
      {
         "name":"Pad Thai",
         "type":"Noodles",
         "variety":[
            "Veg",
            "Chicken",
            "Sea Food",
            "Mixed"
         ],
         "spicy":true,
         "cuisine":"Thai"
      },
      {
         "name":"Biriyani",
         "type":"Rice",
         "variety":[
            "Veg",
            "Chicken",
            "Mutton"
         ],
         "spicy":true,
         "cuisine":"Indian"
      },
      {
         "name":"Pho",
         "type":"Soup",
         "variety":[
            "Veg",
            "Chicken",
            "Sea Food"
         ],
         "spicy":true,
         "cuisine":"Indonesian"
      },
      {
         "name":"Supreme Chicken",
         "type":"Starter",
         "variety":[
            "Chicken"
         ],
         "spicy":false,
         "cuisine":"Chinese"
      },
      {
         "name":"Chilly Chicken",
         "type":"Starter",
         "variety":[
            "Chicken"
         ],
         "spicy":true,
         "cuisine":"Chinese"
      }
   ]
}'''

data = json.loads(menu)
# print(type(data))
print(data['food'][0])

#############################
######Conversion Table#######
#############################
#-JSON-----##----python----##
#object----##--dict--------##
#array-----##--list--------##
#string----##--str---------##
#number----##--int---------##
#real------##--float-------##
#true------##--True--------##
#false-----##--False-------##
#null------##--None--------##
#############################
