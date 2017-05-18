#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int solution(int N)
{
	uint32_t i = 1;
	uint32_t N2(N);
	int factors = 0;
	while (i*i < N2) {
		if (N2%i == 0)
			factors += 2;
		i++;
	}
	if (i*i == N2) {
		factors++;
	}
	return factors;
}

int main(int argc, char **argv) {
	cout << solution(24) <<  endl;
	cout << solution(1000000000) <<  endl;
	cout << solution(2147395600) <<  endl;
	cout << solution(2147483647) <<  endl;
	return 0;
}