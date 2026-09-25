-- Fleet Management Report
-- Combines maintenance costs, service counts,
-- and vehicle downtime into one report.
--
-- Summarize each table separately to prevent
-- row multiplication when joining tables.

CREATE OR REPLACE VIEW fleet_management_report AS

WITH maintenance_summary AS (
    SELECT
        vehicle_id,
        COUNT(*) AS maintenance_records,
        SUM(cost) AS maintenance_cost
    FROM maintenance
    GROUP BY vehicle_id
),

downtime_summary AS (
    SELECT
        vehicle_id,
        SUM(end_date - start_date) AS downtime_days
    FROM downtime_logs
    GROUP BY vehicle_id
)

SELECT
    v.vehicle_number,
    v.make,
    v.model,
    COALESCE(ms.maintenance_records, 0)
        AS maintenance_records,
    COALESCE(ms.maintenance_cost, 0)
        AS maintenance_cost,
    COALESCE(ds.downtime_days, 0)
        AS downtime_days

FROM vehicles AS v

LEFT JOIN maintenance_summary AS ms
    ON v.id = ms.vehicle_id

LEFT JOIN downtime_summary AS ds
    ON v.id = ds.vehicle_id;
