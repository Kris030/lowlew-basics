#include "stdio.h"

void itoa10(int val, char* res) {
	
	char* ecx = res;

	do {
		int rem = val % 10;
		rem += '0';
		
		*ecx = rem;
		ecx++;
		
		val /= 10;
	} while (val > 0);

	*ecx = '\0';
	ecx--;

	char* ebx = res, eax, edx;
	while (ebx < ecx) {
		
		edx = *ecx;

		eax = *ebx;
		*ecx = eax;
		
		ecx--;
		
		*ebx = edx;
		
		ebx++;
	}
}

int main() {
	char buff[20];
	itoa10(524345, buff);
	puts(buff);
}

