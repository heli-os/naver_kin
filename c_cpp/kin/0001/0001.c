/*
https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=104&docId=329415766&mode=answer
*/
#include <stdio.h>

int main() {
	int max = 0, min = 100;
	int i, n, num;
	printf("�л� ���� �Է��ϼ��� : ");
	scanf("%d", &n);
	printf("������ �Է��ϼ���(0~100) : ");
	for (i = 0; i < n; i++) {
		scanf("%d", &num);
		if (num > max)
			max = num;
		if (num < min)
			min = num;
	}
	printf("1���� %d��, ����� %d��\n", max, min);
	return 0;
}