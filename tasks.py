from invoke import task


@task(help={'env': 'environment'})
def compiledeps(c, env):
    """Compile  dependencies file."""
    c.run(
        f"pip-compile ./requirements/{env}.in "
        f"-o ./requirements/{env}.txt "
        "-v"
    )
