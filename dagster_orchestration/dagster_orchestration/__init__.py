from dagster import Definitions, load_asset_checks_from_modules

from .assets import resources

defs = Definitions(
    assets=load_asset_checks_from_modules([assets]),
    resources=resources
)
