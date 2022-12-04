import nox

@nox.session
def lint(session):
    session.install("black")
    session.install("isort")
    session.run("isort", "map_merge/map_merger.py")
    session.run("isort", "map_merge/merge_strategy.py")
    session.run("black", "map_merge/map_merger.py")
    session.run("black", "map_merge/merge_strategy.py")

@nox.session
def unit_test(session):
    session.install("-r", "requirements.txt")
    session.run("coverage", "run", "-m", "pytest")
