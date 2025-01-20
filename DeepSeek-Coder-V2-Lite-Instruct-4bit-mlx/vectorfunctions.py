#include <vector>
using namespace std;

// Reverse a vector.
void backwards(vector<int>& vec){
    int n = vec.size();
    for (int i = 0; i < n / 2; ++i) {
        swap(vec[i], vec[n - i - 1]);
    }
}

// Return every other element of the vector, starting with the first.
vector<int> everyOther(const vector<int>& vec){
    vector<int> result;
    for (size_t i = 0; i < vec.size(); i += 2) {
        result.push_back(vec[i]);
    }
    return result;
}

// Return the smallest value of a vector.
int smallest(const vector<int>& vec){
    int min_val = INT_MAX;
    for (int num : vec) {
        if (num < min_val) {
            min_val = num;
        }
    }
    return min_val;
}

// Return the sum of the elements in the vector.
int sum(const vector<int>& vec){
    int total = 0;
    for (int num : vec) {
        total += num;
    }
    return total;
}

// Return the number of odd integers, that are also on an
// odd index (with the first index being 0).
int veryOdd(const vector<int>& vec){
    int count = 0;
    for (size_t i = 0; i < vec.size(); ++i) {
        if (vec[i] % 2 != 0 && i % 2 != 0) {
            ++count;
        }
    }
    return count;
}