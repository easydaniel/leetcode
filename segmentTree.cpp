#include <cstdio>
#include <vector>
#include <cmath>
using namespace std;


struct segment {
  int start, end, mid, vmin, vmax, vsum, chg;
  bool lazy;
  segment() {
    start = -1, end = -1;
    vmin = INT_MAX;
    vmax = INT_MIN;
    vsum = 0;
  }
  void init(int _start, int _end, int _vmin, int _vmax, int _vsum) {
    start = _start;
    end = _end;
    mid = _start + (1 << (int)log2(_end - _start)) - 1;
    vmin = _vmin;
    vmax = _vmax;
    vsum = _vsum;
    lazy = false;
    chg = 0;
  }
  void show() {
    printf("[%d:%d], min: %d, max: %d, sum: %d\n", start, end, vmin, vmax, vsum);
  }
};

int min(int a, int b) {
  return a > b ? b : a;
}

int max(int a, int b) {
  return a > b ? a : b;
}

int sum(int a, int b) {
  return a + b;
}

void _build(vector<int> &v, vector<struct segment> &st, int s, int e, int d, int sz) {
  if (s > e || s >= v.size()) {
    return;
  }
  int idx = (1 << (sz - d)) + (s >> d);
  if (s == e) {
    st[idx].init(s, e, v[s], v[s], v[s]);
    return;
  }
  int m = s + (1 << (int)log2(e - s)) - 1;
  _build(v, st, s, m, d - 1, sz);
  _build(v, st, m + 1, e, d - 1, sz);
  st[idx].init(s, e, min(st[idx * 2].vmin, st[idx * 2 + 1].vmin),\
                     max(st[idx * 2].vmax, st[idx * 2 + 1].vmax),\
                     sum(st[idx * 2].vsum, st[idx * 2 + 1].vsum));
}

vector<struct segment> build(vector<int> v) {
  size_t sz = v.size();
  int depth = (int)ceil(log2(sz));
  vector<struct segment> st(1 << (depth + 1));
  _build(v, st, 0, (1 << depth) - 1, depth, depth);
  return st;
}


void addRange(vector<struct segment> &st, int i, int j, int value, int idx = 1) {
  if (st[idx].start == i && st[idx].end == j) {
    st[idx].vmin += value;
    st[idx].vmax += value;
    st[idx].vsum += value * (j - i + 1);
    st[idx].lazy = true;
    st[idx].chg = value;
    return;
  }
  if (i > st[idx].end || j < st[idx].start) {
    return;
  } else if (st[idx].mid >= j) {
    addRange(st, i, j, value, idx * 2);
  } else if (st[idx].mid < i) {
    addRange(st, i, j, value, idx * 2 + 1);
  } else {
    int m = i + (1 << (int)log2(j - i)) - 1;
    addRange(st, i, m, value, idx * 2);
    addRange(st, m + 1, j, value, idx * 2 + 1);
  }
  st[idx].vmin = min(st[idx * 2].vmin, st[idx * 2 + 1].vmin);
  st[idx].vmax = max(st[idx * 2].vmax, st[idx * 2 + 1].vmax);
  st[idx].vsum = sum(st[idx * 2].vsum, st[idx * 2 + 1].vsum);
}

void passLazy(vector<struct segment> &st, int idx, int chg) {
    st[idx].lazy = true;
    st[idx].vmin += chg;
    st[idx].vmax += chg;
    st[idx].vsum += chg * (st[idx].end - st[idx].start + 1);
}

int queryMax(vector<struct segment> &st, int i, int j, int idx = 1) {
  if (st[idx].lazy) {
    st[idx].lazy = false;
    passLazy(st, idx * 2, st[idx].chg);
    passLazy(st, idx * 2 + 1, st[idx].chg);
  }
  if (st[idx].start == i && st[idx].end == j) {
    return st[idx].vmax;
  }
  if (i > st[idx].end || j < st[idx].start) {
    return INT_MIN;
  } else if (st[idx].mid >= j) {
    return queryMax(st, i, j, idx * 2);
  } else if (st[idx].mid < i) {
    return queryMax(st, i, j, idx * 2 + 1);
  } else {
    int m = i + (1 << (int)log2(j - i)) - 1;
    return max(queryMax(st, i, m, idx * 2), queryMax(st, m + 1, j, idx * 2 + 1));
  }
}

int queryMin(vector<struct segment> &st, int i, int j, int idx = 1) {
  if (st[idx].lazy) {
    st[idx].lazy = false;
    passLazy(st, idx * 2, st[idx].chg);
    passLazy(st, idx * 2 + 1, st[idx].chg);
  }
  if (st[idx].start == i && st[idx].end == j) {
    return st[idx].vmin;
  }
  if (i > st[idx].end || j < st[idx].start) {
    return INT_MAX;
  } else if (st[idx].mid >= j) {
    return queryMin(st, i, j, idx * 2);
  } else if (st[idx].mid < i) {
    return queryMin(st, i, j, idx * 2 + 1);
  } else {
    int m = i + (1 << (int)log2(j - i)) - 1;
    return min(queryMin(st, i, m, idx * 2), queryMin(st, m + 1, j, idx * 2 + 1));
  }
}

int querySum(vector<struct segment> &st, int i, int j, int idx = 1) {
  if (st[idx].lazy) {
    st[idx].lazy = false;
    passLazy(st, idx * 2, st[idx].chg);
    passLazy(st, idx * 2 + 1, st[idx].chg);
  }
  if (st[idx].start == i && st[idx].end == j) {
    return st[idx].vsum;
  }
  if (i > st[idx].end || j < st[idx].start) {
    return 0;
  } else if (st[idx].mid >= j) {
    return querySum(st, i, j, idx * 2);
  } else if (st[idx].mid < i) {
    return querySum(st, i, j, idx * 2 + 1);
  } else {
    int m = i + (1 << (int)log2(j - i)) - 1;
    return sum(querySum(st, i, m, idx * 2), querySum(st, m + 1, j, idx * 2 + 1));
  }
}

int main(int argc, char const *argv[]) {
  /* code */
  vector<int> v = {4, 1, 2, 5, 3, 3};
  vector<struct segment> st = build(v);
  // for (int i = 0; i < st.size(); ++i) {
  //   st[i].show();
  // }
  printf("%d\n", queryMin(st, 0, 3));
  addRange(st, 0, 4, 1);
  printf("%d\n", queryMin(st, 0, 3));
  // for (int i = 0; i < st.size(); ++i) {
  //   st[i].show();
  // }
  return 0;
}
