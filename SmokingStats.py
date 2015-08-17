__author__ = 'Greg'


class SmokingStats:
    # SmokingStats -- this class encapsulates needed variables and uses them to calculate how much you will spend
    DAYS_IN_50_YEARS = 18250

    def __init__(self, pack_price=0.0, number_cigs=0, inflation=0.0):
        self.__packPrice = pack_price
        self.__number_cigs = number_cigs
        self.__inflation = inflation
        self.__packs_per_day = 0.00
        self.__price_per_day = 0.00
        self.__inflation_decimal = 0.00
        self.__inflation_per_day = 0.00
        self.__num_days_in_50_years = 18250
        self.__cigs_to_pack_CF = 0.05
        self.__percent_to_decimal_CF = 0.01
        self.__per_year_to_per_day_CF = 0.0027397
        self.__total = 0.00

    def set_pack_price(self, price):
        self.__packPrice = price

    def set_number_cigs(self, num):
        self.__number_cigs = num

    def set_inflation(self, inflat):
        self.__inflation = inflat

    def set_packs_per_day(self):
        self.__packs_per_day = self.__number_cigs * self.__cigs_to_pack_CF

    def set_price_per_day(self):
        self.__price_per_day = self.__packs_per_day * self.__packPrice

    def set_inflation_decimal(self):
        self.__inflation_decimal = self.__inflation * self.__percent_to_decimal_CF

    def set_inflation_per_day(self):
        self.__inflation_per_day = self.__inflation_decimal * self.__per_year_to_per_day_CF

    def set_total(self, tot):
        self.__total = tot

    def get_total(self):
        return self.__total

    def get_price_per_day(self):
        return self.__price_per_day

    def set_price_per_day_loop(self, perDay, inflat):
        self.__price_per_day = perDay * inflat + perDay

    def calculate_cost(self):
        i = 0
        for i in range(0, self.DAYS_IN_50_YEARS):
            self.set_total(self.__total + self.__price_per_day)
            self.set_price_per_day_loop(self.__price_per_day, self.__inflation_per_day)
