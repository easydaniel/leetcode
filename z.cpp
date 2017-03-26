#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> zFunction(const string &s) {
  size_t len = s.length();
  int L = 0, R = 0;
  vector<int> zfunc;
  zfunc.push_back(0);
  for (int i = 1; i < len; ++i) {
    zfunc.push_back(0);
    if (i < R) {
      if (i + zfunc[i - L] < R) {
        zfunc[i] = zfunc[i - L];
      } else {
        zfunc[i] = R - i;
      }
    }
    while (i + zfunc[i] < len and s[i + zfunc[i]] == s[zfunc[i]]) {
      zfunc[i]++;
    }
    if (i + zfunc[i] > R) {
      L = i;
      R = i + zfunc[i];
    }
  }
  return zfunc;
}

int main(int argc, char const *argv[]) {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  string str, pattern;

  while (cin >> str >> pattern) {
    cout << pattern << '#' << str << '\n';
    for (auto i : zFunction(pattern + '#' + str)) {
      cout << i << '\n';
    }
  }
  return 0;
}
