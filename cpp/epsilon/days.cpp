//
// Created by user on 12/22/2019.
//

#include "days.h"
#include <iostream>


void days::checkDays(const std::vector<std::string> &check) {
    if (check.size() > 3) {
        std::cout << "Input only three days.\n";
    } else {
        for (int i = 0; i < check.size(); ++i) {
            if (availableDays[i] == check[i]) {
                std::cout << check[i] << " is matched" << std::endl;
            } else {
                std::cout << check[i] << " is'not matched" << std::endl;
            }
        }
    }
}

void days::setAvailbleDays(std::vector<std::string> check) {
    availableDays = std::move(check);
}
