def city_country(name, country):
    city = f'"{name.title()}, {country.title()}"'
    return city
city_names = city_country('new-york', 'united states')
print(city_names)
