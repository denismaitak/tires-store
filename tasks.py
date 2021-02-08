from invoke import task


@task(help={'env': 'environment'})
def compiledeps(c, env):
    """Compile  dependencies file."""
    c.run(
        f'pip-compile ./requirements/{env}.in '
        f'-o ./requirements/{env}.txt '
        '-v'
    )


@task
def setupgithooks(c):
    """Set up predefined hooks to the project's GIT repo."""
    c.run('cp git-hooks/* .git/hooks/')
