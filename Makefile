EXAMPLES := $(wildcard examples/*.py)
EXAMPLE_OUTPUTS := $(patsubst %.py,%.py.txt,$(EXAMPLES))

all: $(EXAMPLE_OUTPUTS)

examples/%.py.txt: examples/%.py
	poetry run python $< > $@
