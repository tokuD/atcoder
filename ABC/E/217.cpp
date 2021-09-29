#include <iostream>

int main(){
    using namespace std;
    int Q;
    cin >> Q;
    int query[Q];
    for(int i=0;i<Q;i++){
        cin >> query[i];
    }
    for(int i=0;i<Q;i++){
        cout << query[i] << endl;
    }
}
