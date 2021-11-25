
all:
	[[ -d bin ]] || mkdir bin
	gcc -w main.c -o bin/main

clean:
	rm -f bin/*

run: all
	./bin/main
