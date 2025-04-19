#include <queue>
#include <iostream>
#include <string>
#include <unordered_map>
#include <cstdint>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;
using ull = uint64_t;

int main(void) {
    ull a = 873;
    ull b = 583;
    ull af = 16807;
    ull bf = 48271;
    ull d = 2147483647;
    ull finalCount = 0;
    for (ull i = 0; i < 40000000; ++i) {
        a *= af;
        a %= d;
        b *= bf;
        b %= d;
        ull ar = a & 0xFFFF;
        ull br = b & 0xFFFF;
        if (ar == br)
            finalCount += 1;
    }
    cout << "Judge's final count: " << finalCount << endl;

    return 0;
}