#include "stdio.h"

void itoa10(int val, char* res) {
	
	char* ptr1 = res;

	do {
		int rem = val % 10;
		rem += '0';
		
		*ptr1 = rem;
		ptr1++;
		
		val /= 10;
	} while (val > 0);

	*ptr1 = '\0';
	ptr1--;

	char* ptr2 = res;
	char tmp;
	while (ptr2 < ptr1) {
		tmp = *ptr1;
		*ptr1 = *ptr2;
		ptr1--;
		*ptr2 = tmp;
		ptr2++;
	}
}

int main() {
	char buff[4];
	itoa10(234, buff);
	puts(buff);
}

