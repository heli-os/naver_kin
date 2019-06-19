/*
https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=1040101&docId=329480275
*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {

	int i;
	int j;
	int lotto[6];
	int input;

	srand(1);

	srand((unsigned)time(NULL));

	for (i = 0; i < 6; i++) {
		lotto[i] = rand() % 45 + 1;
		for (j = 0; j < i; j++) {
			if (lotto[j] == lotto[i]) {
				i--;
			}
		}
	}
	printf("***before***\n");
	for (i = 0; i < 6; i++) {
		printf("%5d", lotto[i]);
	}
	printf("\n정렬 (오름차순 : 1, 내림차순 : 2) >> ");
	scanf("%d", &input);
	
	for (int i = 0; i < 5; ++i)
	{
		for (int j = 0; j < 5-i; ++j)
		{
			if (input == 1) {//오름차순 정렬
				if (lotto[j] > lotto[j+1])
				{
					int temp = lotto[j];
					lotto[j] = lotto[j+1];
					lotto[j+1] = temp;
				}
			}
			else if (input == 2) // 내림차순 정렬
			{
				if (lotto[j] < lotto[j+1])
				{
					int temp = lotto[j];
					lotto[j] = lotto[j + 1];
					lotto[j + 1] = temp;
				}
			}
			
		}
	}
	printf("\n***after***\n");
	


	for (i = 0; i < 6; i++)
	{
		printf(" %5d ", lotto[i]);
	}
}
