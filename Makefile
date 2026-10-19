# Zt3 firmware analysis pipeline.  Ghidra stages need GHIDRA_INSTALL_DIR; see README.md.
PY      ?= python3
ZT3     ?= zt3

.PHONY: setup import match export decompile families plan validate lint doctor coverage apply docs test all clean-project snapshot

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

validate:         ## every annotation file against schema, families and its work packet
	for f in annotations/*/functions/*.json; do \
	  c=$$(basename $$(dirname $$(dirname $$f))); b=$$(basename $$f .json); \
	  p=analysis/work/$$c/$$b.md; [ -f $$p ] && $(ZT3) validate $$f --packet $$p || $(ZT3) validate $$f; done

lint:             ## style/hygiene lint of annotation text
	$(ZT3) lint

doctor:           ## freshness, ownership and orphan gate (no Ghidra needed)
	$(ZT3) doctor && $(ZT3) families --check && $(ZT3) docs --check

coverage:         ## report: every function/variable/table/type described?  (not a gate until the data stage)
	$(ZT3) check

apply:            ## write names, comments, types into the Ghidra programs
	$(ZT3) apply

docs:             ## regenerate docs/<component>/*.md
	$(ZT3) docs

all: import match export decompile families doctor

test:
	$(PY) -m pytest -q tests

clean-project:
	rm -rf ghidra_project analysis/decomp analysis/work

snapshot:         ## regenerate docs, run the gates, commit everything (MSG="...")
	$(ZT3) docs
	$(ZT3) doctor
	$(ZT3) families --check
	$(ZT3) docs --check
	git add -A && git commit -q -m "$(MSG)" -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>" -m "Claude-Session: https://claude.ai/code/session_01UyWHPv28MWcuvyzBdwFRqx"
