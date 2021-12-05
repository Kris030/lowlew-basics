// ------ basic syntax ------
#include <stdio.h>
#include <stdlib.h>

#define MY_CONST 654
#define MY_MACRO(a, b) (a) + (b)

typedef struct {
	int x, y;
} Point;

typedef struct {
	Point pos;
	int w, h;
	char[10] name;
} Rectangle;

void func(char[] str) {
	puts(s);
}
// ------ basic syntax ------

// ------ pointer funcs ------
void pog(char* cp) {
	(*cp)++;
}

void sus() {
	long l = 42069911;
	return &l;
}
// ------ pointer funcs ------

// ------ basic syntax ------
int main() {
	
	int a = MY_CONST + MY_MACRO(4, 8);
	char c = 'c', b = 'b';
	char s[] = "hello world";
	int i[10];

	int *p = &a;
	int v = *p;

	func(s);

	Rectangle r = { { 12, 11 }, 10, 9, "876543210" };
	Rectangle *rp = &r;

	puts(r->pos.x > 10 ? "true" : "false");
	// ------ basic syntax ------

	// ------ everything's a number ------
	for (char c = 'A'; c < 'Z'; c++)
		printf("%c", c);
	printf("\n");

	for (char* i = s; i < s + sizeof(s); i++)
		printf("%c", *i);
	printf("\n");
	// ------ everything's a number ------

	// ------ pointer fun ------
	int *r = 0;
	r++;
	printf("%p\n", r);

	b += 1;
	printf("%c\n", b);

	pog(b);
	printf("%c\n", b);

	long l = sus();
	printf("%l\n", l);
	// ------ pointer fun ------

	// ------ dynamic memory ------
	int len = 123;
	int* arr = (int*) malloc(len * sizeof(int));

	if (arr) {
		printf("%p\n", arr);
		free(arr);
	} else
		puts("Couldn't allocate memory");
	// ------ dynamic memory ------

	// ------ misc ------
	under();

	int j = 10;
	printf("x");
	loop:
	printf("d")
	if (j-- > 0)
		goto loop;
	printf("\n");

}

void under() {
	puts("hello I'm under the water please help");
}

// ------ misc ------
