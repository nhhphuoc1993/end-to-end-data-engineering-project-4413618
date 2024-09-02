from dagster import (
    Definitions,
    AssetSelection,
    ScheduleDefinition,
    define_asset_job
)
from dagster_dbt import DbtCliResource
from .assets import dbt_transformation_dbt_assets, airbyte_assets
from .project import dbt_transformation_project
from .schedules import schedules

big_star_job = define_asset_job('big_star_job', selection=AssetSelection.all())

big_star_schedule = ScheduleDefinition(
    job=big_star_job,
    cron_schedule='0 * * * *',
)

defs = Definitions(
    assets=[dbt_transformation_dbt_assets, airbyte_assets],
    schedules=[big_star_schedule],
    # schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=dbt_transformation_project),
    },
)
