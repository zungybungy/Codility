#include <iostream>
#include <vector>
#include <set>
using namespace std;



int solution(int X, vector<int> &A) {
	// write your code in C++11 (g++ 4.8.2)
	set<int> s;
	for (size_t i = 0; i < A.size(); i++) {
		s.insert(A[i]);
		if (s.size() == X) return i;
	}

	return -1;
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

	cout << solution(5,A) << " ";
	/*

	vector<int> S = solution(A);
	for (vector<int>::iterator it = S.begin(); it != S.end(); it++) {
		cout << *it << " ";
	}*/
}

