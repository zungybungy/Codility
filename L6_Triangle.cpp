#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


bool is_triangle(int64_t a, int64_t b, int64_t c)
{
	return (a + b > c) &&
		(b + c > a) &&
		(c + a > b);
}

int solution(vector<int> &A) {
	// write your code in C++11 (g++ 4.8.2)
	if (A.size() < 3) return 0;

	sort(A.begin(), A.end());

	int res = 0;
	for (int i = 0; i < int(A.size() - 2); i++) {
		if (is_triangle(A[i], A[i + 1], A[i + 2])) return 1;
	}

	return 0;
}


int main(int argc, char **argv)
{
	vector<int> A;
	A.push_back(4);
	A.push_back(5);
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

