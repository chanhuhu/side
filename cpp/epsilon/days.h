//
// Created by user on 12/22/2019.
//

#ifndef EPSILON_DAYS_H
#define EPSILON_DAYS_H


#include <string>
#include <vector>

class days {
    private:
    std::vector<std::string> availableDays;

    public:
    void checkDays(const std::vector<std::string>& check);
    void setAvailbleDays(std::vector<std::string> check);

};


#endif //EPSILON_DAYS_H
