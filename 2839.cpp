#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;

int main()
{
	int N, min = 0, res = 0, num = 0;
	cin >> N;

	min += N / 5;
	res =  N % 5;
	min += res / 3;

	if (res % 3 == 0) { // 나머지 없이 완전히 끝났을 경우
		cout << min << '\n';
		return 0;
	}
	
	else if (res >= 3) { // 5로 나누었을 때 나머지가 3보다 큰 경우
		for (int i = 1; i <= (res / 3); i++) { // 3 나눈 걸 하나씩 다시 곱해서 가능한 지 확인
			num = (res % 3) + (3 * i);
			if (num % 3 == 0) {
				min = min - i + (num / 3);
				cout << min << '\n';
				return 0;
			}
			min--;
		}
		for (int i = 1; i <= (N / 5); i++) { // 5 나눈 걸 하나씩 다시 곱해서 가능한 지 확인
			num = num + (5 * i);
			if (num % 3 == 0) {
				min = min - i + (num / 3);
				cout << min << '\n';
				return 0;
			}
		}
		cout << -1 << '\n'; // 다해도 되지 않을 경우
		return 0;
	}

	else { // 5로 나누었을 때 나머지가 3보다 작은 경우
		for (int i = 1; i <= (N / 5); i++) { // 5 나눈 걸 하나씩 다시 곱해서 가능한 지 확인
			num = (res % 3) + (5 * i);
			if (num % 3 == 0) {
				min = min - i + (num / 3);
				cout << min << '\n';
				return 0;
			}
		}
		cout << -1 << '\n'; // 다해도 되지 않을 경우
	}
	return 0;
}