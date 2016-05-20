from invoke import task, run


@task
def db_revision(msg=None):
    if not msg:
        msg = 'Auto'
    run('solo db revision --autogenerate -m "{msg}" --solocfg _priv/config.yml'.format(msg=msg))


@task
def db_migrate():
    run("solo db upgrade heads --solocfg _priv/config.yml")
