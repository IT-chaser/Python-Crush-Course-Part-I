def get_formatted_city_country_name(city_name, country_name, population =''):
    """Generate fully formatted city and contry name"""
    if population:
        formatted_city_country_name = f"{city_name}, {country_name} - "
        formatted_city_country_name += f"population {population}"
    else:
        formatted_city_country_name = f"{city_name}, {country_name}"

    return formatted_city_country_name.title()
