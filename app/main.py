class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self, distance_from_city_center, clean_power, average_rating, count_of_ratings
    ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars):
        result = 0

        for car in cars:
            result += self.calculate_washing_price(car)
            self.wash_single_car(car)

        return result

    def calculate_washing_price(self, car: Car):
        if car.clean_mark < self.clean_power:
            result = (
                car.comfort_class
                * (self.clean_power - car.clean_mark)
                * self.average_rating
                / self.distance_from_city_center
            )
            return round(result, 1)

        return 0

    def wash_single_car(self, car: Car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
            return True

        return False

    def rate_service(self, num):
        if num >= 0 and num <= 10:
            self.count_of_ratings += 1
            self.average_rating = round(
                (self.average_rating * (self.count_of_ratings - 1) + num)
                / self.count_of_ratings,
                1,
            )
