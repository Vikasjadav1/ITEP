'''
Safely retrieve a value from a deeply nested dictionary. If any key is
    missing, return a default value such as "Unknown".'''



d={
    'user':{
        'profile':{
            'name':"vikas"
        }
    }
}

level1=d.get("user",{})
level2=level1.get("profile",{})
ans=level2.get("name","unknown")
print(ans)