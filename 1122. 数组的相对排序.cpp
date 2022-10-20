#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
	vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
		int countArr[1100] = {};
		int excludeArr[1100] = {};
		int excludeArrSize = 0;
		vector<int> resArr;
		
		for(int i=0; i<(int)arr1.size(); i++) {
			bool belongArr2 = false;
			for(int j=0; j<(int)arr2.size(); j++) {
				if(arr1[i] == arr2[j]) {
					belongArr2 = true;
					countArr[j] ++;
					break;
				}
			}
			if(!belongArr2) {
				excludeArr[excludeArrSize++] = arr1[i];
			}
		}
		quickSort(excludeArr, excludeArrSize, 0, excludeArrSize-1);
		
		for(int i=0; i<(int)arr2.size(); i++) {
			for(int j=0; j<countArr[i]; j++) {
				resArr.push_back(arr2[i]);
			}
		}
		for(int i=0; i<excludeArrSize; i++) {
			resArr.push_back(excludeArr[i]);
		}
		
		return resArr;
	}
	
	void quickSort(int arr[], int arrSize, int l, int r) {
		if(l >= r) {
			return;
		}
		
		int p = arr[l];
		// Partition
		int i = l, j = r;
		while(i < j) {
			while(i < j && arr[j] >= p) --j;
			arr[i] = arr[j];
			while(i < j && arr[i] <= p) ++i;
			arr[j] = arr[i];
		}
		arr[i] = p;
		
		quickSort(arr, arrSize, l, i-1);
		quickSort(arr, arrSize, i+1, r);
	}
};


int main() {
	Solution solution;
	vector arr1 = {2,3,1,3,2,4,6,7,9,2,19};
	vector arr2 = {2,1,4,3,9,6};
	vector res = solution.relativeSortArray(arr1, arr2);
	for(int i=0; i<(int)res.size(); i++) {
		cout << res[i] << " ";
	}
}
