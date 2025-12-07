#include <bitset>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    // constexpr const int l = 20;
    // bitset<l> a;
    // a[l-0-1] = 1;
    // int curL = 5;

    // constexpr const int l = 272;
    constexpr const int l = 35651584;
    bitset<l> a;
    a[l-1-0] = 1;
    a[l-1-1] = 1;
    a[l-1-2] = 1;
    a[l-1-3] = 0;
    a[l-1-4] = 0;
    a[l-1-5] = 0;
    a[l-1-6] = 1;
    a[l-1-7] = 0;
    a[l-1-8] = 1;
    a[l-1-9] = 1;
    a[l-1-10] = 1;
    a[l-1-11] = 1;
    a[l-1-12] = 1;
    a[l-1-13] = 0;
    a[l-1-14] = 1;
    a[l-1-15] = 0;
    a[l-1-16] = 0;
    int curL = 17;

    while (curL < l) {
        a[l-1-curL] = 0;
        for (int li = 0; li < curL; li++) {
            if (l-1-(curL+li+1) < 0)
                break;
            a[l-1-(curL+li+1)] = ~a[l-1-(curL-li-1)];
        }
        curL += curL+1;
    }

    int n = l;
    while (n % 2 == 0) {
        for (int i = 0; i < n/2; i++) {
            a[i] = a[2*i] == a[2*i+1];
        }
        n = (n/2) + (n%2);
    }

    cout << "Correct checksum for disk of length " << l << ": ";
    for (int i = n-1; i >= 0; i--) {
        cout << a[i];
    }
    cout << endl;

    return 0;
}