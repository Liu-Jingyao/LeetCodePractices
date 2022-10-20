#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
	int tempArr[1100] = {};
	vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
		int arr1Size = (int) nums1.size(), arr2Size = (int) nums2.size();
		mergeSort(nums1, arr1Size, 0, arr1Size - 1);
		mergeSort(nums2, arr2Size, 0, arr2Size - 1);
		int i = 0, j = 0;
		vector<int> resArr;
		while(i < arr1Size && j < arr2Size) {
			if(nums1[i] < nums2[j]) i++;
			else if(nums1[i] == nums2[j]) {
				if (i == 0 || nums1[i] != nums1[i-1]) resArr.push_back(nums1[i]);
				i++; j++;
			} else j++;
		}
		return resArr;
	}
	
	void mergeSort(vector<int>& arr, int arrSize, int l, int r) {
		if(l == r) return;
		
		int mid = (l + r) / 2;
		mergeSort(arr, arrSize, l, mid);
		mergeSort(arr, arrSize, mid + 1, r);
		
		int s1 = l, s2 = mid + 1, cnt = 0;
		while(s1 <= mid && s2 <= r){
			if(arr[s1] < arr[s2]) {
				tempArr[cnt++] = arr[s1++];
			} else {
				tempArr[cnt++] = arr[s2++];
			}
		}
		while(s1 <= mid) {
			tempArr[cnt++] = arr[s1++];
		}	
		while(s2 <= r) {
			tempArr[cnt++] = arr[s2++];
		}
		
		for(int i=0; i<cnt; i++) {
			arr[l + i] = tempArr[i];
		}
	}
};


int main() {
	Solution solution;
	vector arr1 = {4,9,5};
	vector arr2 = {9,4,9,8,4};
	vector res = solution.intersection(arr1, arr2);
	for(int i=0; i<(int)res.size(); i++) {
		cout << res[i] << " ";
	}
	return 0;
}
