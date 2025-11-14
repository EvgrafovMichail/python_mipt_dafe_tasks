from typing import Callable

def make_averager(accumulation_period: int) -> Callable[[float], float]:
    list_nums = []
    # замыкаем список и создаем обертку 


    def calculator(income: float) -> float:
        # добавляем в список прибыль 
        list_nums.append(income)

        # список должен состоять из 2х элементов
        if len(list_nums) > accumulation_period: 
            list_nums.pop(0)
        
        # далее возвращаем среднее арифметическое
        # учитыеваем что занчений может быть меньше чем accumulation_period
        summa = 0
        for num in list_nums:
            summa += num


        return summa/len(list_nums)

    return calculator