/*
https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=1040101&docId=329478352
*/
#include <stdio.h>
#include <stdlib.h>

int main() {
	int i, num, num_arr[10] = { 0, };
	for (i = 0; i < 10000; i++)
	{
		num = rand() % 10+1;
		num_arr[num-1]++;
	}
	for (i = 0; i < 10; i++) {
		printf("%dÀÇ È½¼ö : %d/10000\n", i + 1, num_arr[i]);
	}
	return 0;
}