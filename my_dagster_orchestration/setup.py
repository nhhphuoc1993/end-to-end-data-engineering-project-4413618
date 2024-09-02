from setuptools import find_packages, setup

setup(
    name="my_dagster_orchestration",
    version="0.0.1",
    packages=find_packages(),
    package_data={
        "my_dagster_orchestration": [
            "dbt-project/**/*",
        ],
    },
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dbt-bigquery<1.9",
    ],
    extras_require={
        "dev": [
            "dagster-webserver",
        ]
    },
)