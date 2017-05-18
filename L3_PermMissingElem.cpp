#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> &A) {
	// write your code in C++11 (g++ 4.8.2)
	int res = 0;

	for (int i = 0; i < int(A.size()); i++) {
		res += (i + 1 - A[i]);
	}

	res += int(A.size() + 1);

	return res;
}

int main(int argc, char **argv)
{
	vector<int> A;
	A.push_back(2);
	A.push_back(3);
	A.push_back(1);
	A.push_back(5);

	cout << solution(A) << " ";
	/*
	vector<int> S = solution(A);
	for (vector<int>::iterator it = S.begin(); it != S.end(); it++) {
		cout << *it << " ";
	}*/
}

