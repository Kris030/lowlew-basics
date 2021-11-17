
all:
	[[ -d bin ]] || mkdir bin
#	nasm -f elf64 bootloader.s -o bin/bootloader.o
	gcc -c -ffreestanding -nostartfiles -nostdlib -nodefaultlibs -nolibc -m16 -o bin/entry.o entry.c
	gcc -c -ffreestanding -nostartfiles -nostdlib -nodefaultlibs -nolibc -m16 -masm=intel -o bin/bootloader.o bootloader.s
	gcc -o final bin/*.o

clean:
	rm -f bin/*