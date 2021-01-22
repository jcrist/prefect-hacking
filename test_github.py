from prefect import Flow, task
from prefect.storage import GitHub


@task(log_stdout=True)
def echo(x):
    print(x)


with Flow("test-s3") as flow:
    echo("hello")


flow.storage = GitHub("jcrist/prefect-hacking", path="test_github.py")
