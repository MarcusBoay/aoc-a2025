#include <queue>
#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int main(void) {
    short in = 70;
    string elements[93] = {
        "0", // N/A
        "22", // 1
        "13112221133211322112211213322112", // 2
        "312211322212221121123222112", // 3
        "111312211312113221133211322112211213322112", // 4
        "1321132122211322212221121123222112", // 5
        "3113112211322112211213322112", // 6
        "111312212221121123222112", // 7
        "132112211213322112", // 8
        "31121123222112", // 9
        "111213322112", // 10
        "123222112", // 11
        "3113322112", // 12
        "1113222112", // 13
        "1322112", // 14
        "311311222112", // 15
        "1113122112", // 16
        "132112", // 17
        "3112", // 18
        "1112", // 19
        "12", // 20
        "3113112221133112", // 21
        "11131221131112", // 22
        "13211312", // 23
        "31132", // 24
        "111311222112", // 25
        "13122112", // 26
        "32112", // 27
        "11133112", // 28
        "131112", // 29
        "312", // 30
        "13221133122211332", // 31
        "31131122211311122113222", // 32
        "11131221131211322113322112", // 33
        "13211321222113222112", // 34
        "3113112211322112", // 35
        "11131221222112", // 36
        "1321122112", // 37
        "3112112", // 38
        "1112133", // 39
        "12322211331222113112211", // 40
        "1113122113322113111221131221", // 41
        "13211322211312113211", // 42
        "311322113212221", // 43
        "132211331222113112211", // 44
        "311311222113111221131221", // 45
        "111312211312113211", // 46
        "132113212221", // 47
        "3113112211", // 48
        "11131221", // 49
        "13211", // 50
        "3112221", // 51
        "1322113312211", // 52
        "311311222113111221", // 53
        "11131221131211", // 54
        "13211321", // 55
        "311311", // 56
        "11131", // 57
        "1321133112", // 58
        "31131112", //59
        "111312", // 60
        "132", // 61
        "311332", // 62
        "1113222", // 63
        "13221133112", // 64
        "3113112221131112", // 65
        "111312211312", // 66
        "1321132", // 67
        "311311222", // 68
        "11131221133112", // 69
        "1321131112", // 70
        "311312", // 71
        "11132", // 72
        "13112221133211322112211213322113", // 73
        "312211322212221121123222113", // 74
        "111312211312113221133211322112211213322113", // 75
        "1321132122211322212221121123222113", // 76
        "3113112211322112211213322113", // 77
        "111312212221121123222113", // 78
        "132112211213322113", // 79
        "31121123222113", // 80
        "111213322113", // 81
        "123222113", // 82
        "3113322113", // 83
        "1113222113", // 84
        "1322113", // 85
        "311311222113", // 86
        "1113122113", // 87
        "132113", // 88
        "3113", // 89
        "1113", // 90
        "13", // 91
        "3", // 92
    };
    unordered_map<short, vector<short>> decaysInto = {};
    decaysInto.insert({1, {1}});
    decaysInto.insert({2, {72,91,1,20,3}});
    decaysInto.insert({3, {2}});
    decaysInto.insert({4, {32,20,3}});
    decaysInto.insert({5, {4}});
    decaysInto.insert({6, {5}});
    decaysInto.insert({7, {6}});
    decaysInto.insert({8, {7}});
    decaysInto.insert({9, {8}});
    decaysInto.insert({10, {9}});
    decaysInto.insert({11, {10}});
    decaysInto.insert({12, {61,11}});
    decaysInto.insert({13, {12}});
    decaysInto.insert({14, {13}});
    decaysInto.insert({15, {67,14}});
    decaysInto.insert({16, {15}});
    decaysInto.insert({17, {16}});
    decaysInto.insert({18, {17}});
    decaysInto.insert({19, {18}});
    decaysInto.insert({20, {19}});
    decaysInto.insert({21, {67,91,1,20,27}});
    decaysInto.insert({22, {21}});
    decaysInto.insert({23, {22}});
    decaysInto.insert({24, {23}});
    decaysInto.insert({25, {24,14}});
    decaysInto.insert({26, {25}});
    decaysInto.insert({27, {26}});
    decaysInto.insert({28, {30,27}});
    decaysInto.insert({29, {28}});
    decaysInto.insert({30, {29}});
    decaysInto.insert({31, {63,20,89,1,20,30}});
    decaysInto.insert({32, {67,31}});
    decaysInto.insert({33, {32,11}});
    decaysInto.insert({34, {33}});
    decaysInto.insert({35, {34}});
    decaysInto.insert({36, {35}});
    decaysInto.insert({37, {36}});
    decaysInto.insert({38, {37}});
    decaysInto.insert({39, {38,92}});
    decaysInto.insert({40, {39,1,20,43}});
    decaysInto.insert({41, {68,40}});
    decaysInto.insert({42, {41}});
    decaysInto.insert({43, {42}});
    decaysInto.insert({44, {63,20,43}});
    decaysInto.insert({45, {67,44}});
    decaysInto.insert({46, {45}});
    decaysInto.insert({47, {46}});
    decaysInto.insert({48, {47}});
    decaysInto.insert({49, {48}});
    decaysInto.insert({50, {49}});
    decaysInto.insert({51, {61,50}});
    decaysInto.insert({52, {63,20,51}});
    decaysInto.insert({53, {67,52}});
    decaysInto.insert({54, {53}});
    decaysInto.insert({55, {54}});
    decaysInto.insert({56, {55}});
    decaysInto.insert({57, {56}});
    decaysInto.insert({58, {57,1,20,27}});
    decaysInto.insert({59, {58}});
    decaysInto.insert({60, {59}});
    decaysInto.insert({61, {60}});
    decaysInto.insert({62, {61,20,30}});
    decaysInto.insert({63, {62}});
    decaysInto.insert({64, {63,20,27}});
    decaysInto.insert({65, {67,64}});
    decaysInto.insert({66, {65}});
    decaysInto.insert({67, {66}});
    decaysInto.insert({68, {67,61}});
    decaysInto.insert({69, {68,20,27}});
    decaysInto.insert({70, {69}});
    decaysInto.insert({71, {70}});
    decaysInto.insert({72, {71}});
    decaysInto.insert({73, {72,91,1,20,74}});
    decaysInto.insert({74, {73}});
    decaysInto.insert({75, {32,20,74}});
    decaysInto.insert({76, {75}});
    decaysInto.insert({77, {76}});
    decaysInto.insert({78, {77}});
    decaysInto.insert({79, {78}});
    decaysInto.insert({80, {79}});
    decaysInto.insert({81, {80}});
    decaysInto.insert({82, {81}});
    decaysInto.insert({83, {61,82}});
    decaysInto.insert({84, {83}});
    decaysInto.insert({85, {84}});
    decaysInto.insert({86, {67,85}});
    decaysInto.insert({87, {86}});
    decaysInto.insert({88, {87}});
    decaysInto.insert({89, {88}});
    decaysInto.insert({90, {89}});
    decaysInto.insert({91, {90}});
    decaysInto.insert({92, {91}});

    queue<short> q;
    q.push(in);
    short i = 0;
    short n = 75;
    while (i < n) {
        i++;
        unsigned long long qn = q.size();
        if (i > 40) {
            cout << "iteration " << i << endl;
        }
        while (qn > 0) {
            auto cur = q.front();
            q.pop();
            qn--;
            for (auto d : decaysInto[cur]) {
                q.push(d);
            }
        }
    }
    unsigned long long totalLength = 0;
    for (; !q.empty(); q.pop()) {
        totalLength += elements[q.front()].size();
    }
    cout << totalLength << endl;

    return 0;
}