import csv

input_file = "data/fleet_raw.csv"
output_file = "data/fleet_analytics.csv"

with open(input_file, newline="") as f:
    rows = list(csv.DictReader(f))

clean_rows = []

for row in rows:
    year = int(row["year"])
    mileage = int(row["mileage"])
    maintenance_cost = float(row["maintenance_cost"])
    fuel_cost = float(row["fuel_cost"])

    vehicle_age = 2026 - year
    total_operating_cost = maintenance_cost + fuel_cost

    if mileage > 0:
        cost_per_mile = total_operating_cost / mileage
    else:
        cost_per_mile = 0

    clean_rows.append({
        "vehicle_number": row["vehicle_number"].strip(),
        "year": year,
        "vehicle_age": vehicle_age,
        "make": row["make"].strip(),
        "model": row["model"].strip(),
        "vehicle_type": row["vehicle_type"].strip(),
        "mileage": mileage,
        "status": row["status"].strip(),
        "maintenance_cost": round(maintenance_cost, 2),
        "repair_count": int(row["repair_count"]),
        "downtime_days": int(row["downtime_days"]),
        "fuel_gallons": round(float(row["fuel_gallons"]), 2),
        "fuel_cost": round(fuel_cost, 2),
        "total_operating_cost": round(total_operating_cost, 2),
        "cost_per_mile": round(cost_per_mile, 4),
    })

clean_rows.sort(key=lambda row: row["vehicle_number"])

headers = [
    "vehicle_number",
    "year",
    "vehicle_age",
    "make",
    "model",
    "vehicle_type",
    "mileage",
    "status",
    "maintenance_cost",
    "repair_count",
    "downtime_days",
    "fuel_gallons",
    "fuel_cost",
    "total_operating_cost",
    "cost_per_mile",
]

with open(output_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(clean_rows)

print(f"Created {output_file} with {len(clean_rows)} vehicles.")
