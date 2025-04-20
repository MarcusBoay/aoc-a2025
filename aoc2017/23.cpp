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

    while (true) {
        f = 1; // 9
        d = 2; // 10
        while (g != 0) {
            e = 2; // 11
            while (g != 0) {
                g = d; // 12
                g *= e;
                g -= b;
                if (g == 0) {
                    f = 0;
                }
                e++;
                g = e;
                g -= b;
            }
            d++;
            g = d;
            g -= b;
        }
        if (f == 0) { // 27
            h--;
            cout << "h: " << h << endl;
        }
        g = b;
        g -= c;
        cout << "g: " << g << endl;
        if (g == 0) {
            // program termination
            cout << h << endl;
            return 0;
        }
        b += 17;
    }
    return 0;
}

void foo() {
    int a=0, b=0, c=0, d=0, e=0, f=0, g=0, h=0;
    b = 93;
    c = b;
    b *= 100;
    b += 100000;
    c = b;
    c += 17000;

    while (true) {
        f = 1; // 9
        d = 2; // 10
        while (g != 0) {
            e = 2; // 11
            while (g != 0) {
                // d*e - b
                g = d; // 12
                g *= e;
                g -= b;
                if (g == 0) {
                    f = 0;
                }
                // e+1-b
                e++;
                g = e;
                g -= b;
            }
            // d+1-b
            d++;
            g = d;
            g -= b;
        }
        if (f == 0) { // 27
            h++;
            cout << "h: " << h << endl;
        }
        g = b;
        g -= c;
        cout << "g: " << g << endl;
        if (g == 0) {
            // program termination
            cout << h << endl;
            return;
        }
        b += 17;
    }
    return;
}