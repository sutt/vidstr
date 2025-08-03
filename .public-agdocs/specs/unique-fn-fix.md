let's refactor main.get_unique_filepath:

- change a: always start with counter "001" when generating

currently the behavior for a function calling with "myfp.ext" as the filepath arg:
if "myfp.ext" does not exist, create myfp.ext
if "myfp.ext" does exist, create myfp-001.ext
etc
desired behavior: even if "myfp.ext" does not exist, create "myfp-

- change b: strip "_XXX" suffixes from input filenames before adding the unique filepath
currently the behavior is some functions pass in /path/to/fn_1.ext to get_unique_filepath, and it return /path/to/fn_1-001.ext
desired behavior is to return /path/to/fn-001.ext
- the criteria should be to strip suffix of an underscore if it is numeric to the right of the underscore e.g.
strip: file_0.png -> file.png -> file-001.png
strip: file_9236927392.ext -> file.ext -> file-001.ext
keep: file_next.png -> file_next.png -> file_next.png