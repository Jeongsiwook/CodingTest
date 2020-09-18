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

	if (res % 3 == 0) { // ������ ���� ������ ������ ���
		cout << min << '\n';
		return 0;
	}
	
	else if (res >= 3) { // 5�� �������� �� �������� 3���� ū ���
		for (int i = 1; i <= (res / 3); i++) { // 3 ���� �� �ϳ��� �ٽ� ���ؼ� ������ �� Ȯ��
			num = (res % 3) + (3 * i);
			if (num % 3 == 0) {
				min = min - i + (num / 3);
				cout << min << '\n';
				return 0;
			}
			min--;
		}
		for (int i = 1; i <= (N / 5); i++) { // 5 ���� �� �ϳ��� �ٽ� ���ؼ� ������ �� Ȯ��
			num = num + (5 * i);
			if (num % 3 == 0) {
				min = min - i + (num / 3);
				cout << min << '\n';
				return 0;
			}
		}
		cout << -1 << '\n'; // ���ص� ���� ���� ���
		return 0;
	}

	else { // 5�� �������� �� �������� 3���� ���� ���
		for (int i = 1; i <= (N / 5); i++) { // 5 ���� �� �ϳ��� �ٽ� ���ؼ� ������ �� Ȯ��
			num = (res % 3) + (5 * i);
			if (num % 3 == 0) {
				min = min - i + (num / 3);
				cout << min << '\n';
				return 0;
			}
		}
		cout << -1 << '\n'; // ���ص� ���� ���� ���
	}
	return 0;
}