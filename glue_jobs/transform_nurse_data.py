# transform_nurse_data.py
# Glue Job to process and rank nurse revenue data

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Load raw data
datasource = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://your-bucket/raw/nurse_data/"]},
    format="json"
)

# Transform and rank
df = datasource.toDF()
df = df.withColumn("revenue", df.net_paid + df.net_profit)
df.createOrReplaceTempView("nurse_data")

ranked_df = spark.sql("""
SELECT *, RANK() OVER (PARTITION BY department ORDER BY revenue DESC) as rank
FROM nurse_data
""")
ranked_df.show()

# Save to S3 or Snowflake
# ...
job.commit()
