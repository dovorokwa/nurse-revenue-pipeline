⚙️ Architecture Overview
Architecture Flow:
Confluent Kafka → AWS S3 (Raw → Processed → Semantic) → AWS Lambda → AWS Glue → Snowflake → Power BI


A flowchart diagram illustrates the streaming ingestion from Kafka, AWS orchestration for ETL, Snowflake analytics, and Power BI visualization.

🧩 Components
🔁 Kafka (Confluent Cloud)
Real-time ingestion of nurse data (e.g., shift logs, revenue per patient, time tracking).

Kafka Connect pushes JSON events to AWS S3 using the S3 Sink Connector.

🪣 Amazon S3
Raw Layer: Stores raw JSON data received from Kafka.

Processed Layer: Stores transformed/cleaned datasets.

Semantic Layer: Final datasets ready for analytics.

⚡ AWS Lambda
Listens for new files in the S3 bucket.

Triggers ETL jobs using AWS Glue.

Handles small batch processing for near real-time transformation.

🔄 AWS Glue
Runs Spark-based ETL jobs to:

Parse raw nurse records.

Clean and transform the data.

Compute metrics such as total revenue per nurse, patients attended, and average revenue per shift.

Rank nurses by performance (RN, EN, AEN levels).

Writes the transformed data back to the Semantic S3 layer or directly to Snowflake.

❄️ Snowflake
Acts as the enterprise data warehouse.

Hosts curated views and tables for:

Top-performing nurses.

Monthly and quarterly revenue performance.

Comparison across departments or shifts.

📊 Power BI
Connects to Snowflake for data visualization.

Dashboards include:

Nurse leaderboards by revenue.

Filters by date, department, nurse type.

Trends over time (monthly/weekly breakdown).



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
