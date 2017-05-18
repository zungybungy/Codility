#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int X, int Y, int D) {
	// write your code in C++11 (g++ 4.8.2)
	return (Y - X + (D - 1)) / D;
}

int main(int argc, char **argv)
{


	cout << solution(10,85,30) << " ";
	/*
	vector<int> A;
	A.push_back(2);
	A.push_back(3);
	A.push_back(1);
	A.push_back(5);
	vector<int> S = solution(A);
	for (vector<int>::iterator it = S.begin(); it != S.end(); it++) {
		cout << *it << " ";
	}*/
}

