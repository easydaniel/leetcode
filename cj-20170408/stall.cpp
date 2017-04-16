#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

void solve(long long n, long long k) {
  long long l = 1, ac = 1;

  while (l < k) {
    k -= l;
    if (n & 1) {
      ac += l;
    }
    n >>= 1;
    l <<= 1;
  }
  if (k > ac) {
    n--;
  }
  cout << (n / 2) << " " << (n - n/2 - 1) << endl;
}

int main(int argc, char const *argv[]) {
  cin.tie(nullptr), ios_base::sync_with_stdio(false);
  int c;
  cin >> c;
  for (int i = 1; i <= c; ++i) {
    long long n, k;
    cin >> n >> k;
    cout << "Case #" << i << ": ";
    solve(n, k);
  }
  return 0;
}
