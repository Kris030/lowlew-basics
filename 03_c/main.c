#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "main.h"


void pog(int* p) {
	(*p)++;
}

int* sus() {
	int j = 123;
	return &j;
}


/*
typedef struct {
	int x, y;
	char name[10];
} point;

typedef struct {
	point pos;
	int w, h;
} rect;
*/

int main() {
	
	int i = 10;
	int* p = &i;

	printf("%d\n", i);
	printf("%p\n", p);

	pog(p);
	printf("%d\n", i);

	// ---

	//int* p2 = sus();
	//printf("%d\n", *p2);

	// ---

	for (char c = 'A'; c < 'Z'; c++)
		printf("%c", c);
	printf("\n");

	char arr[11] = "hello world";
	for (char* i = arr; i < arr + sizeof(arr); i++) {
		// printf("%d", arr[i]); 
		// =
		printf("%c", *i);
	}
	printf("\n");
	
	int* a = arr; // 0 index
	a++; // 1 index

	int boo = 10;
	puts(boo ? "true" : "false");
	
	for (int x = 0; x < 100; x++)
		for (int y = 0; y < 100; y++)
			goto asd;
	puts("dead code");
	asd:
	
	int* arr2 = (int*) malloc(10000000 * sizeof(int));

	if (!arr2)
		puts("couldn't allocate memory");

	printf("%d\n", arr);
	free(arr2);

	char b[10];
	char d;

	// b[11] == d

	

	/*
	rect* rs = malloc(10 * sizeof(rect));

	point p = { -5, 56, "0123465798" };

	rect r;
	r.w = 10;
	r.h = 11;
	r.pos = p;
	*/

	test();
}

void test() {
	puts("test called");
}
