#include <string>
#include <iostream>
#include <cstdint>
#include <vector>

using namespace std;
using vull = vector<uint64_t>;

int main() {
    uint64_t goal = 34000000;

    uint64_t l = 700000;
    uint64_t r = 1519039;

    while (l <= r) {
        uint64_t n = 0;
        for (int i = 1; i <= l; ++i)
            if (l % i == 0)
                n += i;
        if (n >= (goal/10)) {
            cout << l << endl;
            return 0;
        }
        ++l;
    }

    cout << "COULD NOT FIND" << endl;
    return 0;
}