import os

from prefect import Flow, task, Parameter
from prefect.storage import GitHub
from prefect.run_configs import LocalRun


@task(log_stdout=True)
def greet(name):
    greeting = os.environ.get("GREETING", "Hello")
    print(f"{greeting}, {name}!")


with Flow("test-github") as flow:
    name = Parameter("name")
    greet(name)


flow.storage = GitHub("jcrist/prefect-hacking", path="test_github.py")
flow.run_config = LocalRun(env={"GREETING": "Hello"})
