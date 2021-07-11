#include <iostream>
using namespace std;
int H,W;

int main(){
    cin >> H >> W;
    if((H==1) || (W==1)) cout << H*W << endl;
    else cout << int((H+1) / 2) * int((W+1)/2) << endl;
    return 0;
}
