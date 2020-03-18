#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    string x[4] = {"WOrld", "hELlo", "int", "AEIOU"};
    int a[4] = {1, 2, 3, 4};
    int n = sizeof(a) / sizeof(a[0]);
    for (const string& i : x) {
        cout << i << " ";
    }
    cout << "\n**********************" << endl;
    cout << *max_element(a, a + n);
    return 0;
}