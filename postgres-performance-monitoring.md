---
Title: PostGresSQL Performance Monitoring
Decription: PostGresSQL Performance Monitoring
Author: Bhaskar Mangal
Date: 
Tags: PostGresSQL Performance Monitoring
---

**Table of Contents**
* TOC
{:toc}


## PostGresSQL Performance Monitoring
- https://blog.pandorafms.org/how-to-monitor-postgress/
```bash
ps aux | grep “postgres” | grep -v “grep”
vmstat 1 5
```
- https://wiki.postgresql.org/wiki/Monitoring
- https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-SHARED-BUFFERS
```sql
reindex table <table_name>
vacuum analyze <table_name>
```

## postgres-monitoring-cheatsheet
- https://russ.garrett.co.uk/2015/10/02/postgres-monitoring-cheatsheet/


### Number of connections by state
```sql
SELECT state, count(*) FROM pg_stat_activity GROUP BY state;
```

The possible states of interest are:

active: Connections currently executing queries. A large number tends to indicate DB slowness.
idle: Idle connections, not in a transaction. idle in transaction
Connections with an open transaction, not executing a query. Lots of these can indicate long-running transactions.
idle in transaction (aborted)
Connection is in a transaction, but an error has occurred and the transaction hasn’t been rolled back.

### Connections waiting for a lock
```sql
SELECT count(distinct pid) FROM pg_locks WHERE granted = false;
```

### Maximum transaction age
```sql
SELECT max(now() - xact_start) FROM pg_stat_activity  WHERE state IN ('idle in transaction', 'active');
SELECT pid, xact_start FROM pg_stat_activity ORDER BY xact_start ASC;
```
Long-running transactions are bad because they prevent Postgres from vacuuming old data. This causes database bloat and, in extreme circumstances, shutdown due to transaction ID (xid) wraparound. Transactions should be kept as short as possible, ideally less than a minute.

Alert if this number gets greater than an hour


## PG_STAT_STATEMENT Module
- http://www.dbrnd.com/2016/09/postgresql-track-all-sql-query-execution-statistics-using-pg_stat_statements-extension-performance-tuning-query-optimization-day-1/
- https://www.postgresql.org/docs/9.4/static/pgstatstatements.html

## Errors
* AH01220 error reading status kine from remote server
* sorry too many clients alread in 

## System Monitoring
* https://serverfault.com/questions/219939/too-many-time-wait-state-connections
* https://serverfault.com/questions/329845/how-to-forcibly-close-a-socket-in-time-wait
* http://www.dbatodba.com/db2/zlinux-tips/how-does-tcp-time_wait-work/
```bash
netstat -nat | awk '{print $6}' | sort | uniq -c | sort -n
```

## Checkpoint Errors
* https://www.depesz.com/2011/07/14/write-ahead-log-understanding-postgresql-conf-checkpoint_segments-checkpoint_timeout-checkpoint_warning/
* http://morozovsky.blogspot.in/2007/11/postgresql-checkpoints.html
* https://blog.2ndquadrant.com/basics-of-tuning-checkpoints/
* https://stackoverflow.com/questions/28280643/ubuntu-14-10-and-postgres-9-4-how-to-run-pg-controldata
* https://www.packtpub.com/books/content/server-configuration-tuning-postgresql
