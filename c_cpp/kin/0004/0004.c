/*
https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=1040101&docId=329510623
*/
#include <stdio.h>
#include <stdlib.h>
int main() {
	int a, b, i;
	for (i = 0; i < 400; i++) {
		a = rand() % 201 + 300;
		b = rand() % 201 + 600;
		printf("(%d , %d )\n", a, b);
	}
	return 0;
}