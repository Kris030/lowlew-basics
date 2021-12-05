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
	char name[10];
} Rectangle;

void func(const char str[]) {
	printf("from function: %s %d\n", str, 123);
}
// ------ basic syntax ------

// ------ pointer funcs ------
void pog(char* cp) {
	(*cp)++;
}

long* sus() {
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

	int *p = &a, v = *p;

	func(s);

	Rectangle r = { { 12, 11 }, 10, 9, "876543210" }, rs[2];
	puts(sizeof(rs) == 2 * ((4 + 4) + (4 + 4 + 10)) ? "true" : "false");

	Rectangle *rp = &r;

	printf("ternary and arrow operators: %s\n", rp->pos.x > 10 ? "true" : "false");
	// ------ basic syntax ------

	// ------ everything's a number ------
	printf("characters are numbers: ");
	for (char c = 'A'; c < 'Z'; c++)
		printf("%c", c);
	printf("\n");

	printf("pointers are numbers: ");
	for (char* i = s; i < s + sizeof(s); i++)
		printf("%c", *i);
	printf("\n");
	// ------ everything's a number ------

	// ------ pointer fun ------
	int *k = 0;
	k++;
	printf("pointer arimethric: %p, ", k);

	b += 1;
	printf("%c\n", b);

	pog(&b);
	printf("pog: %c\n", b);

	long* l = sus();
	//printf("%l\n", *l);
	printf("sus pointer: %p\n", l);
	// ------ pointer fun ------

	// ------ dynamic memory ------
	int len = 123;
	int* arr = (int*) malloc(len * sizeof(int));

	if (arr) {
		printf("malloc: %p\n", arr);
		free(arr);
	} else
		puts("Couldn't allocate memory");
	// ------ dynamic memory ------

	// ------ misc ------
	under();

	int j = 10;
	printf("allmighty goto: x");
	loop:
	printf("d");
	if (j-- > 0)
		goto loop;
	printf("\n");
	// ------ misc ------

	// ------ bitwise operators ------

	unsigned char n = 0b11100101;
	pbin("original", n);
	pbin("or", n | 0b11);
	pbin("and", n & 0b11100000);
	pbin("left shift", n << 1);
	pbin("right shift", n >> 1);
	pbin("binary not", ~n);
	pbin("xor", n ^ 0b111);
}

int _pbin(unsigned char n, char *p) {
	unsigned char s = n >> 1;
	int r = 1;
	if (s)
		r += _pbin(s, p - 1);
	*p = '0' + (n & 1);
	return r;
}
void pbin(const char str[], unsigned char n) {
	char arr[9]; arr[8] = '\0';
	int r = 8 - _pbin(n, arr + 7);

	for (int i = 0; i < r; i++)
		printf("0");

	printf("%s - %s\n", arr + r, str);
}
// ------ bitwise operators ------

// ------ misc ------
void under() {
	puts("headers: hello I'm under the water please help");
}
// ------ misc ------
