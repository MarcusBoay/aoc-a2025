#include <string>
#include <iostream>
#include <cstdint>
#include <vector>
#include <unordered_map>

using namespace std;
using vull = vector<uint64_t>;

int main() {
    uint64_t goal = 34000000;

    uint64_t l = 1;
    uint64_t r = goal;

    unordered_map<uint64_t, uint64_t> numbers = {};
    uint64_t lowestHouseNumber = goal;

    uint64_t end = 4000000;
    for (uint64_t i = l; i < r; ++i) {
        cout << "Current elf: " << i << endl;
        for (uint64_t j = i; j <= i*50; j += i) {
            if (!numbers.contains(j)) {
                numbers[j] = 0;
            }
            numbers[j] += i;
            if (numbers[j]*11 >= goal) {
                // cout << "Lowest house number: " << j << endl;
                lowestHouseNumber = min(lowestHouseNumber, j);
            }
        }
        // for (auto h : numbers) {
        //     cout << "h: " << h.first << "=" << h.second << endl;
        // }
        // return 1;
        numbers.erase(i);
        if (i == end) {
            break;
        }
    }



    // while (l <= r) {
    //     uint64_t n = 0;
    //     for (int i = 1; i <= l; ++i)
    //         if (l % i == 0)
    //             n += i;
    //     if (n >= (goal/10)) {
    //         cout << l << endl;
    //         return 0;
    //     }
    //     ++l;
    // }

    cout << "Lowest house number: " << lowestHouseNumber << endl;
    return 0;
}