#include <iostream>
#include <vector>
using namespace std;


#include <set>
int solution(const vector<int> &A) {
	std::set<int> theSet;

	for (int idx = 0; idx < A.size(); idx++) {
		theSet.insert(A[idx]);
	}

	return theSet.size();
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

