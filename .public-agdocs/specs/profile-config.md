add functionality for a profile.yaml which supplements config.yaml:
- config.yaml loads the defaults, and should not be edited typically.
- profile.yaml (optional): if present, the settings here override the default settings in config.yaml
- the default location for profile.yaml is in repo root, but it could be present in "project data directory" in which case that should be the one loaded (instead of any other)
- add a cli setting (-c/--config) to specify a path + fn of where to load the profile.yaml from. If this is not supplied but the output dir is specied in a command, search for a profile.yaml in the output dir and then the repo root.
    - add logging if the profile is found and loaded for the user's sake.
- note: do not create a true profile in ~ or anything like that, nor do hierachal lookups for profile.yaml along the path.
- git behavior: config.yaml will be check-in to git, for profile.yaml will be gitignored