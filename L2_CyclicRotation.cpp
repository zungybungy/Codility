#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static inline void swapElems(vector<int> &A, int start, int end)
{
	int tmp = 0;
	while (start < end)
	{
		tmp = A[start];
		A[start++] = A[end];
		A[end--] = tmp;
	}
}
vector<int> solutionCyclicRotation(vector<int> &A, int K)
{
	int len = A.size();
	if (0 == len || 0 == K)
		return A;
	K = K % len;
	swapElems(A, len - K, len - 1);
	swapElems(A, 0, len - K - 1);
	swapElems(A, 0, len - 1);
	return A;
}

vector<int> solution2(vector<int> &A, int K) {

	vector<int> arr;
	int N = A.size();
	if (N == 0)
		return arr;

	int remain = (N + K) % N;
	arr.resize(N);
	for (auto i : A)
	{
		arr[remain] = i;
		if (++remain >= N)
			remain = 0;
	}

	return arr;
}
int main(int argc, char **argv)
{
	vector<int> A;
	A.push_back(1);
	A.push_back(3);
	A.push_back(1);
	A.push_back(4);
	A.push_back(2);
	A.push_back(3);
	A.push_back(5);
	A.push_back(4);

	vector<int> S = solution2( A,3);
	for (vector<int>::iterator it = S.begin(); it != S.end(); it++) {
		cout << *it << " ";
	}
}

