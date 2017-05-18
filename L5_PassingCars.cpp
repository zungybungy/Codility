#include <iostream>
#include <vector>
using namespace std;


int solution(vector<int> &A) {
	// write your code in C++11 (g++ 4.8.2)
	vector<int> pre_sum(A.size(), 0);

	int s = 0;
	for (size_t i = 0; i < A.size(); i++) {
		s += A[i];
		pre_sum[i] = s;
	}

	int res = 0;

	for (int i = int(A.size() - 1); i >= 0; i--) {
		if (A[i] == 0) {
			res += (pre_sum[A.size() - 1] - pre_sum[i]);
			if (res > 1000000000) return -1;
		}
	}

	return res;
}

int main(int argc, char **argv)
{
	vector<int> A;
	A.push_back(0);
	A.push_back(1);
	A.push_back(1);
	A.push_back(0);
	A.push_back(0);
	A.push_back(1);

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

