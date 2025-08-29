### 1.Define a Definitions object 
###2. The Definitions object will hold all the assets,jobs,schedules,sensors, and resources that were defined in the assets.py file
###3. The load_assets will load assets from the assets.py file
###4. The Definitions object will be declared  with the resource object. In this case it is dlt resource.  

from dagster import Definitions, load_assets_from_modules
from dagster_dlt import DagsterDltResource
from . import assets
from .assets import dagster_rest_api_data_extraction  # noqa: TID252
dlt_resource=DagsterDltResource()
all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets ,
    jobs=[dagster_rest_api_data_extraction],
      resources={
          "dlt":dlt_resource
      }
)
