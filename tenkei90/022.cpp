#include <iostream>
#include <math.h>
using namespace std;

// long long A,B,C,warareru,waru,amari;

// int main(){
//     cin >> A >> B >> C;
//     warareru = max(A,B);
//     waru = min(A,B);
//     while(true){
//         amari = warareru % waru;
//         if(amari==0){
//             break;
//         }
//         warareru = waru;
//         waru = amari;
//     }
//     warareru = max(waru,C);
//     waru = min(waru,C);
//     while(true){
//         amari = warareru % waru;
//         if(amari==0){
//             break;
//         }
//         warareru = waru;
//         waru = amari;
//     }
//     cout << A/waru + B/waru + C/waru - 3 << endl;
//     return 0;
// }


//!-----------------------------
long long gcd(long long a, long long b){
    if(b==0)return a;
    return gcd(b, a % b);
}

long long A,B,C;

int main(){
    cin >> A >> B >> C;
    long long s = gcd(A,gcd(B,C));
    cout << A/s + B/s + C/s - 3 << endl;
    return 0;
}
