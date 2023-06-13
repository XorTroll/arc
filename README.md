# arc

`arc` (short for "Atmosphère" and "result" combined) is a Python Atmosphère/custom Nintendo Switch result utility.

## Databases

`arc_db_gen.py` parses both [Atmosphère](https://github.com/Atmosphere-NX/Atmosphere)'s C++ headers and custom (default or user-provided) result headers to generate two JSON databases: `arc_rc_db.json` and `arc_range_db.json` (of results and result ranges respectively).

Some useful/template result headers are provided [here](default_rc_hpps). Note that they are not valid C++ headers by themselves, since they just follow a simple format (similar to Atmosphère's result headers but without any includes or extra stuff).

Pull requests can be used to add default result definitions of relevant homebrew projects using custom results.

## C++ headers

`arc_cpp_gen.py` generates a standalone C++ header containing result definitions and utilities from the generated database results and result ranges.

## Usage

### Generating the databases

`python arc.py gen_db default`

`python arc.py gen_db ams+goldleaf+emuiibo`

`python arc.py gen_db default+../dummy/rc_defs.hpp`

> 'ams' is a special token for Atmosphère results, while 'default' is a special token all Atmosphère and default results

> User-provided (non-default) result headers can be supplied with or without their extension in case it's `.rc.hpp` or even as an absolute/relative path (always keep in mind that `+` is a reserved symbol here)

### Result lookup (databases must already be generated)

`python arc.py rc 0x202`

`python arc.py rc 2168-0002`

> This will print all the result or result range matches found in the databases

### C++ generation (databases must already be generated)

`python arc.py gen_cpp testmod TESTMACRO test.hpp`

> This will generate everything inside `testmod::` namespace, and all macro names will be prefixed as `TESTMACRO_<...>`

## Credits

[Atmosphère](https://github.com/Atmosphere-NX/Atmosphere) for containing simple definitions of a wide range of official results (and basically the best official result+name collection out there)
