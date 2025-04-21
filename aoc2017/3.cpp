#include <iostream>
#include <vector>
#include <utility>

using namespace std;

int main() {
    vector<vector<int>> grid;
    int L = 610;
    int input = 368078;
    for (int i = 0; i < L; i++) {
        vector<int> row = {};
        for (int j = 0; j < L; j++) {
            row.push_back(0);
        }
        grid.push_back(std::move(row));
    }

    int i = 305;
    int j = 305;
    grid[i][j] = 1;
    int l = 3;
    while (true) {
        // step into next circle
        j++;
        cout << "l: " << l << endl;
        // step up the right side
        int steps = l-1;
        cout << i << " " << j << endl;
        do {
            grid[i][j] = grid[i+1][j] + grid[i-1][j] +
                         grid[i][j+1] + grid[i][j-1] +
                         grid[i+1][j+1] + grid[i+1][j-1] +
                         grid[i-1][j+1] + grid[i-1][j-1];
            if (grid[i][j] > input) {
                cout << "found: " << grid[i][j] << " at " << i << " " << j << endl;
                return 0;
            }
            i--;
            steps--;
        } while (steps);
        i++;
        // step to the left of the upper side
        steps = l;
        cout << i << " " << j << endl;
        do {
            grid[i][j] = grid[i+1][j] + grid[i-1][j] +
                         grid[i][j+1] + grid[i][j-1] +
                         grid[i+1][j+1] + grid[i+1][j-1] +
                         grid[i-1][j+1] + grid[i-1][j-1];
            if (grid[i][j] > input) {
                cout << "found: " << grid[i][j] << " at " << i << " " << j << endl;
                return 0;
            }
            j--;
            steps--;
        } while (steps);
        j++;
        // step down the left side
        steps = l;
        cout << i << " " << j << endl;
        do {
            grid[i][j] = grid[i+1][j] + grid[i-1][j] +
                         grid[i][j+1] + grid[i][j-1] +
                         grid[i+1][j+1] + grid[i+1][j-1] +
                         grid[i-1][j+1] + grid[i-1][j-1];
            if (grid[i][j] > input) {
                cout << "found: " << grid[i][j] << " at " << i << " " << j << endl;
                return 0;
            }
            i++;
            steps--;
        } while (steps);
        i--;
        // step to the right of the bottom side
        steps = l;
        cout << i << " " << j << endl;
        do {
            grid[i][j] = grid[i+1][j] + grid[i-1][j] +
                         grid[i][j+1] + grid[i][j-1] +
                         grid[i+1][j+1] + grid[i+1][j-1] +
                         grid[i-1][j+1] + grid[i-1][j-1];
            if (grid[i][j] > input) {
                cout << "found: " << grid[i][j] << " at " << i << " " << j << endl;
                return 0;
            }
            j++;
            steps--;
        } while (steps);
        j--;

        l += 2;
    }

    return 0;
}