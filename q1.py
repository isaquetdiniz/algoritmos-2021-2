def main():
    class Day:
        def __init__(self, value_in_day):
            self.value_in_day = value_in_day
            self.previous_day = None

        def get_value_in_day(self):
            return self.value_in_day

        def get_previous_day(self):
            return self.previous_day

        def update_previous_day(self, previous_day):
            self.previous_day = previous_day

    class List_of_days:
        def __init__(self):
            self.last_day = None
            self.big_number = 0
            self.actual_day = 0

        def verify_has_last_day(self):
            if(self.last_day == None):
                raise Exception('Nenhum dia foi adicionado')

        def add_day(self, day):
            last_day = self.last_day

            if(last_day == None):
                self.last_day = day
                self.big_number = day.get_value_in_day()
                self.actual_day += 1
                return self

            if(day.get_value_in_day() > self.big_number):
                self.big_number = day.get_value_in_day()

            day.update_previous_day(last_day)
            self.last_day = day
            self.actual_day += 1

        def get_number_of_good_days_to_sell_actions(self):
            self.verify_has_last_day()

            number_days = 1

            last_day = self.last_day

            actual_value_of_day = last_day.get_value_in_day()

            last_day_previous_day = last_day.get_previous_day()
            last_day_has_previous_day = last_day_previous_day != None

            if(actual_value_of_day == self.big_number):
                number_days = self.actual_day
                print('O ULTIMO VALOR FOI {} E HOJE E UM BOM DIA PARA VENDER ACOES DOS ULTIMOS {} DIAS'.format(actual_value_of_day, number_days))
                return


            while(last_day_has_previous_day and actual_value_of_day >= last_day_previous_day.get_value_in_day()):
                number_days += 1
                last_day_previous_day = last_day_previous_day.get_previous_day()
                last_day_has_previous_day = last_day_previous_day != None

            print('O ULTIMO VALOR FOI {} E HOJE E UM BOM DIA PARA VENDER ACOES DOS ULTIMOS {} DIAS'.format(actual_value_of_day, number_days))


    list_of_days = List_of_days()

    number_interactions = int(input())

    for i in range(number_interactions):
        input_of_user = input()

        if(input_of_user.find('ATUALIZA') != -1):
            value_in_day = int(input_of_user.replace('ATUALIZA ', ''))

            new_day = Day(value_in_day)

            list_of_days.add_day(new_day)
        else:
            list_of_days.get_number_of_good_days_to_sell_actions()



if __name__ == '__main__':
    main()
