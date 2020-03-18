//
// Created by user on 1/13/2020.
//

#ifndef GAMMA_SOUP_H
#define GAMMA_SOUP_H

#include <string>
#include "FoodFactory.h"

class Soup : public FoodFactory
{
public:
    int getPrice(std::string type) const override {
        if (type == "thai") return thai;
        if (type == "visitor") return visitor;
    }

private:
    int thai = 60;
    int visitor = 120;
};

#endif //GAMMA_SOUP_H
