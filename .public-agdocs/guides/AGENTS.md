# Guidance for coding agents:
- if any documentation urls are provided, make sure to scrape those to obtain information on the package.
- run package installation commands if changing any packages.
- run bash scripts to verify your work.
- get documentation on 3rd party packages by running something like: uv run python -c "import foo; print(help(foo.bar))"
- you continue to run commands and search the web until you have succeeded at your task.
- do not follow conventions or rely on facts in .public-agdocs/specs/, this is simply scratch work on defining specification for previous iterations of the software and may be deprecated or unimplemented.

# Best practices for coding agents:
- Use uv for running the app and package management.
- use `uv run pytest` to run pytest.
- when adding new packages to pyproject.toml, make sure to update the environment with `uv sync --all-extras`
- add any nec packages to main dependencies and/or to the testing group dependencies if you write tests that need those.