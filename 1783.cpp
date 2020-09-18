#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;

int main()
{
	int N, M;
	cin >> N >> M;

	int max = 1;
	int share = (N - 3) / 2;
	int res = (N - 3) % 2;

	max += share;

	if (N < 3 && M < 7) { // 이동 횟수가 4번이 안될 때
		if (N == 1 || M == 1) {
			cout << 1 << '\n';
			return 0;
		}
		if (M == 4) {
			cout << 2 << '\n';
		}
		else {
			cout << 3 << '\n';
		}
		return 0;
	}
	else if (N == 2) {
		if (M <= 2 )
			cout << 1 << '\n';
		else if (M <= 4)
			cout << 2 << '\n';
		else if (M <= 6)
			cout << 3 << '\n';
		else if (M <= 8) 
			cout << 4 << '\n';
		else 
			cout << 3 << '\n';
		return 0;
	}
	else if (M < 5) {
		cout << M << '\n';
		return 0;
	}
	else if (M >= 5 && M <= 6) {
		cout << 4 << '\n';
		return 0;
	}

	else if (res == 0) { // 나머지가 없을 때
		M -= (share + 1 + 2);
		max += M + 1;
		cout << max << '\n';
		return 0;
	}
	else { // 나머지가 있을 때
		share++;
		M -= (1 + share);
		if (M >= 5)
		{
			max += (M - 3);
			cout << max << '\n';
			return 0;
		}
		else {
			for (int i = 1; i <= share; i++) {
				M++;
				if (M == 5) {
					share -= i;
					max = (share + 3) + 1;
					cout << max << '\n';
					break;
				}
			}			
		}		

	}
	return 0;
}