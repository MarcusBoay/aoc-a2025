#include <iostream>

using namespace std;


int main() {
    int a=12, b=0, c=0, d=0;

    b = a;
    do {
        b--;
        d = a;
        a = 0;
        // a = b*d; ??
        // c = 0;
        // d = 0;
        do {
            c = b;
            do {
                a++;
                c--;
            } while (c != 0);
            d--;
        } while (d != 0);
        b--;
        c = b;
        d = c; // this toggles between cpy and jnz...
        // c = 2*b; ???
        do {
            d--;
            c++;
        } while (d != 0);
        // tgl c
        c = -16;
    } while (1 != 0); // jnz 1 c // ... this always jump back 16 steps???
    c = 79;
    // jnz 74 d // ????????
    a++;
    d++;
    // jnz d -2
    c++;
    // jnz c -5

    return 0;
}