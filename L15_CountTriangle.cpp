#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

int solution(vector<int> &A) {
	int N(A.size());
	if (N < 3)
		return 0;
	std::sort(A.begin(), A.end());
	int count(0), P(0), Q(0);
	for (int R = N - 1; R > 1; --R)
	{
		P = 0;
		Q = R - 1;
		while ((P < Q))
		{
			while ((P < Q) && (A[P] + A[Q] <= A[R]))
				++P;
			count += Q - P;
			--Q;
		}
	}
	return count;
}

int main(int argc, char **argv)
{
	vector<int> A;
	A.push_back(4);
	A.push_back(5);
	A.push_back(6);
	A.push_back(7);
	A.push_back(1);
	A.push_back(10);
	
	std::cout << solution(A) << " ";
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