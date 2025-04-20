#!/bin/bash

# Include extra results here which might be useful for users

GOLDLEAF_RC_HPP=https://raw.githubusercontent.com/XorTroll/Goldleaf/master/Goldleaf/include/base_Results.rc.hpp
ULAUNCH_RC_HPP=https://raw.githubusercontent.com/XorTroll/uLaunch/unew/libs/uCommon/include/ul/ul_Results.rc.hpp

python arc.py gen_db default+$GOLDLEAF_RC_HPP+$ULAUNCH_RC_HPP
python arc.py gen_md docs/index.md
