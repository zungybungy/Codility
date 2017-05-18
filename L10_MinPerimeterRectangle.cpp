#include <iostream>
#include <algorithm>

using namespace std;

int solution(int N) {
	// write your code in C++11 (g++ 4.8.2)
	int i = 1;

	int A = 1;
	while (i * i < N) {
		if (N % i == 0) {
			A = i;
		}
		i++;
	}

	if (i * i == N) {
		A = i;
	}

	return (A + (N / A)) * 2;
}

int main(int argc, char **argv) {
	cout << solution(30) << endl;
	cout << solution(1000000000) << endl;
	return 0;
}