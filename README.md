# AWS Airflow Control-M style demo

Local demo using Docker Compose (Airflow + Prometheus + Grafana) with AWS S3 and AWS RDS (Postgres).

## Quick run
1. Copy example env:
cp .env.example .env

edit .env to put RDS endpoint, DB password, AWS keys, and S3 bucket name

2. Start:
docker compose up -d

3. UIs:
- Airflow: http://localhost:8080
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000 (default admin/admin)

## Notes
- Do **not** commit .env — it is in .gitignore.
- If your RDS cluster is public, make sure your IP is allowed in the DB security group.
