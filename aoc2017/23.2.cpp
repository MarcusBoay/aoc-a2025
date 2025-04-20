#include <iostream>

using namespace std;

int main() {
    int a=0, b=0, c=0, d=0, e=0, f=0, g=0, h=0;
    b = 93;
    c = b;
    b *= 100;
    b += 100000;
    c = b;
    c += 17000;
    // int nh = 0;

    while (true) {
        f = 1;
        d = 2;
        for (int di = 2; di < b-1; di++) {
            for (int ei = 2; ei < b-1; ei++) {
                if (di*ei == b) {
                    f = 0;
                    break;
                }
                if (di*ei > b) {
                    break;
                }
            }
            if (f == 0)
                break;
        }
        if (f == 0) { // 27
            h++;
            cout << "h: " << h << endl;
        }
        if (b == c) {
            // program termination
            cout << h << endl;
            return 0;
        }
        b += 17;
    }
    return 0;
}