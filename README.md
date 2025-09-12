# Azure-Sales-Analytics-Platform-An-End-to-End-Data-Warehouse-Project
##Project Summary
This project demonstrates a complete, end-to-end data engineering pipeline built entirely on the Microsoft Azure cloud platform. The goal is to ingest raw, transactional sales data from multiple sources, process it through a multi-layered data lake, model it into an analytics-ready Star Schema, and serve it for business intelligence and reporting.

Architecture
The pipeline follows the modern ELT (Extract, Load, Transform) paradigm using a Medallion Architecture to ensure data quality and governance, moving data from a raw Bronze layer to a clean Silver layer, and finally to an aggregated Gold layer ready for analytics.

<img width="1687" height="662" alt="Project Structure" src="https://github.com/user-attachments/assets/f306111b-3ea4-4b8d-9117-0956df85bf55" />

Technologies Used
<img width="693" height="203" alt="image" src="https://github.com/user-attachments/assets/de4a654b-4590-4060-b404-28a2269530bb" />

How It Works

1. Data Ingestion (Incremental Loading)
   
An Azure Data Factory pipeline orchestrates the entire process. It uses a watermark technique to incrementally load only new or updated data from the source, making the process efficient and scalable. The pipeline includes lookups to determine the data range, a copy activity to move the data, and a stored procedure to update the watermark upon successful completion.
<img width="1495" height="779" alt="connection to make parquet" src="https://github.com/user-attachments/assets/6021e988-625f-4888-bc9f-2d35c56e03e0" />

<img width="1885" height="856" alt="Incremental pipeline" src="https://github.com/user-attachments/assets/e659b5a1-4ffb-4872-bb45-1a0e9d4acc67" />

2. Data Transformation (Bronze to Gold)
Once the raw data is landed in the Bronze layer of the Data Lake, Azure Databricks takes over the transformation using PySpark notebooks.

Silver Layer:
The raw data is cleaned, validated, and enriched. It's queried here directly from the Parquet files stored in the data lake.
<img width="1818" height="466" alt="image" src="https://github.com/user-attachments/assets/982fef07-f1e9-439c-bab5-c4399c8bd02e" />
<img width="1526" height="705" alt="Databricks querying on silver data" src="https://github.com/user-attachments/assets/171b8d11-1ec9-4627-9e4e-adf2170487a3" />

Gold Layer:
The Silver layer data is then modeled into a Star Schema, consisting of four dimension tables and one central fact table. This is orchestrated using a Databricks Job that runs the notebooks in the correct order of dependency.

<img width="1447" height="763" alt="Azure pipeline" src="https://github.com/user-attachments/assets/879b8a6e-c303-4753-8206-f9ddffa5071c" />
<img width="361" height="277" alt="image" src="https://github.com/user-attachments/assets/e70dd453-3635-4677-ad31-d630229dc404" />


The final fact_sales table contains surrogate keys and numeric measures, optimized for fast BI queries.

<img width="1356" height="697" alt="fact table" src="https://github.com/user-attachments/assets/5f2d9ee6-e874-43b8-b4a3-4c0ef172218c" />

3. Data Serving & Visualization
The final, aggregated Gold layer data is then ready for analysis. Using Databricks SQL, we can perform analytics and create visualizations, such as analyzing the total units sold per year.

<img width="1876" height="775" alt="databricks sales visualization" src="https://github.com/user-attachments/assets/08dcb7e6-b548-4430-9b7c-4d6d8d50f922" />

Key Learnings & Concepts Implemented
Incremental Data Loading: Designing efficient pipelines that only process new data.

Medallion Architecture: Structuring the data lake into Bronze (raw), Silver (clean), and Gold (aggregated) layers.

Dimensional Modeling: Building a Star Schema with Fact and Dimension tables to optimize for analytics.

Slowly Changing Dimensions (SCD Type 1): Using MERGE operations in Databricks to handle updates to dimension data.

Infrastructure as Code (IaC) Principles: The entire environment can be defined and deployed through templates.

Cloud Data Governance: Using Unity Catalog to manage tables and security.

## Repository Contents
Notebooks: This repository contains the complete PySpark source code (.py files) for all the Azure Databricks notebooks used to perform the data transformations.

Screenshots: The README.md file is illustrated with screenshots that showcase the pipeline architecture, successful job runs, and final data models to provide a visual walkthrough of the project from end to end.














