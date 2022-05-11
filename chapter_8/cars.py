def car_info(manufacturer, model_name, **car_features):
    car_features['manufacturer'] = manufacturer
    car_features['model_name'] = model_name
    return car_features
car = car_info('subaro', 'outback', color='blue', tow_package=True)
print(car)
