#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;



int solution(vector<int> &A) {
	// the use of a auto_ptr would be better, but it does not work with arrays
	// use of boost::scoped_array seems like an overkill
	bool * seen = new bool[A.size()];

	for (unsigned int i = 0; i< A.size(); i++) {
		seen[i] = false;
	}

	for (unsigned int i = 0; i< A.size(); i++) {
		if (!(0 < A[i] && A[i] <= A.size() && seen[A[i] - 1] == false)) {
			delete[] seen;
			return 0;
		}
		else {
			seen[A[i] - 1] = true;
		}
	}

	delete[] seen;
	return 1;
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

