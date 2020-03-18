#include <iostream>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int greedy(vector<int> arr, int N, int X) {
    int sum = 0;
    int count = 0;
    sort(arr.begin(), arr.end());
    for (int i = 0; i < N; i++) {
        if (X < sum) {
            sum = sum + arr[i];
            if (X >= sum) break;
            count++;
        }
    }
    return count;
}

int main() {
    int T, input;
    scanf("%d", &T);
    long N, X;
    vector<int> arr;
    for (int i = 0; i < T; i++) {
        scanf("%ld %ld", &N, &X);
        for (int j = 0; j < N; j++) {
            cin >> input;
            arr.push_back(input);
        }
    }
    int count = greedy(arr, N, X);
    cout << count << "\n";
}

