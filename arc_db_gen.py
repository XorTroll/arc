import json
import os
import requests

DIR = os.path.dirname(os.path.realpath(__file__))
RC_DB_JSON = os.path.join(DIR, "arc_rc_db.json")
RANGE_DB_JSON = os.path.join(DIR, "arc_range_db.json")

def query_ams_rc_hpps():
    rc_hpps = list()

    # We assume for simplicity that all Atmosphere result-defining headers are inside "libraries/libvapours/include/vapours/results/"
    # At least for now, this is the case
    gh_api_url = "https://api.github.com/repos/Atmosphere-NX/Atmosphere/contents/libraries/libvapours/include/vapours/results"
    entries = json.loads(requests.get(gh_api_url).content.decode("utf-8"))
    for entry in entries:
        entry_name = entry["name"]
        entry_type = entry["type"]
        if (entry_type == "file") and entry_name.endswith("_results.hpp"):
            entry_url = entry["download_url"]
            rc_hpps.append(entry_url)

    return rc_hpps


def load_ams_rc_hpp(rc_hpp_url):
    return requests.get(rc_hpp_url).content.decode("utf-8")

def query_local_rc_hpps():
    rc_hpps = list()

    local_rc_hpp_dir = "local_rc_hpps"
    for entry_name in os.listdir(local_rc_hpp_dir):
        if entry_name.endswith("_results.hpp"):
            rc_hpps.append(os.path.join(local_rc_hpp_dir, entry_name))

    return rc_hpps

def load_local_rc_hpp(rc_hpp_path):
    with open(rc_hpp_path, "r") as f:
        return f.read()

def process_rc_hpp(rc_hpp, namespace_modules, namespace_descs, namespace_ranges, cur_namespace):
    for rc_hpp_line in rc_hpp.split("\n"):
        rc_hpp_line_spaced = rc_hpp_line.lstrip().split(" ")
        if len(rc_hpp_line_spaced) > 0:
            if rc_hpp_line_spaced[0] == "namespace":
                assert len(rc_hpp_line_spaced) == 3
                assert rc_hpp_line_spaced[2] == "{"
                assert cur_namespace == ""
                
                cur_namespace = rc_hpp_line_spaced[1]
                # print("Entering namespace '" + cur_namespace + "'...")
            elif rc_hpp_line_spaced[0] == "}":
                assert len(rc_hpp_line_spaced) == 1
                assert cur_namespace != ""

                # print("Exiting namespace...")
                cur_namespace = ""

        rc_hpp_line_tokens = rc_hpp_line.replace(" ", "").replace(",", "|").replace("(", "|").replace(")", "|").split("|")
        if len(rc_hpp_line_tokens) > 0:
            if rc_hpp_line_tokens[0] == "R_DEFINE_NAMESPACE_RESULT_MODULE":
                assert len(rc_hpp_line_tokens) >= 4
                assert rc_hpp_line_tokens[3].startswith(";")

                namespace = rc_hpp_line_tokens[1]
                rc_module = rc_hpp_line_tokens[2]
                assert namespace not in namespace_modules
                namespace_modules[namespace] = rc_module
                print("Got module: namespace '" + namespace + "', module '" + rc_module + "'")
            elif rc_hpp_line_tokens[0] == "R_DEFINE_ERROR_RESULT":
                assert len(rc_hpp_line_tokens) >= 4
                assert rc_hpp_line_tokens[3].startswith(";")

                rc_name = rc_hpp_line_tokens[1]
                rc_desc = rc_hpp_line_tokens[2]
                if cur_namespace not in namespace_descs:
                    namespace_descs[cur_namespace] = list()
                namespace_descs[cur_namespace].append({ "name": rc_name, "desc": rc_desc })
            elif rc_hpp_line_tokens[0] == "R_DEFINE_ERROR_RANGE":
                assert len(rc_hpp_line_tokens) >= 5
                assert rc_hpp_line_tokens[4].startswith(";")

                rg_name = rc_hpp_line_tokens[1]
                rg_start_desc = rc_hpp_line_tokens[2]
                rg_end_desc = rc_hpp_line_tokens[3]
                if cur_namespace not in namespace_ranges:
                    namespace_ranges[cur_namespace] = list()
                namespace_ranges[cur_namespace].append({
                    "name": rg_name,
                    "start_desc": rg_start_desc,
                    "end_desc": rg_end_desc
                })

def generate_dbs(do_ams, local_rc_hpps):
    namespace_modules = dict()
    namespace_descs = dict()
    namespace_ranges = dict()
    cur_namespace = ""

    if do_ams:
        for ams_rc_hpp_url in query_ams_rc_hpps():
            process_rc_hpp(load_ams_rc_hpp(ams_rc_hpp_url), namespace_modules, namespace_descs, namespace_ranges, cur_namespace)

    for local_rc_hpp_path in local_rc_hpps:
        process_rc_hpp(load_local_rc_hpp(local_rc_hpp_path), namespace_modules, namespace_descs, namespace_ranges, cur_namespace)

    all_rcs = list()
    all_ranges = list()
    for namespace in namespace_descs:
        assert namespace in namespace_modules
        namespace_module = int(namespace_modules[namespace])

        if namespace in namespace_descs:
            for rc_name_desc in namespace_descs[namespace]:
                all_rcs.append({
                    "name": rc_name_desc["name"],
                    "module": namespace_module,
                    "module_name": namespace,
                    "desc": int(rc_name_desc["desc"])
                })
        if namespace in namespace_ranges:
            for rg in namespace_ranges[namespace]:
                all_ranges.append({
                    "name": rg["name"],
                    "module": namespace_module,
                    "module_name": namespace,
                    "start_desc": int(rg["start_desc"]),
                    "end_desc": int(rg["end_desc"])
                })

    with open(RC_DB_JSON, "w") as f:
        f.write(json.dumps(all_rcs, indent=4))

    with open(RANGE_DB_JSON, "w") as f:
        f.write(json.dumps(all_ranges, indent=4))
