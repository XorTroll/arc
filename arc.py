import json
import os
import sys
import arc_db_gen
import arc_cpp_gen
import requests

DIR = os.path.dirname(os.path.realpath(__file__))
DEFAULT_RC_HPP_DIR = os.path.join(DIR, "default_rc_hpps")

def format_rc(rc_module, rc_desc):
    rc = ((rc_module & 0x1FF) | (rc_desc & 0x1FFF) << 9)
    rc_fmt = f"{2000 + rc_module:04}-{rc_desc:04}"
    rc_hex = f"0x{rc:X}"
    return f"({rc_fmt}, {rc_hex})"

def try_find_rc_hpp_path(rc_hpp_item):
    paths = []

    paths.append(rc_hpp_item)
    paths.append(os.path.join(os.getcwd(), rc_hpp_item))

    rc_hpp_item_2 = rc_hpp_item + ".rc.hpp"
    paths.append(rc_hpp_item_2)
    paths.append(os.path.join(os.getcwd(), rc_hpp_item_2))

    paths.append(os.path.join(DEFAULT_RC_HPP_DIR, rc_hpp_item))
    paths.append(os.path.join(DEFAULT_RC_HPP_DIR, rc_hpp_item_2))

    for path in paths:
        if os.path.isfile(path):
            return path

    if requests.get(rc_hpp_item).status_code == 200:
        return rc_hpp_item

    return None

def check_dbs():
    if not os.path.isfile(arc_db_gen.RC_DB_JSON) or not os.path.isfile(arc_db_gen.RANGE_DB_JSON):
        print("Databases were not found (did you forget to generate them...?)")
        sys.exit()

def lookup_rc(rc_module, rc_desc):
    with open(arc_db_gen.RC_DB_JSON, "r") as f:
        all_rcs = json.load(f)
    
    with open(arc_db_gen.RANGE_DB_JSON, "r") as f:
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
    print("== arc - Atmosphère (and custom) result utility ==")
    print("==================================================")
    print()
    print("== Generate databases ==")
    print("'arc.py gen_db <sources>'")
    print("==== examples: 'arc.py gen_db default', 'arc.py gen_db ams+goldleaf+../dummy/rc_defs.hpp'")
    print()
    print("== Search result ==")
    print("'arc.py rc <rc_code>'")
    print("==== examples: 'arc.py 2002-0001', 'arc.py 0x202'")
    print()
    print("== Generate C++ header ==")
    print("'arc.py gen_cpp <namespace> <macro_prefix> <out_hpp>'")
    print("==== examples: 'arc.py gen_cpp testmod TESTMACRO test.hpp'")
    print()
    print("==================================================")
    print()

    if len(sys.argv) > 1:
        main_param = sys.argv[1]

        if main_param == "rc":
            if len(sys.argv) < 3:
                print("No result was provided...")
                sys.exit()
            raw_rc = sys.argv[2]
            raw_rc_tokens = raw_rc.split("-")
            if len(raw_rc_tokens) == 2:
                rc_module = int(raw_rc_tokens[0]) - 2000
                rc_desc = int(raw_rc_tokens[1])
            else:
                try:
                    try:
                        rc = int(raw_rc, 16)
                    except:
                        rc = int(raw_rc)
                except:
                    print("An invalid result was provided!")
                rc_module = rc & 0x1FF
                rc_desc = (rc >> 9) & 0x1FFF

            check_dbs()
            print(f"Searching for result {format_rc(rc_module, rc_desc)}...")
            print()

            try:
                lookup_rc(rc_module, rc_desc)
            except Exception as e:
                print("Execution error: " + str(e))
        elif main_param == "gen_db":
            if len(sys.argv) < 3:
                print("No sources were provided...")
                sys.exit()
            srcs_raw = sys.argv[2]
            src_tokens_raw = srcs_raw.split("+")
            do_ams = False
            rc_hpps = []
            for token in src_tokens_raw:
                if token == "ams":
                    do_ams = True
                elif token == "default":
                    do_ams = True
                    for default_rc_hpp in os.listdir(DEFAULT_RC_HPP_DIR):
                        rc_hpps.append(os.path.join(DEFAULT_RC_HPP_DIR, default_rc_hpp))
                else:
                    rc_hpp_path = try_find_rc_hpp_path(token)
                    if rc_hpp_path is not None:
                        rc_hpps.append(rc_hpp_path)
                    else:
                        print(f"Source does not exist: '{rc_hpp_path}'")
                        sys.exit()
            
            # Remove duplicates
            rc_hpps = list(dict.fromkeys(rc_hpps))
            if len(rc_hpps) == 0:
                print("No actual sources were provided...")
                sys.exit()
            arc_db_gen.generate_dbs(do_ams, rc_hpps)
            print("Done!")
        elif main_param == "gen_cpp":
            if len(sys.argv) < 5:
                print("Not enough input parameters were provided...")
                sys.exit()
            namespace = sys.argv[2]
            macro_prefix = sys.argv[3]
            out_hpp = sys.argv[4]

            check_dbs()
            arc_cpp_gen.generate_cpp(namespace, macro_prefix, out_hpp)
            print("Done!")
    else:
        print("No command was provided...")