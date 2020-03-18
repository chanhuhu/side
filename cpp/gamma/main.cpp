#include "FoodFactory.h"

int main() {
    FoodFactory* x = new FoodFactory(1);
    x->getPrice((std::string *) "thai");
}