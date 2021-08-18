# Databricks notebook source
# DBTITLE 1,Imports
import pyspark.sql.functions as F
import pyspark.sql.types as T
from pyspark.sql import DataFrame
from sklearn.datasets import load_boston
import pandas as pd

# COMMAND ----------

# DBTITLE 1,Functions
def get_data() -> DataFrame:
    bd = load_boston()
    _df = pd.DataFrame(bd.data, columns=bd.feature_names)
    _df["TARGET"] = bd.target
    df = spark.createDataFrame(_df)
    return df


# COMMAND ----------

# DBTITLE 1,Main
df = get_data()
df.write.format("delta").mode("overwrite").save("dbfs:/gcp-ci-sample/data/boston")
