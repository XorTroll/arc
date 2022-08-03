import json
import os
import sys
import arc_db_gen

arc_rc_db_path = "arc_rc_db.json"
arc_range_db_path = "arc_range_db.json"

def ensure_dbs():
    if (not os.path.isfile(arc_rc_db_path)) or (not os.path.isfile(arc_range_db_path)):
        print()
        print("Result/range databases are not present, automatically generating them...")
        arc_db_gen.generate_dbs()
        print("Result/range databases were successfully generated!")
        print()

def format_rc(rc_module, rc_desc):
    rc = ((rc_module & 0x1FF) | (rc_desc & 0x1FFF) << 9)
    rc_fmt = f"{2000 + rc_module:04}-{rc_desc:04}"
    rc_hex = f"0x{rc:X}"
    return f"({rc_fmt}, {rc_hex})"

def lookup_rc(rc_module, rc_desc):
    ensure_dbs()

    with open("arc_rc_db.json", "r") as f:
        all_rcs = json.load(f)
    
    with open("arc_range_db.json", "r") as f:
        all_ranges = json.load(f)

    print("Result matches:")
    any_rc = False
    for a_rc in all_rcs:
        a_rc_module = int(a_rc["module"])
        a_rc_desc = int(a_rc["desc"])
        if (a_rc_module == rc_module) and (a_rc_desc == rc_desc):
            any_rc = True
            a_rc_mod_name = a_rc["module_name"]
            a_rc_name = "Result" + a_rc["name"]
            print (f" - [{a_rc_mod_name}] {a_rc_name}: {format_rc(a_rc_module, a_rc_desc)}")
    if not any_rc:
        print(" <none>")

    print("Range matches:")
    any_rg = False
    for a_rg in all_ranges:
        a_rg_module = int(a_rg["module"])
        a_rg_start_desc = int(a_rg["start_desc"])
        a_rg_end_desc = int(a_rg["end_desc"])
        if (a_rg_module == rc_module) and (a_rg_start_desc <= rc_desc) and (a_rg_end_desc >= rc_desc):
            any_rg = True
            a_rg_mod_name = a_rg["module_name"]
            a_rg_name = a_rg["name"]
            print(f" - [{a_rg_mod_name}] {a_rg_name}: from {format_rc(a_rg_module, a_rg_start_desc)} to {format_rc(a_rg_module, a_rg_end_desc)}")
    if not any_rg:
        print(" <none>")

if __name__ == "__main__":
    print("===================================================")
    print("== arc - Atmosphère (and custom) result database ==")
    print("===================================================")
    print("===================================================")
    print("== USAGE: 'arc.py <rc>' or 'arc.py update'       ==")
    print("== Examples: 'arc.py 2002-0001', 'arc.py 0x202'  ==")
    print("== Use 'arc.py update' to update the databases!  ==")
    print("===================================================")
    print()

    if len(sys.argv) > 1:
        try:
            raw = sys.argv[1]
            raw_tokens = raw.split("-")
            if len(raw_tokens) == 2:
                rc_module = int(raw_tokens[0]) - 2000
                rc_desc = int(raw_tokens[1])
            elif raw == "update":
                print("Regenerating result/range databases...")
                arc_db_gen.generate_dbs()
                print("Result/range databases were successfully generated!")
                sys.exit()
            else:
                try:
                    rc = int(raw, 16)
                except:
                    rc = int(raw)
                rc_module = rc & 0x1FF
                rc_desc = (rc >> 9) & 0x1FFF
        except:
            print("The provided result was not in a valid format...")
            sys.exit()

        print(f"Searching for result {format_rc(rc_module, rc_desc)}...")
        print()

        lookup_rc(rc_module, rc_desc)
    else:
        print("No result was provided...")
        sys.exit()