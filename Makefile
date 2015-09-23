include /usr/share/templar/make/Makefile

ALL:=$(TEMPLAR_ALL)
ALL_DEP:=$(TEMPLAR_ALL_DEP)

ALL_PY:=$(shell find src -name "*.py")
ALL_STAMP:=$(addsuffix .stamp, $(basename $(ALL_PY)))

.PHONY: all
all: check_all

.PHONY: check_all
check_all: $(ALL_STAMP)

.PHONY: check
check: check_ws check_return check_if check_has_key

.PHONY: check_ws
check_ws:
	$(info doing [$@])
	@git grep -E "\s$$" -- '*.py' || exit 0

.PHONY: check_return
check_return:
	$(info doing [$@])
	@git grep -l -E "return\(.*\)$$" -- '*.py' || exit 0
	@git grep -l -E "return \(.*\)$$" -- '*.py' || exit 0

.PHONY: check_if
check_if:
	$(info doing [$@])
	@git grep -l -E "if \(" -- '*.py' || exit 0
	@git grep -l -E "if\(" -- '*.py' || exit 0

.PHONY: check_has_key
check_has_key:
	$(info doing [$@])
	@git grep -l "has_key" -- '*.py' || exit 0

$(ALL_STAMP): %.stamp: %.py
	$(info doing [$@])
	@scripts/syntax_check.py $<
	@touch $@

.PHONY: debug_me
debug_me:
	echo $(ALL_STAMP)

.PHONY: show_shbang
show_shbang:
	find src -name "*.py" -and -executable -exec head -1 {} \; | sort | uniq
