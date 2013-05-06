# Building a SoC in python with Migen
# http://brandonhamilton.github.io/building-a-soc-with-migen

all: build/soc_top.bit

build/soc_top.bit:
	@./build.py

hdl:
	@./build.py --no-run

clean:
	rm -rf build/*

.PHONY: hdl clean