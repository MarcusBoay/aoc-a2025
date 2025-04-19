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

vector<vector<string>> getInstructions(string fileName) {
    string s;
    ifstream file(fileName);
    getline(file, s);
    file.close();

    vector<vector<string>> instructions = {};
    const string delimiter = ",";
    while (s.size() > 0) {
        // cout << s.size() << endl;
        string instr = s.substr(0, s.find(delimiter));
        s.erase(0, s.find(delimiter) + delimiter.length());
        if (s.size() == instr.size()) {
            s = "";
        }

        vector<string> currentInstr = {};
        string cur(1, instr[0]);
        currentInstr.push_back(cur);
        if (instr[0] == 's') {
            string sn = instr.substr(1);
            currentInstr.push_back(sn);
        } else if (instr[0] == 'x') {
            string xInstr = instr.substr(1);
            string pDelim = "/";
            string pi1 = xInstr.substr(0, xInstr.find(pDelim));
            string pi2 = xInstr.substr(xInstr.find(pDelim)+pDelim.length());
            currentInstr.push_back(pi1);
            currentInstr.push_back(pi2);
        } else if (instr[0] == 'p') {
            string pInstr = instr.substr(1);
            string p1(1, pInstr[0]);
            string p2(1, pInstr[2]);
            currentInstr.push_back(p1);
            currentInstr.push_back(p2);
        }
        instructions.push_back(currentInstr);
    }
    return instructions;
}

void part2(string fileName) {
    vector<vector<string>> instrs = getInstructions(fileName);
    // vector<char> programs = {
    //         'a',
    //         'b',
    //         'c',
    //         'd',
    //         'e',
    // };
    vector<char> programs = {
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'h',
        'i',
        'j',
        'k',
        'l',
        'm',
        'n',
        'o',
        'p'
    };
    for (ull ite = 0; ite < 1000000000; ++ite) {
        // cout << "iteration " << ite << endl;
        for (const auto &p : programs) {
            cout << p;
        }
        cout << endl;
        // if (ite % 1000 == 0)
        //     cout << "iteration " << ite << endl;
        if (ite >= 1000) {
            return;
        }

        for (const auto &instr : instrs) {
            if (instr[0] == "s") {
                int sn = stoi(instr[1]);
                while (sn--) {
                    auto b = programs.back();
                    programs.pop_back();
                    programs.insert(programs.begin(), b);
                }
            } else if (instr[0] == "x") {
                int pi1 = stoi(instr[1]);
                int pi2 = stoi(instr[2]);
                char p1 = programs[pi1];
                char p2 = programs[pi2];
                programs[pi1] = p2;
                programs[pi2] = p1;
            } else if (instr[0] == "p") {
                int pi1 = 0;
                int pi2 = 0;
                for (int i = 0; i < programs.size(); ++i) {
                    if (programs[i] == *instr[1].c_str()) {
                        pi1 = i;
                    } else if (programs[i] == *instr[2].c_str()) {
                        pi2 = i;
                    }
                }
                programs[pi1] = *instr[2].c_str();
                programs[pi2] = *instr[1].c_str();
            }
        }
    }
    cout << "Order of programs: ";
    for (const auto &p : programs) {
        cout << p;
    }
    cout << endl;
    // print(f"Order of programs: {"".join(programs)}")
}

int main(void) {
    // cout << "== 16.ex.in ==" << endl;
    // part2("16.ex.in");
    cout << "== 16.in ==" << endl;
    part2("16.in");
    return 0;
}