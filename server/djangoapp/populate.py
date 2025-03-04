from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"name":"NISSAN", "description":"Great cars. Japanese technology"},
        {"name":"Mercedes", "description":"Great cars. German technology"},
        {"name":"Audi", "description":"Great cars. German technology"},
        {"name":"Kia", "description":"Great cars. Korean technology"},
        {"name":"Toyota", "description":"Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
            car_make_instances.append(CarMake.objects.create(name=data['name'], description=data['description']))


    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
      {"name":"Pathfinder", "dealer_id": 0, "type":"SUV", "year": 2023, "car_make":car_make_instances[0]},
      {"name":"Qashqai", "dealer_id": 1, "type":"SUV", "year": 2023, "car_make":car_make_instances[0]},
      {"name":"XTRAIL", "dealer_id": 2, "type":"SUV", "year": 2023, "car_make":car_make_instances[0]},
      {"name":"YTRAIL", "dealer_id": 3, "type":"MINIVAN", "year": 2024, "car_make":car_make_instances[0]},
      {"name":"A-Class", "dealer_id": 4, "type":"SUV", "year": 2023, "car_make":car_make_instances[1]},
      {"name":"C-Class", "dealer_id": 0, "dealer_id": 0, "type":"JEEP", "year": 2023, "car_make":car_make_instances[1]},
      {"name":"E-Class", "dealer_id": 1, "type":"WAGON", "year": 2023, "car_make":car_make_instances[1]},
      {"name":"F-Class", "dealer_id": 2, "type":"MINIVAN", "year": 2025, "car_make":car_make_instances[1]},
      {"name":"A4", "dealer_id": 3, "type":"SUV", "year": 2023, "car_make":car_make_instances[2]},
      {"name":"A5", "dealer_id": 4, "type":"SUV", "year": 2023, "car_make":car_make_instances[2]},
      {"name":"A6", "dealer_id": 0, "type":"SUV", "year": 2023, "car_make":car_make_instances[2]},
      {"name":"A7", "dealer_id": 1, "type":"COUPE", "year": 2020, "car_make":car_make_instances[2]},
      {"name":"Sorrento", "dealer_id": 2, "type":"JEEP", "year": 2023, "car_make":car_make_instances[3]},
      {"name":"Carnival", "dealer_id": 3, "type":"WAGON", "year": 2023, "car_make":car_make_instances[3]},
      {"name":"Cerato", "dealer_id": 4, "type":"Sedan", "year": 2023, "car_make":car_make_instances[3]},
      {"name":"Kilgon", "dealer_id": 0, "type":"COUPE", "year": 2019, "car_make":car_make_instances[3]},
      {"name":"Corolla", "dealer_id": 1, "type":"Sedan", "year": 2023, "car_make":car_make_instances[4]},
      {"name":"Camry", "dealer_id": 2, "type":"Sedan", "year": 2023, "car_make":car_make_instances[4]},
      {"name":"Kluger", "dealer_id": 3, "type":"WAGON", "year": 2023, "car_make":car_make_instances[4]},
        # Add more CarModel instances as needed
    ]

    for data in car_model_data:
            CarModel.objects.create(name=data['name'], dealer_id=data['dealer_id'], car_make=data['car_make'], type=data['type'], year=data['year'])