# Linux Administration Lab - September 6, 2026

## System Information
- Ubuntu 26.04.1 LTS
- Kernel: 7.0.0-31-generic
- Memory: 14 GiB RAM
- Swap: 4 GiB
- System load was low during the lab.

## Process Monitoring
Commands practiced:
- ps aux
- ps aux --sort=-%mem
- top
- ps -ef
- kill

Learned how to identify:
- PID
- CPU usage
- memory usage
- process owner
- running command

## PostgreSQL Service Troubleshooting
PostgreSQL version: 18
Cluster: main
Port: 5432

Commands practiced:
- pg_lsclusters
- systemctl status
- ps -ef
- ss -ltnp
- pg_ctlcluster
- journalctl
- tail
- grep

Verified PostgreSQL by checking:
1. Running processes
2. Listening port 5432
3. PostgreSQL application logs
4. Database connection

## Log Troubleshooting Exercise
Attempted to connect to a database that does not exist:

fake_database

PostgreSQL returned:

FATAL: database "fake_database" does not exist

The same error appeared in the PostgreSQL log.

Troubleshooting process:
1. Reproduce the problem
2. Check service/process state
3. Check network port
4. Review logs
5. Identify the cause
6. Verify the fix
