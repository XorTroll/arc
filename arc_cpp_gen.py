import json
import os
import arc_db_gen

DIR = os.path.dirname(os.path.realpath(__file__))
TEMPLATE_HPP = os.path.join(DIR, "arc_cpp_gen_template.hpp")


def format_rc(rc_module, rc_desc):
    rc = ((rc_module & 0x1FF) | (rc_desc & 0x1FFF) << 9)
    rc_fmt = f"{2000 + rc_module:04}-{rc_desc:04}"
    rc_hex = f"0x{rc:X}"
    return f"({rc_fmt}, {rc_hex})"


def generate_cpp(namespace, macro_prefix, out_hpp):
    with open(TEMPLATE_HPP, "r") as in_h:
        hpp = in_h.read()

        with open(arc_db_gen.RC_DB_JSON, "r") as f:
            all_rcs = json.load(f)

        with open(arc_db_gen.RANGE_DB_JSON, "r") as f:
            all_ranges = json.load(f)

        rcs_src = ""
        rcs_src_indent = "    "
        rc_names_src = ""
        rc_names_src_indent = "        "
        for rc in all_rcs:
            rc_src = f"namespace {rc['module_name']} {{ constexpr Result Result{rc['name']} = $MACRO_RC_MAKE({rc['module']}, {rc['desc']}); }}"
            rcs_src += rcs_src_indent + rc_src + "\n"

            rc_name_src = f"std::make_pair(::$NAMESPACE::{rc['module_name']}::Result{rc['name']}, std::make_pair(\"{rc['module_name']}\", \"{rc['name']}\")),"
            rc_names_src += rc_names_src_indent + rc_name_src + "\n"
        try:
            rcs_src.removesuffix("\n")
            rc_names_src.removesuffix("\n")
        except AttributeError:
            if rcs_src.endswith("\n"):
                rcs_src = rcs_src[:-len("\n")]
            if rc_names_src.endswith("\n"):
                rc_names_src = rc_names_src[:-len("\n")]
        hpp = hpp.replace("$RES_DEFINE", rcs_src)
        hpp = hpp.replace("$RES_TABLE", rc_names_src)

        ranges_src = ""
        ranges_src_indent = "    "
        range_names_src = ""
        range_names_src_indent = "        "
        for rc_range in all_ranges:
            range_src = f"namespace {rc_range['module_name']} {{ constexpr ResultRange ResultRange{rc_range['name']}({rc_range['module']}, {rc_range['start_desc']}, {rc_range['end_desc']}); }}"
            ranges_src += ranges_src_indent + range_src + "\n"

            range_name_src = f"std::make_pair(::$NAMESPACE::{rc_range['module_name']}::ResultRange{rc_range['name']}, std::make_pair(\"{rc_range['module_name']}\", \"{rc_range['name']}\")),"
            range_names_src += range_names_src_indent + range_name_src + "\n"
        hpp = hpp.replace("$RES_RANGE_DEFINE", ranges_src)
        hpp = hpp.replace("$RES_RANGE_TABLE", range_names_src)

        hpp = hpp.replace("$NAMESPACE", namespace)
        hpp = hpp.replace("$MACRO", macro_prefix)

        if os.path.exists(out_hpp):
            with open(out_hpp, "r") as out_h:
                old_hpp = out_h.read()
                if old_hpp == hpp:
                    print(f"{out_hpp} is up to date!")
                    return

        with open(out_hpp, "w") as out_h:
            out_h.write(hpp)
