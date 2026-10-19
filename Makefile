# Zt3 firmware analysis pipeline.  Requires Ghidra (see docs/methodology.md) and the zt3re package.
PY      ?= python3
ZT3     ?= zt3

.PHONY: setup import match export decompile families plan check apply docs test all clean-project

setup:            ## install the harness (editable) with PyGhidra
	$(PY) -m pip install -e '.[dev]'

import:           ## import + analyse every image in firmware/ into ghidra_project/
	$(ZT3) import

match:            ## Ghidra Version Tracking between versions of each component
	$(ZT3) match

export:           ## per-image JSON facts -> analysis/export
	$(ZT3) export

decompile:        ## decompiled C cache -> analysis/decomp (not committed)
	$(ZT3) decompile

families:         ## cross-version function / variable families -> analysis/families
	$(ZT3) families

plan:             ## annotation work packets -> analysis/work
	$(ZT3) plan

check:            ## coverage gate: every function/variable/table/type described?
	$(ZT3) check

apply:            ## write names, comments, types into the Ghidra programs
	$(ZT3) apply

docs:             ## regenerate docs/<component>/*.md
	$(ZT3) docs

all: import match export decompile families check

test:
	$(PY) -m pytest -q tests

clean-project:
	rm -rf ghidra_project analysis/decomp analysis/work
