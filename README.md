# arc

`arc` (short for "Atmosphère" and "result" combined) is an Atmosphère (and custom) result database, or rather, two simple scripts generating them.

`arc_db_gen.py` can be imported or directly executed, and it will generate two JSON databases: `arc_rc_db.json` and `arc_range_db.json`, with results and result ranges respectively.

`arc.py` is a command-line script to quickly look up a certain result, making use of the generated databases.

## Generation

The generator script parses [Atmosphère](https://github.com/Atmosphere-NX/Atmosphere)'s C++ headers (specifically, the ones [here](https://github.com/Atmosphere-NX/Atmosphere/blob/master/libraries/libvapours/include/vapours/results) where results are defined) to generate the database.

Following Atmosphère's C++ header format, for other kind of "unofficial" results not defined there, local definitions are provided [here](local_rc_src_hpps) that are also parsed the same way by the generator script.

Pull requests can be used to add local result definitions of relevant homebrew projects using custom results.

## Usage

```
$ python arc.py 0x6a8
===================================================
== arc - Atmosphère (and custom) result database ==
===================================================
===================================================
== USAGE: 'arc.py <rc>' or 'arc.py update'       ==
== Examples: 'arc.py 2002-0001', 'arc.py 0x202'  ==
== Use 'arc.py update' to update the databases!  ==
===================================================

Result matches:
 - [ams::creport] ResultAlignmentFault: (2168-0003, 0x6A8)
Range matches:
 <none>
```

```
$ python arc.py 2002-6201
===================================================
== arc - Atmosphère (and custom) result database ==
===================================================
===================================================
== USAGE: 'arc.py <rc>' or 'arc.py update'       ==
== Examples: 'arc.py 2002-0001', 'arc.py 0x202'  ==
== Use 'arc.py update' to update the databases!  ==
===================================================

Result matches:
 - [ams::fs] ResultFileExtensionWithoutOpenModeAllowAppend: (2002-6201, 0x307202)
Range matches:
 - [ams::fs] Internal: from (2002-3000, 0x177002) to (2002-7999, 0x3E7E02)
 - [ams::fs] PreconditionViolation: from (2002-6000, 0x2EE002) to (2002-6499, 0x32C602)
 - [ams::fs] InvalidOperationForOpenMode: from (2002-6200, 0x307002) to (2002-6299, 0x313602)
```

## Credits

[Atmosphère](https://github.com/Atmosphere-NX/Atmosphere) for containing simple definitions of a wide range of official results