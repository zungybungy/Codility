#include <iostream>
#include <vector>
using namespace std;


int solution(int A, int B, int K) {
	// write your code in C++11 (g++ 4.8.2)
	if (A % K != 0) A = (A / K + 1) * K;

	if (B < A) return 0;

	return (B - A) / K + 1;
}

int main(int argc, char **argv)
{
	cout << solution(2,100,2) << " ";
	/*
	vector<int> A;
	A.push_back(1);
	A.push_back(3);
	A.push_back(1);
	A.push_back(4);
	A.push_back(2);
	A.push_back(3);
	A.push_back(5);
	A.push_back(7);

	vector<int> S = solution(A);
	for (vector<int>::iterator it = S.begin(); it != S.end(); it++) {
		cout << *it << " ";
	}*/
}

