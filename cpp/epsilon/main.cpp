#include <iostream>
#include "days.h"

int main() {
    days test;
    std::vector<std::string> check{"Friday", "Thursday", "Monday"};
    std::vector<std::string> check2{"Friday", "Thursday", "Monday", "Sunday"};
    std::vector<std::string> check3{"Friday", "Thursday", "Sunday"};
    test.setAvailbleDays(check);
    test.checkDays(check3);
}
