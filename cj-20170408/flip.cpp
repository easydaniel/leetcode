#include <iostream>
#include <string>

using namespace std;


bool check(string c) {
  int sz = c.length();
  for (int i = 0; i < sz; ++i)
    if (c[i] == '-')
      return false;
  return true;
}

string solve(string c, int k) {
  if (!check(c) && c.length() < k)
    return "IMPOSSIBLE";
  int sz = c.length();
  int cnt = 0;
  for (int i = 0; i <= sz - k; ++i) {
    if (c[i] == '-') {
      cnt += 1;
      for (int j = 0; j < k; ++j)
        c[i + j] = (c[i + j] == '+' ? '-' : '+');
    }
  }
  for (int i = sz - k; i < sz; ++i)
    if (c[i] == '-')
      return "IMPOSSIBLE";
  return to_string(cnt);
}

int main(int argc, char const *argv[]) {
  cin.tie(nullptr), ios_base::sync_with_stdio(false);
  int c;
  cin >> c;
  for (int i = 1; i <= c; ++i) {
    string cake;
    int k;
    cin >> cake >> k;
    cout << "Case #" << i << ": " << solve(cake, k) << endl;
  }

  return 0;
}
