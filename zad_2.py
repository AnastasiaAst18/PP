def create_person(first_name, last_name, age = 30, city = "Warszawa"):
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "city": city
    }
print(create_person("Jan", "Kowalski"))
print(create_person("Anna", "Nowak", 25, "Kraków"))