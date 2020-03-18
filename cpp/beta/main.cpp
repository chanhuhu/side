#include <iostream>

struct values {
    int x;
    int y;
};

values func(int arr[], int k) {
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            int sum;
            sum = arr[i] + arr[j];
            if (sum == k) {
                values v = {arr[i], arr[j]};
                return v;
            }
            sum = 0;
        }
    }
}

int main() {
    int a[4] = {15, 15, 10, 7};
    int k = 17;
    values ans = func(a, k);
    std::cout << ans.x << " + " << ans.y << " = " << k << std::endl;
    return 0;
}
