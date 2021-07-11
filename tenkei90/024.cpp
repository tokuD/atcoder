#include <iostream>
#include <cmath>
using namespace std;

long long N,K;
long long A[1 << 18], B[1 << 18];

int main(){
    //input
    cin >> N >> K;
    for(int i=1;i<=N;i++) cin >> A[i];
    for(int i=1;i<=N;i++) cin >> B[i];

    //check difference
    long long dif = 0;
    for(int i=1;i<=N;i++) dif += abs(A[i]-B[i]);

    if(dif>K){
        cout << "No" << endl;
        return 0;
    }

    if((K-dif)%2 != 0){
        cout << "No" << endl;
        return 0;
    }

    cout << "Yes" << endl;
    return 0;
}
