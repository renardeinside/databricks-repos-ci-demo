# Databricks notebook source
# DBTITLE 1,Install nutter and it's dependencies
# MAGIC %pip install nutter

# COMMAND ----------

# DBTITLE 1,Define testing classes
from runtime.nutterfixture import NutterFixture, tag


class PrepareDataTestFixture(NutterFixture):
    def run_test_name(self):
        dbutils.notebook.run("../src/prepare-data", 600)

    def assertion_test_name(self):
        counter = spark.sql(
            "SELECT COUNT(*) AS total FROM delta.`dbfs:/databricks-repos-ci-demo/data/boston`"
        )
        first_row = counter.first()
        assert first_row[0] > 1


result = PrepareDataTestFixture().execute_tests()
print(result.to_string())

is_job = (
    dbutils.notebook.entry_point.getDbutils()
    .notebook()
    .getContext()
    .currentRunId()
    .isDefined()
)
if is_job:
    result.exit(dbutils)

