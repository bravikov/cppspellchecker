# Spell Checker for C++ Source Code

## Help

```
usage: cppspellchecker.py [-h] [-t] [-l LOWER_BOUND] [-u UPPER_BOUND]
                          [-d DICTIONARIES_FOLDER]
                          file [file ...]

C++ Spell Checker

positional arguments:
  file                  files for checking

optional arguments:
  -h, --help            show this help message and exit
  -t, --unique-typo-list
                        print list of unique typos
  -l LOWER_BOUND, --lower-bound LOWER_BOUND
                        print unique typo if it occurs less than "LOWER_BOUND"
                        times. Default: 1.
  -u UPPER_BOUND, --upper-bound UPPER_BOUND
                        print unique typo if it occurs less than "UPPER_BOUND"
                        times. Default: 1000000.
  -d DICTIONARIES_FOLDER, --dictionaries-folder DICTIONARIES_FOLDER
                        path to folder with dictionaries
```

## Dictionaries

The english dictionary is taken from [Big English Word Lists](https://www.keithv.com/software/wlist/).

Other English dictionaries may be useful:

*  [google-10000-english](https://github.com/first20hours/google-10000-english) repository.
