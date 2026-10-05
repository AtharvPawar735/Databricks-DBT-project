# Databricks-DBT-project
# End-to-End Big Data Pipeline: Databricks, dbt, & Delta Live Tables

## Overview
This project implements a scalable, end-to-end Data Engineering pipeline using the **Medallion Architecture** (Bronze, Silver, Gold). Built on Databricks, the pipeline automates the ingestion, transformation, and dimensional modeling of raw data into high-performance Delta tables optimized for enterprise analytics and Business Intelligence. 

## Tech Stack
* **Data Processing & Streaming:** PySpark, Apache Spark
* **Data Platform & Governance:** Databricks, Unity Catalog
* **Ingestion & Pipelines:** Databricks Autoloader, Delta Live Tables (DLT)
* **Transformation & Modeling:** dbt (data build tool), SQL
* **Storage:** Delta Lake
* **Orchestration:** Databricks Workflows / Jobs

## Architecture Breakdown

### 1. Bronze Layer (Raw Data Ingestion)
* Ingested 7 distinct raw CSV datasets.
* Utilized **Databricks Autoloader** with PySpark Streaming for efficient, incremental data ingestion.
* Saved raw data directly into **Delta Tables** to ensure ACID compliance and schema enforcement from the point of entry.

### 2. Silver Layer (Cleansing & Incremental Transformation)
* Leveraged **Delta Live Tables (DLT)** to build declarative, fault-tolerant pipelines.
* Cleaned, filtered, and deduplicated the raw Bronze data.
* Implemented incremental transformations to process only new or updated records, significantly reducing compute costs and processing time.

### 3. Gold Layer (Dimensional Modeling & Analytics)
* Stored the Delta tables in the gold layer after transformation in the silver layer.
* Implemented Automated **Slowly Changing Dimensions (SCD)** to track historical data changes over time.
* Used **dbt (data build tool)** and SQL to execute complex business logic and aggregate data for downstream reporting tools (e.g., Power BI).

## Key Features
* **Unity Catalog Integration:** Centralized data governance, access control, and auditing across the entire pipeline.
* **Automated Orchestration:** Deployed Databricks Jobs to schedule and manage the execution of DLT pipelines and dbt models.
* **Version Control:** Managed dbt transformations and PySpark notebooks via Git integration.
