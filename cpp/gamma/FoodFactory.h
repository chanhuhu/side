#ifndef GAMMA_FOODFACTORY_H
#define GAMMA_FOODFACTORY_H

#include <string>
#include <iostream>

#include "Fried.h"
#include "Soup.h"

class FoodFactory {
public:
    virtual int getPrice(std::string &type) const = 0;

    explicit FoodFactory(int type) {
        switch (type) {
            case 1:
                return new Fried;
                break;
            case 2:
                return new Soup;
                break;
            default:
                std::cout << "error \n";
        }
    }

    virtual ~FoodFactory() { }
};


#endif
