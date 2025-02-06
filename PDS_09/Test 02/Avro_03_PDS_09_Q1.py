inventory = {
    'Apple':{'price':1.2, 'stock':50},
    'Banana':{'price':0.5, 'stock':100},
    'Orange':{'price':0.8, 'stock':80}
}

#add Grapes
inventory['Grapes'] = {'price':2, 'stock':40}

#update Banana
inventory['Banana']['stock'] = 120

#print final inventory
print(inventory)