

# Defining assets to store extracted data.
# Asset is basically a persistent data object like a table,report, machine learning model.
#Steps:
#Since we are using dlt with dagster, we need the foloowing:
# 1. Data Source: Using dlt, we can define our data source,in this case it is REST APIs.
# 2. Data Destination: Using dlt, we can define our data destination, In this case it is PostgreSQL.
# 3. Defining a method as an asset to store this data.
# 4. We will be using @dlt.assets which is proided as a support for dlt on dagster
# 5.No need to use dlt.source since the source is a rest api.
#6. Define a pipeline to run the asset extraction.
import dlt
from dlt.sources.rest_api import rest_api_source
from dlt import pipeline
from dagster import AssetExecutionContext, Definitions,define_asset_job,AssetSelection
from dagster_dlt import DagsterDltResource, dlt_assets

# Define Assets
@dlt_assets(
    dlt_source=rest_api_source({
        "client": {
            "base_url": "http://localhost:5000/"
        },
        "resource_defaults": {
            "primary_key": "customer_id",
            "write_disposition": "replace",
            "endpoint": {
                "params": {
                    "per_page": 100,
                },
            },
        },
        "resources": [
            "getcustomerdata"
        ]
    }),
   dlt_pipeline=dlt.pipeline(pipeline_name="postgres_rest_example",dataset_name="postgres_rest_example",destination="postgres") 
)
def dagster_rest_api_assets(context: AssetExecutionContext, dlt: DagsterDltResource):
    yield from dlt.run(context=context)

###Define job here
dagster_rest_api_data_extraction=define_asset_job( name="Customer_Orders_Data_Extraction", description="Postgres REST API job extraction",selection=AssetSelection.assets(dagster_rest_api_assets)
                                                   )