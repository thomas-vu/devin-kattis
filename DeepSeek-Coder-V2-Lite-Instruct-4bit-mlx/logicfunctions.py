# logicfunctions.cpp
#include <iostream>
#include "logicfunctions.h"

// Compute xor
void exclusive_or(bool x, bool y, bool &result) {
    result = (x != y);
}

// Compute implication
void implication(bool x, bool y, bool &result) {
    result = (!x || y);
}

// Compute equivalence
void equivalence(bool x, bool y, bool &result) {
    result = (x == y);
}