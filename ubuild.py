import os
import subprocess
from uranium import task_requires


def main(build):
    build.packages.install(".", develop=True)


@task_requires("main")
def test(build):
    build.packages.install("pytest")
    build.packages.install("aiohttp")
    build.packages.install("radon")
    build.packages.install("coverage")
    build.executables.run([
        "coverage", "run", "--append",
        "--source=aioslack",
        "./bin/pytest", "./tests",
    ])
    build.executables.run([
        "coverage", "report", "-m"
    ])


def distribute(build):
    """ distribute the uranium package """
    build.packages.install("wheel")
    build.executables.run([
        "python", "setup.py",
        "sdist", "bdist_wheel", "--universal", "upload"
    ])
