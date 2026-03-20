em_dict = {}
print(type(em_dict))

person = {"name": "vignesh", "lastName": "Kumar", "city": "chennai"}
print(person)
print(person.get("city"))
print(person.get("age", "unknown"))

person["phone"] = "+9191919191"
print(person)
person["phone"] = "+9191"
print(person)

editing = {"city": "Madurai", "occ": "SW"}

person.update(editing)
print(person)

del person["occ"]
print(person)

pop_operation = person.pop("phone")
print(person)
print(pop_operation)
