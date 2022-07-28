import json
import os
import requests

def query_ams_rc_src_hpps():
    src_hpps = list()

    # We assume for simplicity that all Atmosphere result-defining headers are inside "libraries/libvapours/include/vapours/results/"
    # At least for now this is the case
    gh_api_url = "https://api.github.com/repos/Atmosphere-NX/Atmosphere/contents/libraries/libvapours/include/vapours/results"
    entries = json.loads(requests.get(gh_api_url).content.decode("utf-8"))
    for entry in entries:
        entry_name = entry["name"]
        entry_type = entry["type"]
        if (entry_type == "file") and entry_name.endswith("_results.hpp"):
            entry_url = entry["download_url"]
            src_hpps.append(entry_url)

    return src_hpps


def load_ams_rc_src_hpp(src_hpp_url):
    return requests.get(src_hpp_url).content.decode("utf-8")

def query_local_rc_src_hpps():
    src_hpps = list()

    local_rc_src_hpp_dir = "local_rc_src_hpps"
    for entry_name in os.listdir(local_rc_src_hpp_dir):
        if entry_name.endswith("_results.hpp"):
            src_hpps.append(os.path.join(local_rc_src_hpp_dir, entry_name))

    return src_hpps

def load_local_rc_src_hpp(src_hpp_path):
    with open(src_hpp_path, "r") as f:
        return f.read()

def process_rc_src_hpp(src_hpp, namespace_modules, namespace_descs, namespace_ranges, cur_namespace):
    for src_hpp_line in src_hpp.split("\n"):
        src_hpp_line_spaced = src_hpp_line.lstrip().split(" ")
        if len(src_hpp_line_spaced) > 0:
            if src_hpp_line_spaced[0] == "namespace":
                assert len(src_hpp_line_spaced) == 3
                assert src_hpp_line_spaced[2] == "{"
                assert cur_namespace == ""
                
                cur_namespace = src_hpp_line_spaced[1]
                print("Entering namespace '" + cur_namespace + "'...")
            elif src_hpp_line_spaced[0] == "}":
                assert len(src_hpp_line_spaced) == 1
                assert cur_namespace != ""

                print("Exiting namespace...")
                cur_namespace = ""

        src_hpp_line_tokens = src_hpp_line.replace(" ", "").replace(",", "|").replace("(", "|").replace(")", "|").split("|")
        if len(src_hpp_line_tokens) > 0:
            if src_hpp_line_tokens[0] == "R_DEFINE_NAMESPACE_RESULT_MODULE":
                assert len(src_hpp_line_tokens) >= 4
                assert src_hpp_line_tokens[3].startswith(";")

                namespace = src_hpp_line_tokens[1]
                rc_module = src_hpp_line_tokens[2]
                assert namespace not in namespace_modules
                namespace_modules[namespace] = rc_module
                print("Got module: namespace '" + namespace + "', module '" + rc_module + "'")
            elif src_hpp_line_tokens[0] == "R_DEFINE_ERROR_RESULT":
                assert len(src_hpp_line_tokens) >= 4
                assert src_hpp_line_tokens[3].startswith(";")

                rc_name = src_hpp_line_tokens[1]
                rc_desc = src_hpp_line_tokens[2]
                if cur_namespace not in namespace_descs:
                    namespace_descs[cur_namespace] = list()
                namespace_descs[cur_namespace].append({ "name": rc_name, "desc": rc_desc })
                # print("Got result: name '" + rc_name + "', desc '" + rc_name + "'")
            elif src_hpp_line_tokens[0] == "R_DEFINE_ERROR_RANGE":
                assert len(src_hpp_line_tokens) >= 5
                assert src_hpp_line_tokens[4].startswith(";")

                rg_name = src_hpp_line_tokens[1]
                rg_start_desc = src_hpp_line_tokens[2]
                rg_end_desc = src_hpp_line_tokens[3]
                if cur_namespace not in namespace_ranges:
                    namespace_ranges[cur_namespace] = list()
                namespace_ranges[cur_namespace].append({
                    "name": rg_name,
                    "start_desc": rg_start_desc,
                    "end_desc": rg_end_desc
                })
                # print("Got result range: name '" + rg_name + "', start desc '" + rg_start_desc + "', end desc '" + rg_end_desc + "'")

def generate_dbs():
    namespace_modules = dict()
    namespace_descs = dict()
    namespace_ranges = dict()
    cur_namespace = ""

    for ams_src_hpp_url in query_ams_rc_src_hpps():
        process_rc_src_hpp(load_ams_rc_src_hpp(ams_src_hpp_url), namespace_modules, namespace_descs, namespace_ranges, cur_namespace)

    for local_src_hpp_path in query_local_rc_src_hpps():
        process_rc_src_hpp(load_local_rc_src_hpp(local_src_hpp_path), namespace_modules, namespace_descs, namespace_ranges, cur_namespace)

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

    with open("arc_rc_db.json", "w") as f:
        f.write(json.dumps(all_rcs, indent=4))

    with open("arc_range_db.json", "w") as f:
        f.write(json.dumps(all_ranges, indent=4))

if __name__ == "__main__":
    generate_dbs()
    print("Done generating and saving result/range databases from Atmosphère (and custom) result definitions!")