#include <iostream>
#include <climits>
using namespace std;

int main()
{
	int i, j, temp;
	int num, cnt = 0;

	cin >> num;
	int tmp = num;

	// 배열 크기 계산
	while (tmp != 0) {
		tmp /= 10;
		cnt++;
	}

	int* arr = new int[cnt];

	// 배열에 입력
	do {
		for (i = 0; i < cnt; i++) {
			arr[i] = num % 10;
			num /= 10;
		}		
	} while (num != 0);
	
	// 삽입정렬
	for (i = 0; i < cnt - 1; i++) {
		j = i;
		while (j >= 0 && arr[j] < arr[j + 1]) {
			temp = arr[j];
			arr[j] = arr[j + 1];
			arr[j + 1] = temp;
			j--;
		}
	}

	for (i = 0; i < cnt; i++) {
		cout << arr[i];
	}
	
	return 0;
}
