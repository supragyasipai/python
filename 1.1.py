# data={3,4,5,4,3}
# print(data)
# print(type(data))

data={
    'name' : 'Supragya',
    'age' : 17,
    'contact' : {
        'email': 'supragya@gmail.com',
        'phone':{
            'home': 7654445,
            'office' : 5765767889
        }
    }
}

print(data['contact']['phone']['home'])
print(data['contact']['phone']['office'])

print(data.get('names','key not found'))

print(data.keys())
print(data.values())

# opperator