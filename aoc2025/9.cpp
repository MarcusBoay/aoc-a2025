#include <cmath>
#include <iostream>
#include <sstream>
#include <vector>
#include <fstream>

using namespace std;

const auto EPS = 1e-9;

struct point {
  double x, y;
  point() { x = y = 0; }
  point(double _x, double _y) : x(_x), y(_y) {}
  bool operator == (const point &other) const {
    return fabs(x-other.x) < EPS && fabs(y==other.y) < EPS;
  }
  bool operator != (const point &other) const {
    return fabs(x-other.x) > EPS && fabs(y-other.y) > EPS;
  }
};

double dist(const point &p1, const point &p2) { // Euclidean distance
  auto dx = p1.x-p2.x;
  auto dy = p1.y-p2.y;
  return sqrt(dx*dx + dy*dy);
}

struct vec {
  double x=0, y=0;
  vec(double _x, double _y) : x(_x), y(_y) {}
};

vec toVec(const point &a, const point &b) {
  return vec(b.x-a.x, b.y-a.y);
}

double dot(vec a, vec b) { return (a.x*b.x + a.y*b.y); }

double norm_sq(vec v) { return v.x*v.x + v.y*v.y; }

double angle(const point &a, const point &o, const point &b) {
  vec oa = toVec(o, a), ob = toVec(o, b); // a != o != b
  return acos(dot(oa, ob) / sqrt(norm_sq(oa) * norm_sq(ob))); // angle aob in rad
}

double cross(vec a, vec b) { return a.x*b.y - a.y*b.x; }

// returns true if point r is on the left side of line pq
bool ccw(point p, point q, point r) {
  return cross(toVec(p, q), toVec(p, r)) > EPS;
}

/*
 * return 1/0/-1 if point is inside/on vertex/outside of
 * either convex/concave polygon P
 */
int insidePolygon(point pt, const vector<point> &P) {
  int n = (int)P.size();
  if (n <= 3) return -1;
  bool on_polygon = false;
  for (int i = 0; i < n-1; ++i)
    if (fabs(dist(P[i], pt) + dist(pt, P[i+1]) - dist(P[i], P[i+1])) < EPS)
      on_polygon = true;
  if (on_polygon) return 0;
  double sum = 0.0;
  for (int i = 0; i < n-1; ++i) {
    if (ccw(pt, P[i], P[i+1]))
      sum += angle(P[i], pt, P[i+1]);
    else
      sum -= angle(P[i], pt, P[i+1]);
  }
  return fabs(sum) > M_PI ? 1 : -1;
}

struct line { double a, b, c; }; // ax + by + c = 0

// answer stored in third param (pass by ref)
void pointsToLine(const point &p1, const point &p2, line &l) {
  if (fabs(p1.x-p2.x) < EPS)
    l = {1.0, 0.0, -p1.x};
  else
    l = {-(double)(p1.y-p2.y) / (p1.x-p2.x),
         1.0,
         -(double)(l.a*p1.x) - p1.y};
}

bool areParallel(line l1, line l2) {
  return (fabs(l1.a-l2.a) < EPS) && (fabs(l1.b-l2.b) < EPS);
}

bool areSame(line l1, line l2) {
  return areParallel(l1, l2) && (fabs(l1.c-l2.c) < EPS);
}

// return true (+ intersection point p) if two lines aer intersect
bool areIntersect(line l1, line l2, point &p) {
  if (areParallel(l1, l2)) return false; // no intersection
  // solve system of 2 linear algebraic equations with 2 unknowns
  p.x = (l2.b*l1.c - l1.b*l2.c) / (l2.a*l1.b - l1.a*l2.b);
  // special case: test for vertical line to avoid division by zero
  if (fabs(l1.b > EPS))
    p.y = -(l1.a*p.x + l1.c);
  else
    p.y = -(l2.a*p.x + l2.c);
  return true;
}

vec scale(const vec &v, double s) {
  return vec(v.x*s, v.y*s);
}

point translate(const point &p, const vec &v) {
  return point(p.x+v.x, p.y+v.y);
}

double distToLine(point p, point a, point b, point &c) {
  vec ap = toVec(a, p), ab = toVec(a, b);
  double u = dot(ap, ab) / norm_sq(ab);
  c = translate(a, scale(ab, u));
  return dist(p, c);
}

double distToLineSegment(point p, point a, point b, point &c) {
  vec ap = toVec(a, p), ab = toVec(a, b);
  double u = dot(ap, ab) / norm_sq(ab);
  if (u < 0.0) {
    c = point(a.x, a.y);
    return dist(p, a);
  }
  if (u > 1.0) {
    c = point(b.x, b.y);
    return dist(p, b);
  }
  return distToLine(p, a, b, c);
}

point lineIntersectSeg(point p, point q, point A, point B) {
  double a = B.y-A.y, b = A.x-B.x, c = B.x*A.y - A.x*B.y;
  double u = fabs(a*p.x + b*p.y + c);
  double v = fabs(a*q.x + b*q.y + c);
  return point((p.x*v + q.x*u) / (u+v), (p.y*v + q.y*u) / (u+v));
}

vector<point> cutPolygon(point A, point B, const vector<point> &Q) {
  vector<point> P;
  for (int i = 0; i < (int)Q.size(); ++i) {
    double left1 = cross(toVec(A, B), toVec(A, Q[i])), left2 = 0;
    if (i != (int)Q.size()-1) left2 = cross(toVec(A, B), toVec(A, Q[i+1]));
    if (left1 > -EPS) P.push_back(Q[i]);
    if (left1*left2 < -EPS)
      P.push_back(lineIntersectSeg(Q[i], Q[i+1], A, B));
  }
  if (!P.empty() && !(P.back() == P.front()))
    P.push_back(P.front());
  return P;
}

// all points of the polygon
vector<point> P;

void getInput(string fileName) {
    string str = "";
    ifstream file(fileName);
    const char delimiter = ',';
    int ci = 0;
    while (getline(file, str)) {
        stringstream ss(str);
        string t;
        vector<string> s = {};
        while (!ss.eof()) {
            getline(ss, t, delimiter);
            s.push_back(t);
        }
        point pi = point(stoi(s[0]), stoi(s[1]));
        P.push_back(std::move(pi));
    }
    P.push_back(P[0]);
    file.close();
}

unsigned long long area_i(const point &p1, const point &p3) {
  auto dx = abs(p1.x-p3.x)+1.0;
  auto dy = abs(p1.y-p3.y)+1.0;
  return ((unsigned long long)dx)*((unsigned long long)dy);
}

bool isOnLineSeg(const point &cur, const point &next, const point &intersect_point) {
  return (cur.y == next.y && intersect_point.y == cur.y && cur.x < next.x && intersect_point.x > cur.x && intersect_point.x < next.x) ||
          (cur.y == next.y && intersect_point.y == cur.y && cur.x > next.x && intersect_point.x < cur.x && intersect_point.x > next.x) ||
          (cur.x == next.x && intersect_point.x == cur.x && cur.y < next.y && intersect_point.y > cur.y && intersect_point.y < next.y) ||
          (cur.x == next.x && intersect_point.x == cur.x && cur.y > next.y && intersect_point.y < cur.y && intersect_point.y > next.y);
}

bool lineSegIntersect(point a, point b, point c, point d) {
  return ccw(a,c,d) != ccw(b,c,d) && ccw(a,b,c) != ccw(a,b,d);
}

int main(int argc, char* argv[]) {
  getInput("9.in");
  ofstream out_file("9.coords");
  auto old_rdbuf = clog.rdbuf();
  clog.rdbuf(out_file.rdbuf());
  // iterate over all points, assign p1, p3 as the opposite points
  // create p2, p4 from the candidate points
  // check if all points of the rect are in the polygon
  // if yes, the area is a candidate for the largest area
  // if no, reject
  unsigned long long largest_area = 1; // trivial case: a single point is always 1
  point lp1, lp3;
  for (int i = 0; i < P.size(); ++i) {
    for (int j = i+1; j < P.size(); ++j) {
      point p1 = P[i], p3 = P[j];
      point p2 = point(p1.x, p3.y), p4 = point(p3.x, p1.y);
      vector<point> rect_points = {p1, p2, p3, p4, p1};

      int is_inside = 0;
      for (auto p : rect_points) {
        is_inside = insidePolygon(p, P);
        if (is_inside == -1) {
          break;
        }
      }

      if (is_inside == -1) {
        continue;
      }
      clog << area_i(p1,p3) << "," << p1.x << "," << p1.y << "," << p3.x << "," << p3.y << endl;
      // else if (is_inside == 0) {
      //   cout << "on polygon!!" << p1.x << "," << p1.y << endl;
      // }

      bool is_intersecting = false;
      // iterate over each line of each polygon and try to check if they intersect
      // if they do, reject
      for (int k = 0; k < rect_points.size()-1; ++k) {
        point cur = rect_points[k];
        point next = rect_points[k+1];
        // line rect_side;
        // pointsToLine(cur, next, rect_side);

        for (int m = 0; m < P.size()-1; ++m) {
          point p_cur = P[m];
          point p_next = P[m+1];
          // line poly_side;
          // pointsToLine(p_cur, p_next, poly_side);

          // if polygon line segment doesn't intersect, we are done
          if (!lineSegIntersect(cur, next, p_cur, p_next)) {
            continue;
          }
          // try to cut the rect
          // if rect can be cut, the rect is intersecting the polygon
          auto Q = cutPolygon(p_cur, p_next, rect_points);
          if (Q.size() > 0) {
            is_intersecting = true;
            break;
          }

          // if (cur == p_cur || cur == p_next || next == p_cur || next == p_next) {
          //   continue;
          // }

          // point intersect_point;
          // if (areIntersect(rect_side, poly_side, intersect_point) &&
          //     // !areParallel(rect_side, poly_side) &&
          //     !areSame(rect_side, poly_side)) {
          //   point dummy1;
          //   point dummy2;
          //   auto d1 = distToLineSegment(intersect_point, p_cur, p_next, dummy1);
          //   auto d2 = distToLineSegment(intersect_point, cur, next, dummy2);
          //   if (p1.x == 17217 && p1.y == 85603 && p3.x == 82570 && p3.y == 14626 && m > 248 && m < 252) {
          //     cout << "found the thingy: " << d1 << "," << d2 << endl;
          //     // cout << dist(cur, intersect_point) << " + " << dist(intersect_point, next) << " ==? " << dist(cur, next)
          //     //   << endl;
          //
          //     cout << "rect: "
          //         << p1.x << "," << p1.y << "  "
          //         << p2.x << "," << p2.y << "  "
          //         << p3.x << "," << p3.y << "  "
          //         << p4.x << "," << p4.y << "  "
          //         << "rect_side: "
          //         << cur.x << "," << cur.y << "  "
          //         << next.x << "," << next.y << "  "
          //         << "poly_side: "
          //         << p_cur.x << "," << p_cur.y << "  "
          //         << p_next.x << "," << p_next.y << "  "
          //         << "intersect_point: "
          //         << intersect_point.x << "," << intersect_point.y
          //         // << a << endl;
          //         << endl;
          //   }
          //
          //   // cout << d1 << "x" << d2 << endl;
          //   if (
          //       ((d1 < EPS && d1 > -EPS) && (d2 < EPS && d2 > -EPS)) &&
          //       // (cur != intersect_point && next != intersect_point) &&
          //       // (dummy1 == intersect_point || dummy2 == intersect_point) &&
          //       // isOnLineSeg(cur, next, intersect_point) &&
          //       // isOnLineSeg(p_cur, p_next, intersect_point)
          //       // lineSegIntersect(cur, next, p_cur, p_next)
          //       true
          //       ) {
          //   // if ((d1 < EPS && d1 > -EPS) && (d2 < EPS && d2 > -EPS)) {
          //     // cout << "found the thingy: " << d1 << "," << d2 << endl;
          //   // if (dist(cur, intersect_point) + dist(intersect_point, next) == dist(cur, next) &&
          //   //     dist(p_cur, intersect_point) + dist(intersect_point, p_next) == dist(p_cur, p_next)) {
          //     if (p1.x == 17217 && p1.y == 85603 && p3.x == 82570 && p3.y == 14626) {
          //       cout << "hi" << endl;
          //       cout << "rect: "
          //           << p1.x << "," << p1.y << "  "
          //           << p2.x << "," << p2.y << "  "
          //           << p3.x << "," << p3.y << "  "
          //           << p4.x << "," << p4.y << "\n"
          //           << "rect_side: "
          //           << cur.x << "," << cur.y << "  "
          //           << next.x << "," << next.y << "\n"
          //           << "poly_side: "
          //           << p_cur.x << "," << p_cur.y << "  "
          //           << p_next.x << "," << p_next.y << "\n"
          //           << "intersect_point: "
          //           << intersect_point.x << "," << intersect_point.y << "  "
          //           << "dummy1: "
          //           << dummy1.x << "," << dummy1.y << "  "
          //           << "dummy2: "
          //           << dummy2.x << "," << dummy2.y << "  "
          //           // << a << endl;
          //           << endl;
          //       // if (dummy1 == intersect_point || dummy2 == intersect_point) {
          //       //   cout << "dummies!!" << endl;
          //       // }
          //     }
          //     is_intersecting = true;
          //     // cout << "intersecting at: " << intersect_point.x << "," << intersect_point.y
          //     //      << " for points " << cur.x << "," << cur.y << ":" << next.x << "," << next.y
          //     //      << " against " << p_cur.x << "," << p_cur.y << ":" << p_next.x << "," << p_next.y << endl;
          //     break;
          //   }
          // }
        }

        if (is_intersecting) {
          break;
        }
      }

      if (!is_intersecting) {
        unsigned long long a = area_i(p1, p3);
        if (a > largest_area) {
          cout << "FOUND LARGEST AREA: "
              << p1.x << "," << p1.y << "  "
              << p2.x << "," << p2.y << "  "
              << p3.x << "," << p3.y << "  "
              << p4.x << "," << p4.y << "  "
              << a << endl;
          largest_area = max(largest_area, a);
          lp1 = p1;
          lp3 = p3;
        }
      }
    }
  }
  cout << "Largest area: " << largest_area << endl;
  // write largest area coords out
  clog.rdbuf(old_rdbuf);

  return 0;
}
