-- Fleet Management SQL Queries
-- September 12, 2026

-- 1. Vehicles sorted by highest mileage
SELECT
    vehicle_number,
    year,
    make,
    model,
    mileage
FROM vehicles
ORDER BY mileage DESC;

-- 2. Vehicles currently in maintenance
SELECT
    vehicle_number,
    year,
    make,
    model,
    status
FROM vehicles
WHERE status = 'Maintenance';

-- 3. Total maintenance cost for each vehicle
SELECT
    v.vehicle_number,
    COALESCE(SUM(m.cost), 0) AS total_maintenance_cost
FROM vehicles AS v
LEFT JOIN maintenance AS m
    ON v.id = m.vehicle_id
GROUP BY v.id, v.vehicle_number
ORDER BY total_maintenance_cost DESC;

-- 4. Most recent maintenance date for each vehicle
SELECT
    v.vehicle_number,
    MAX(m.service_date) AS last_service_date
FROM vehicles AS v
LEFT JOIN maintenance AS m
    ON v.id = m.vehicle_id
GROUP BY v.id, v.vehicle_number
ORDER BY last_service_date DESC NULLS LAST;

-- 5. Maintenance jobs costing more than $100
SELECT
    v.vehicle_number,
    m.service_date,
    m.service_type,
    m.cost
FROM vehicles AS v
INNER JOIN maintenance AS m
    ON v.id = m.vehicle_id
WHERE m.cost > 100
ORDER BY m.cost DESC;

-- 6. Number of maintenance records per vehicle
SELECT
    v.vehicle_number,
    COUNT(m.id) AS maintenance_records
FROM vehicles AS v
LEFT JOIN maintenance AS m
    ON v.id = m.vehicle_id
GROUP BY v.id, v.vehicle_number
ORDER BY maintenance_records DESC;

-- 7. Vehicles with no maintenance history
SELECT
    v.vehicle_number,
    v.year,
    v.make,
    v.model
FROM vehicles AS v
LEFT JOIN maintenance AS m
    ON v.id = m.vehicle_id
WHERE m.id IS NULL;

-- 8. Average maintenance cost
SELECT
    ROUND(AVG(cost), 2) AS average_maintenance_cost
FROM maintenance;

-- 9. Total maintenance spending
SELECT
    SUM(cost) AS total_maintenance_spending
FROM maintenance;

-- 10. Vehicle with the highest total maintenance cost
SELECT
    v.vehicle_number,
    v.make,
    v.model,
    SUM(m.cost) AS total_maintenance_cost
FROM vehicles AS v
INNER JOIN maintenance AS m
    ON v.id = m.vehicle_id
GROUP BY v.id, v.vehicle_number, v.make, v.model
ORDER BY total_maintenance_cost DESC
LIMIT 1;
