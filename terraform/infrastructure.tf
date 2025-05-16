# infrastructure.tf
# Provision Kafka, S3, Lambda, and Glue using Terraform

provider "aws" {
  region = "us-west-2"
}

resource "aws_s3_bucket" "nurse_data" {
  bucket = "nurse-revenue-data-pipeline"
}

# Add more resources: lambda, glue, IAM roles, etc.
