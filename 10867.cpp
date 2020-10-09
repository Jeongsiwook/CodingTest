#include <iostream>
using namespace std;

int main()
{
	int N, i ,j, temp;
	cin >> N;

	int* arr = new int[N];

	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}

	// »ğÀÔÁ¤·Ä
	for (i = 0; i < N - 1; i++) {
		j = i;
		while (j >= 0 && arr[j] > arr[j + 1]) {
			temp = arr[j];
			arr[j] = arr[j + 1];
			arr[j + 1] = temp;
			j--;
		}		
	}

	for (i = 0; i < N; i++) {
		while (arr[i] == arr[i+1]) {
			i++;
			continue;
		}
		cout << arr[i] << " ";
	}
}