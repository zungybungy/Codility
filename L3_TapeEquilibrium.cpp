#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>
using namespace std;



int solution(vector<int> &A) {
	// write your code in C++11 (g++ 4.8.2)
	vector<int> pre_sum;
	int s = 0;
	for (auto i : A) {
		s += i;
		pre_sum.push_back(s);
	}

	int min_abs_diff = numeric_limits<int>::max();
	for (size_t i = 1; i < pre_sum.size(); i++) {
		int abs_diff = abs(pre_sum[i - 1] * 2 - pre_sum[pre_sum.size() - 1]);
		min_abs_diff = min(min_abs_diff, abs_diff);
	}

	return min_abs_diff;
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

