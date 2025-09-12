# Databricks notebook source
# MAGIC %md
# MAGIC # DATA READING

# COMMAND ----------

df=spark.read.format('parquet')\
    .option('inferschema',True)\
        .load('abfss://bronze@cargauthadatalake.dfs.core.windows.net/rawdata')

# COMMAND ----------

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC # DATA TRANSFORMATION

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

df=df.withColumn("Model_category",split(col("Model_ID"),"-")[0])
df.display()

# COMMAND ----------

df.withColumn('Units_Sold',col('Units_Sold').cast(StringType())).printSchema()

# COMMAND ----------

df=df.withColumn('RevPerUnit',col('Revenue')/col('Units_Sold'))
df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC # AD-HOC
# MAGIC

# COMMAND ----------

df.display()

# COMMAND ----------

display(df.groupBy('Year','BranchName').agg(sum('Units_Sold').alias('Total_Units')).sort('Year','Total_Units',ascending=[1,0]))

# COMMAND ----------

# MAGIC %md 
# MAGIC # DATA-WRITING

# COMMAND ----------

df.write.format('parquet')\
    .mode('overwrite')\
        .option('path','abfss://silver@cargauthadatalake.dfs.core.windows.net/carsales')\
            .save()

# COMMAND ----------

# MAGIC %md
# MAGIC # Querying Silver Data

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from parquet.`abfss://silver@cargauthadatalake.dfs.core.windows.net/carsales`

# COMMAND ----------

