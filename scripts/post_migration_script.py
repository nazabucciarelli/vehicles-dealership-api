# scripts/post_migration_script.py

from django.db import connection

def run():
    sql_commands = [
        "DELETE FROM vehicles_vehicle;",
        "DELETE FROM vehicles_model;",
        "DELETE FROM vehicles_category;",
        "DELETE FROM vehicles_brand;",
        "DELETE FROM vehicles_transmission;",
        "DELETE FROM vehicles_tractioncontrol;",
        "DELETE FROM vehicles_vehiclebodytype;",
        "DELETE FROM vehicles_steering;",
        "DELETE FROM vehicles_enginetype;",
        "DELETE FROM vehicles_vehiclecondition;",
        "DELETE FROM users_country;",
        "DELETE FROM users_province;",
        "DELETE FROM users_city;",
        "DELETE FROM users_gender;",
        "DELETE FROM sqlite_sequence WHERE name='vehicles_vehicle';",
        "DELETE FROM sqlite_sequence WHERE name='vehicles_model';",
        "DELETE FROM sqlite_sequence WHERE name='vehicles_category';",
        "DELETE FROM sqlite_sequence WHERE name='vehicles_brand';",
        "DELETE FROM sqlite_sequence WHERE name='vehicles_transmission';",
        "DELETE FROM sqlite_sequence WHERE name='vehicles_tractioncontrol';",
        "DELETE FROM sqlite_sequence WHERE name='vehicles_vehiclebodytype';",
        "DELETE FROM sqlite_sequence WHERE name='vehicles_steering';",
        "DELETE FROM sqlite_sequence WHERE name='vehicles_enginetype';",
        "DELETE FROM sqlite_sequence WHERE name='vehicles_vehiclecondition';",
        "DELETE FROM sqlite_sequence WHERE name='users_country';",
        "DELETE FROM sqlite_sequence WHERE name='users_province';",
        "DELETE FROM sqlite_sequence WHERE name='users_city';",
        "DELETE FROM sqlite_sequence WHERE name='users_gender';",
        "INSERT INTO users_country (name) VALUES ('Argentina');",
        "INSERT INTO users_province (name,country_id) VALUES ('Cordoba',1);",
        "INSERT INTO users_city (name,province_id) VALUES ('Rio Cuarto',1);",
        "INSERT INTO users_gender (name) VALUES ('Male');",
        "INSERT INTO users_gender (name) VALUES ('Female');",
        "INSERT INTO vehicles_category (name) VALUES ('Trucks'), ('Motorbikes'), ('Cars');",
        "INSERT INTO vehicles_brand (name) VALUES ('Toyota'), ('Ford'), ('Honda'), ('Harley-Davidson'), ('BMW');",
        "INSERT INTO vehicles_transmission (name) VALUES ('Automatic'), ('Manual'), ('Semi-Automatic');",
        "INSERT INTO vehicles_tractioncontrol (name) VALUES ('AWD'), ('FWD'), ('RWD'), ('4WD');",
        "INSERT INTO vehicles_vehiclebodytype (name) VALUES ('Coupe'), ('Convertible'), ('Hatchback'), ('Sedan'), ('SUV'), ('Truck'), ('Motorbike');",
        "INSERT INTO vehicles_steering (name) VALUES ('Power Steering'), ('Manual Steering'), ('Electric Steering');",
        "INSERT INTO vehicles_enginetype (name) VALUES ('Petrol'), ('Diesel'), ('Electric'), ('Hybrid');",
        "INSERT INTO vehicles_vehiclecondition (name) VALUES ('New'), ('Used');",
        "INSERT INTO vehicles_model (name, brand_id, transmission_id, traction_control_id, vehicle_body_type_id, steering_id, engine_type_id, category_id) VALUES ('F-150', 2, 2, 4, 6, 1, 2, 1);",
        "INSERT INTO vehicles_model (name, brand_id, transmission_id, traction_control_id, vehicle_body_type_id, steering_id, engine_type_id, category_id) VALUES ('Civic', 3, 1, 3, 4, 2, 1, 3);",
        "INSERT INTO vehicles_model (name, brand_id, transmission_id, traction_control_id, vehicle_body_type_id, steering_id, engine_type_id, category_id) VALUES ('Mustang', 2, 2, 2, 1, 1, 1, 3);",
        "INSERT INTO vehicles_model (name, brand_id, transmission_id, traction_control_id, vehicle_body_type_id, steering_id, engine_type_id, category_id) VALUES ('Road King', 4, 2, 2, 7, 2, 1, 2);",
        "INSERT INTO vehicles_model (name, brand_id, transmission_id, traction_control_id, vehicle_body_type_id, steering_id, engine_type_id, category_id) VALUES ('i8', 5, 1, 1, 1, 3, 3, 3);",
        "INSERT INTO vehicles_model (name, brand_id, transmission_id, traction_control_id, vehicle_body_type_id, steering_id, engine_type_id, category_id) VALUES ('Hilux', 1, 1, 4, 6, 1, 2, 1);",
        "INSERT INTO vehicles_model (name, brand_id, transmission_id, traction_control_id, vehicle_body_type_id, steering_id, engine_type_id, category_id) VALUES ('Gold Wing', 3, 1, 1, 7, 2, 1, 2);",
        "INSERT INTO vehicles_model (name, brand_id, transmission_id, traction_control_id, vehicle_body_type_id, steering_id, engine_type_id, category_id) VALUES ('X5', 5, 3, 1, 5, 3, 4, 3);",
        "INSERT INTO vehicles_model (name, brand_id, transmission_id, traction_control_id, vehicle_body_type_id, steering_id, engine_type_id, category_id) VALUES ('Ranger', 2, 2, 4, 6, 1, 2, 1);",
    ]

    with connection.cursor() as cursor:
        for command in sql_commands:
            cursor.execute(command)

    print("Script post-migración ejecutado exitosamente.")
