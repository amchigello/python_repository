# try catch block
# else block
# finally block
# assert statement
# custom exception


class ZeroSpeedLimit(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class vehicle:
    def __init__(self, brand, color, type_of_vehicle):
        self.brand = brand
        self.color = color
        self.type_of_vehicle = type_of_vehicle
        print("A {} vehicle, {} created of {} color".format(
            type_of_vehicle, brand, color))

    def set_speed_limit(self, speed_limit):
        try:
            if speed_limit <= 0:
                raise ZeroSpeedLimit(
                    'SpeedLimit {}'.format(speed_limit), 'Speed Limit cannot be zero/negetive')
            assert (speed_limit > 140), "Unsafe speed limit"
            self.set_speed_limit = speed_limit
        except Exception as e:
            print(e)
        else:
            print("speed limit of {} set for {}".format(
                speed_limit, self.brand))
        finally:
            print("speed limit set method completed")


if __name__ == '__main__':
    avenger = vehicle('Bajaj Avenger', 'White', 'Two wheel')
    avenger.set_speed_limit(100)
