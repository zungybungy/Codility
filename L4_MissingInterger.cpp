#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;



#include <unordered_map>

int solution(vector<int> &A) {
	// write your code in C++11 (g++ 4.8.2)
	unordered_map<int, int> map;

	for (int i = 0; i < int(A.size()); i++) {
		if (A[i] > 0) {
			map[A[i]] = i;
		}
	}

	for (int i = 1; i < int(map.size() + 1); i++) {
		if (map.find(i) == map.end()) return i;
	}

	return int(map.size() + 1);
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
	A.push_back(7);

	cout << solution(A) << " ";
	/*

	vector<int> S = solution(A);
	for (vector<int>::iterator it = S.begin(); it != S.end(); it++) {
		cout << *it << " ";
	}*/
}

