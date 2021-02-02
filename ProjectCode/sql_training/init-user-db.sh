#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER user_problems  WITH PASSWORD '123456';
    GRANT CONNECT ON DATABASE postgres TO user_problems;
    GRANT SELECT ON ALL TABLES IN SCHEMA public TO user_problems;
EOSQL
