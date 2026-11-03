# 5-1: sepuluh tes dasar
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
 
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
 
print("\nIs car != 'audi'? I predict True.")
print(car != 'audi')
 
print("\nIs car != 'subaru'? I predict False.")
print(car != 'subaru')
 
print("\nIs 5 == 5? I predict True.")
print(5 == 5)
 
print("\nIs 5 == 6? I predict False.")
print(5 == 6)
 
print("\nIs 'a' < 'b'? I predict True.")
print('a' < 'b')
 
print("\nIs 'a' > 'b'? I predict False.")
print('a' > 'b')
 
print("\nIs 10 > 3? I predict True.")
print(10 > 3)
 
print("\nIs 10 < 3? I predict False.")
print(10 < 3)
 
# 5-2: tes tambahan
print("\n--- 5-2 ---")
print("\nString equality / inequality")
print(car == 'subaru')
print(car != 'subaru')
 
print("\nlower()")
name = 'Eric'
print(name.lower() == 'eric')
print(name.lower() == 'ERIC')
 
print("\nNumerical tests")
age = 20
print(age == 20)
print(age != 20)
print(age > 18)
print(age < 18)
print(age >= 20)
print(age <= 19)
 
print("\nand / or")
print(age > 18 and age < 30)
print(age > 18 and age < 20)
print(age < 18 or age == 20)
print(age < 18 or age > 30)
 
print("\nin / not in list")
cars = ['subaru', 'audi', 'bmw']
print('audi' in cars)
print('toyota' in cars)
print('toyota' not in cars)
print('audi' not in cars)