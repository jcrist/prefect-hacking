from prefect import task, Flow
from prefect.run_configs import ECSRun
from prefect.storage import GitHub


@task(log_stdout=True)
def greet(name):
    print(f"Hello, {name}")


with Flow("test-ecs") as flow:
    greet("world!")


flow.storage = GitHub("jcrist/prefect-hacking", path="test_ecs.py")
flow.run_config = ECSRun()
