//
// Created by user on 1/13/2020.
//

#ifndef GAMMA_FRIED_H
#define GAMMA_FRIED_H


#include "FoodFactory.h"

class Fried : public FoodFactory
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


#endif //GAMMA_FRIED_H
