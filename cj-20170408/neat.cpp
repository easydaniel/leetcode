#include <iostream>
#include <string>
using namespace std;

string solve(string n) {
  size_t sz = n.length();
  for (int i = sz - 1; i > 0; --i) {
    if (n[i] < n[i-1]) {
      for (int j = i; j < sz; ++j) {
        n[j] = '9';
      }
      n[i-1] -= 1;
      for (int j = i - 1; j > 0; --j) {
        if (n[j] < '0' || n[j] < n[j - 1]) {
          n[j] = '9';
          n[j-1] -= 1;
        }
      }
    }
  }
  string trim;
  bool lead = false;
  for (int i = 0; i < sz; ++i) {
    if (lead || n[i] != '0')
      trim += n[i];
    if ((!lead && n[i] == '0') || n[i] != '0')
      lead = true;
  }
  if (sz == 1)
    return n;
  return trim;
}
// 666611
// 678911
int main(int argc, char const *argv[]) {
  cin.tie(nullptr), ios_base::sync_with_stdio(false);
  int c;
  cin >> c;
  for (int i = 1; i <= c; ++i) {
    string n;
    cin >> n;
    cout << "Case #" << i << ": " << solve(n) << "\n";
  }
  return 0;
}
