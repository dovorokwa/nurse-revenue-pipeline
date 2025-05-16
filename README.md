# Nurse Revenue Ranking Pipeline

This project uses a Confluent Kafka -> AWS -> Snowflake architecture to stream, process, and visualize nurse revenue data.

## Components

- **Kafka** (Confluent Cloud): Ingest nurse data
- **S3**: Store raw, processed, and semantic layers
- **Lambda**: Trigger ETL workflows
- **Glue**: Transform and rank nurse revenue
- **Snowflake**: Final views for dashboards
- **Power BI**: Visualize top-performing nurses

## Folder Structure

```
kafka/              - Kafka data producers
lambda/             - AWS Lambda trigger code
glue_jobs/          - PySpark ETL jobs for AWS Glue
snowflake/          - SQL views for nurse revenue ranking
dashboards/         - Power BI dashboard files
terraform/          - Infrastructure as code
```

## Deployment

1. Deploy infrastructure using Terraform
2. Run `nurse_data_producer.py` to simulate Kafka stream
3. Process data using Glue or Step Functions
4. Query views in Snowflake
5. Visualize in Power BI
