#include <queue>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <cstdint>
#include <fstream>
#include <vector>
#include <algorithm>
#include <utility>
#include <sstream>

using namespace std;
using ull = uint64_t;

vector<vector<int>> p;
vector<vector<int>> v;
vector<vector<int>> a;

void getInput(string fileName) {
    string str = "";
    ifstream file(fileName);
    const char delimiter = ',';
    while (getline(file, str)) {
        stringstream ss(str);
        string t;
        vector<string> s = {};
        while (!ss.eof()) {
            getline(ss, t, delimiter);
            s.push_back(t);
        }
        vector<int> pi = {stoi(s[0]), stoi(s[1]), stoi(s[2])};
        vector<int> vi = {stoi(s[3]), stoi(s[4]), stoi(s[5])};
        vector<int> ai = {stoi(s[6]), stoi(s[7]), stoi(s[8])};
        p.push_back(std::move(pi));
        v.push_back(std::move(vi));
        a.push_back(std::move(ai));
    }
    file.close();
}

void part2(string fileName) {
    getInput(fileName);
    // s = ut + 0.5at^2
    int maxT = 10000;
    unordered_set<int> collided;
    for (int t = 0; t < maxT; ++t) {
        if (t % 1000 == 0) {
            cout << "Running tick " << t << " collisions so far: " << collided.size() << endl;
        }
        unordered_map<string, vector<int>> coords;
        for (int i = 0; i < p.size(); ++i) {
            if (!collided.contains(i)) {
                // ull sx = v[i][0]*t + a[i][0]*t*t/2 + p[i][0];
                // ull sy = v[i][1]*t + a[i][1]*t*t/2 + p[i][1];
                // ull sz = v[i][2]*t + a[i][2]*t*t/2 + p[i][2];
                v[i][0] += a[i][0];
                v[i][1] += a[i][1];
                v[i][2] += a[i][2];
                p[i][0] += v[i][0];
                p[i][1] += v[i][1];
                p[i][2] += v[i][2];
                string cs = to_string(p[i][0])+","+to_string(p[i][1])+","+to_string(p[i][2]);
                if (!coords.contains(cs)) {
                    coords.insert({cs, {}});
                }
                coords[cs].push_back(i);
            }
        }
        for (const auto &xyz : coords) {
            if (xyz.second.size() > 1) {
                for (const auto p : xyz.second) {
                    cout << "Particle " << p << " collided at tick " << t << "!" << endl;
                    collided.insert(p);
                }
            }
        }
    }
    cout << "Particles left after running for " << maxT << " ticks: " << p.size()-collided.size() << endl;
}

int main(void) {
    cout << "== 20.in ==" << endl;
    part2("20.in");
    return 0;
}