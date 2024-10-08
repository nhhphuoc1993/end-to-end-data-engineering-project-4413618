from dagster import AssetExecutionContext, EnvVar
from dagster_dbt import DbtCliResource, dbt_assets
from dagster_airbyte import AirbyteResource, load_assets_from_airbyte_instance
from .project import dbt_transformation_project


@dbt_assets(manifest=dbt_transformation_project.manifest_path)
def dbt_transformation_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()


airbyte_instance = AirbyteResource(
    host="localhost",
    port="8000",
    # If using basic auth, include username and password:
    username="airbyte",
    password=EnvVar("AIRBYTE_PASSWORD"),
)

airbyte_assets = load_assets_from_airbyte_instance(airbyte_instance, key_prefix="raw_data")
