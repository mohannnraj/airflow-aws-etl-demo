
# airflow-aws-etl-demo

This is a local demo environment built using Docker Compose, showcasing Apache Airflow integrated with AWS S3 and AWS RDS (PostgreSQL), along with Prometheus and Grafana for monitoring — all designed to demonstrate ETL orchestration with AWS services.

---

## Features

- Apache Airflow orchestration using LocalExecutor  
- AWS S3 integration to upload files via Airflow DAG  
- Simulated AWS RDS (PostgreSQL) interaction  
- Metrics collection with StatsD, Prometheus, and visualization in Grafana  
- Easy setup with Docker Compose  

---

## Prerequisites

- Docker & Docker Compose installed  
- AWS account with valid credentials  
- Existing AWS S3 bucket and RDS (Postgres) instance accessible from your environment  
- [Optional] AWS CLI configured locally  

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/mohannnraj/airflow-aws-etl-demo.git
cd airflow-aws-etl-demo
```

### 2. Setup environment variables

Copy the example environment file and edit it:

```bash
cp .env.example .env
```

Edit `.env` to add your actual values for:

- `AWS_ACCESS_KEY_ID`  
- `AWS_SECRET_ACCESS_KEY`  
- `AWS_DEFAULT_REGION`  
- `AIRFLOW__DATABASE__SQL_ALCHEMY_CONN` (with your RDS endpoint, username, and password)  
- `AIRFLOW__CORE__EXECUTOR` (should be `LocalExecutor`)  
- Your S3 bucket name in the DAG file (default is `airflow-demo-mohan`)  

**Important:** Do **NOT** commit your `.env` file as it contains sensitive credentials. It is included in `.gitignore`.  

### 3. Start all services with Docker Compose

```bash
docker compose up -d
```

This will start:

- Airflow webserver, scheduler, triggerer, and workers  
- Prometheus server  
- Grafana dashboard  
- StatsD exporter  

### 4. Access the UIs

- Airflow Webserver: [http://localhost:8080](http://localhost:8080)  
  (Default user: `admin` / password: `admin` unless changed in `.env`)  
- Prometheus: [http://localhost:9090](http://localhost:9090)  
- Grafana: [http://localhost:3000](http://localhost:3000)  
  (Default user/password: `admin/admin`)  

---

## Running the Demo DAG

The demo DAG `s3_to_rds_demo` does the following:

- Uploads a simple file (`test.txt`) to the configured S3 bucket  
- Simulates an RDS insert operation (prints a placeholder message)  

To run it:

1. Open the Airflow UI at `localhost:8080`  
2. Find the DAG named `s3_to_rds_demo`  
3. Toggle it **On**  
4. Trigger a manual run by clicking the “Play” button  

You should see:

- The file `test.txt` created in your S3 bucket  
- Logs showing the RDS insert simulation in the Airflow task logs  

---

## Monitoring with Prometheus & Grafana

- Airflow metrics are collected via the StatsD exporter and scraped by Prometheus  
- Grafana dashboard is pre-configured to show Airflow metrics for scheduler and webserver health  
- Visit Grafana at [http://localhost:3000](http://localhost:3000) to explore dashboards  

---

## Troubleshooting & Common Fixes

### Webserver fails to start or refuses connections

- Check Docker container logs:

```bash
docker compose logs -f webserver
```

- Make sure Docker Desktop and WSL2 have enough CPU and RAM allocated  
- Restart Docker Desktop and/or run `wsl --shutdown` from PowerShell  

### Airflow login issues

- Default admin user is `admin` / `admin` unless changed via env vars  
- If login fails, try running:

```bash
docker compose run --rm webserver airflow standalone
```

### AWS SDK (boto3) errors

- Ensure your AWS credentials in `.env` are valid and have S3 write permissions  
- Verify the bucket name matches exactly  

### Database connection errors

- Confirm your RDS endpoint is reachable  
- Check security groups allow inbound traffic from your IP or Docker network  

### Deprecated Docker Compose version warning

- Remove the `version` attribute from `docker-compose.yml` to avoid warnings  

---

## Useful Commands

- View logs:

```bash
docker compose logs -f webserver
docker compose logs -f scheduler
```

- Restart services:

```bash
docker compose restart
```

- Shutdown all services:

```bash
docker compose down
```

---

## License

MIT License
