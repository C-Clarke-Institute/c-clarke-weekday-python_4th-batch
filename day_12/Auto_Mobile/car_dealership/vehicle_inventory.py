

vehicles = [
    {
        "veh_id": 1,
        "name": "Toyota Corolla",
        "manufacture": "Toyota",
        "manufacture_year": 2023,
        "model": "Corolla",
        "country_of_origin": "Japan",
        "price": 12500000.0
    },
    {
        "veh_id": 2,
        "name": "Honda Civic",
        "manufacture": "Honda",
        "manufacture_year": 2022,
        "model": "Civic",
        "country_of_origin": "Japan",
        "price": 14500000.0
    },
    {
        "veh_id": 3,
        "name": "Suzuki Swift",
        "manufacture": "Suzuki",
        "manufacture_year": 2024,
        "model": "Swift",
        "country_of_origin": "Japan",
        "price": 8500000.0
    },
    {
        "veh_id": 4,
        "name": "Toyota Prius",
        "manufacture": "Toyota",
        "manufacture_year": 2021,
        "model": "Prius",
        "country_of_origin": "Japan",
        "price": 11500000.0
    },
    {
        "veh_id": 5,
        "name": "Hyundai Tucson",
        "manufacture": "Hyundai",
        "manufacture_year": 2023,
        "model": "Tucson",
        "country_of_origin": "South Korea",
        "price": 18500000.0
    },
    {
        "veh_id": 6,
        "name": "Kia Sportage",
        "manufacture": "Kia",
        "manufacture_year": 2022,
        "model": "Sportage",
        "country_of_origin": "South Korea",
        "price": 17500000.0
    },
    {
        "veh_id": 7,
        "name": "BMW 320i",
        "manufacture": "BMW",
        "manufacture_year": 2023,
        "model": "320i",
        "country_of_origin": "Germany",
        "price": 32000000.0
    },
    {
        "veh_id": 8,
        "name": "Mercedes-Benz C-Class",
        "manufacture": "Mercedes-Benz",
        "manufacture_year": 2022,
        "model": "C-Class",
        "country_of_origin": "Germany",
        "price": 35000000.0
    },
    {
        "veh_id": 9,
        "name": "Nissan Leaf",
        "manufacture": "Nissan",
        "manufacture_year": 2024,
        "model": "Leaf",
        "country_of_origin": "Japan",
        "price": 10500000.0
    },
    {
        "veh_id": 10,
        "name": "Tesla Model 3",
        "manufacture": "Tesla",
        "manufacture_year": 2023,
        "model": "Model 3",
        "country_of_origin": "United States",
        "price": 28000000.0
    },
    {
        "veh_id": 11,
        "name": "Ford Ranger",
        "manufacture": "Ford",
        "manufacture_year": 2021,
        "model": "Ranger",
        "country_of_origin": "United States",
        "price": 22000000.0
    }
]

def add_vehicle(vehicle) :
    if 'veh_id' not in vehicle:
        print("Print Vehicle ID is required.")
        return

    if get_vehicle_by_id(vehicle['veh_id']) is not None:
        print("Vehicle ID already exists.")
        return

    vehicles.append(vehicle)
    print("Vehicle added successfully.")

def get_vehicle_by_id(vehicle_id):

    for vehicle in vehicles:
        if vehicle['veh_id'] == vehicle_id:
            return vehicle

    return None