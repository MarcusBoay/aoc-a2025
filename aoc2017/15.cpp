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

void part1(ull a, ull b) {
    cout << "--- Part 1 ---" << endl;
    constexpr const ull af = 16807;
    constexpr const ull bf = 48271;
    constexpr const ull d = 2147483647;
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
}

void part2(ull a, ull b) {
    cout << "--- Part 2 ---" << endl;
    constexpr const ull af = 16807;
    constexpr const ull bf = 48271;
    constexpr const ull d = 2147483647;
    ull finalCount = 0;
    for (ull i = 0; i < 5000000; ++i) {
        do {
            a *= af;
            a %= d;
        } while (a % 4 > 0);
        do {
            b *= bf;
            b %= d;
        } while (b % 8 > 0);
        ull ar = a & 0xFFFF;
        ull br = b & 0xFFFF;
        if (ar == br)
            finalCount += 1;
    }
    cout << "Judge's final count: " << finalCount << endl;
}

int main(void) {
    cout << "== 15.ex.in ==" << endl;
    part1(65,8921);
    part2(65,8921);
    cout << "== 15.in ==" << endl;
    part1(873,583);
    part2(873,583);
    return 0;
}