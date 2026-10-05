import csv
import random

random.seed(42)

vehicles = [
    ("Ford", "Transit", "Van"),
    ("Chevrolet", "Express", "Van"),
    ("Ram", "ProMaster", "Van"),
    ("Ford", "F-150", "Pickup"),
    ("Ford", "F-250", "Pickup"),
    ("Ford", "F-550", "Truck"),
    ("Chevrolet", "Silverado 1500", "Pickup"),
    ("Chevrolet", "Silverado 2500", "Pickup"),
    ("GMC", "Sierra 1500", "Pickup"),
    ("GMC", "Sierra 2500", "Pickup"),
]

statuses = ["Active", "Active", "Active", "Active", "Maintenance", "Out of Service"]

rows = []

for i in range(1, 76):
    make, model, vehicle_type = random.choice(vehicles)

    year = random.randint(2016, 2026)
    age = 2026 - year

    mileage = random.randint(18000, 45000) + (age * random.randint(7000, 12000))

    repair_count = max(
        0,
        int((mileage / 30000) + random.randint(-1, 2))
    )

    maintenance_cost = round(
        repair_count * random.uniform(225, 900),
        2
    )

    downtime_days = max(
        0,
        repair_count + random.randint(-1, 3)
    )

    fuel_gallons = round(
        random.uniform(550, 1800),
        2
    )

    avg_price = random.uniform(3.10, 3.90)
    fuel_cost = round(fuel_gallons * avg_price, 2)

    status = random.choice(statuses)

    rows.append([
        f"UNIT-{i:03d}",
        year,
        make,
        model,
        vehicle_type,
        mileage,
        status,
        maintenance_cost,
        repair_count,
        downtime_days,
        fuel_gallons,
        fuel_cost
    ])

headers = [
    "vehicle_number",
    "year",
    "make",
    "model",
    "vehicle_type",
    "mileage",
    "status",
    "maintenance_cost",
    "repair_count",
    "downtime_days",
    "fuel_gallons",
    "fuel_cost"
]

with open("data/fleet_raw.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(rows)

print("Created data/fleet_raw.csv with 75 vehicles.")
