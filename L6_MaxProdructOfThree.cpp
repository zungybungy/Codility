#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int solution(vector<int> &A) {
	// write your code in C++11 (g++ 4.8.2)
	sort(A.begin(), A.end());

	int s = int(A.size());

	int m1 = A[s - 1] * A[s - 2] * A[s - 3];
	if ((A[s - 1] < 0) || (A[0] > 0)) return m1;

	int m2 = A[0] * A[1] * A[s - 1];

	return max(m1, m2);
}


int main(int argc, char **argv)
{
	vector<int> A;
	A.push_back(4);
	A.push_back(5);
	A.push_back(6);
	A.push_back(4);
	A.push_back(-9);
	A.push_back(6);

	cout << solution(A) << " ";
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

