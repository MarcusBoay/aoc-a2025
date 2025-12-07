#include <vector>
#include <iostream>

using namespace std;

int main() {
    const int serialNumber = 4151;
    vector<vector<int>> grid;
    for (int y = 1; y < 301; y++) {
        vector<int> row;
        for (int x = 1; x < 301; x++) {
            row.push_back(0);
        }
        grid.push_back(std::move(row));
    }

    for (int y = 1; y < 301; y++) {
        for (int x = 1; x < 301; x++) {
            int rackID = x + 10;
            int powerLevel = rackID * y;
            powerLevel = powerLevel + serialNumber;
            powerLevel = powerLevel * rackID;
            powerLevel = (powerLevel / 100) % 10;
            powerLevel = powerLevel - 5;
            grid[y-1][x-1] = powerLevel;
        }
    }
    int maxPower = 0;
    int maxX=0, maxY=0, maxSize=0;
    // for (int s = 3; s < 4; s++) {
    for (int s = 1; s < 301; s++) {
        cout << "s: " << s << endl;
        for (int y = 0; y < 301-s; y++) {
            for (int x = 0; x < 301-s; x++) {
                int curPower = 0;
                for (int sy = y; sy < y+s; sy++) {
                    for (int sx = x; sx < x+s; sx++) {
                        curPower += grid[sy][sx];
                    }
                }
                if (curPower > maxPower) {
                    maxPower = curPower;
                    maxX = x+1;
                    maxY = y+1;
                    maxSize = s;
                }
            }
        }
    }
    cout << "Largest total power: " << maxPower << endl;
    cout << "Largest square: " << maxX << ", " << maxY << ", " << maxSize << endl;
    return 0;
}