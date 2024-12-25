import pandas as pd
import numpy as np
from random import choice, randint, uniform
from datetime import datetime, timedelta

def generate_structured_dataset(n=1000, output_file='structured_customer_data.csv'):
    """
    Генерация структурированного датасета с логической связью между признаками и целевой переменной.
    
    Параметры:
        n (int): Количество строк в датасете.
        output_file (str): Имя CSV файла для сохранения данных.
    """
    data = []
    
    for i in range(n):
        customer_id = i + 1
        age = randint(18, 80)
        gender = choice(['Male', 'Female'])
        registration_date = datetime(2020, 1, 1) + timedelta(days=randint(0, 2000))
        average_purchase_value = round(uniform(0, 1000), 2)
        visit_frequency = randint(1, 30)
        days_since_last_visit = randint(1, 60)
        purchase_last_30_days = randint(0, 10)
        customer_feedback_score = randint(1, 5)
        is_subscribed = choice(['Yes', 'No'])
        is_first_time_visitor = choice(['Yes', 'No'])
        
        # Генерация целевой переменной с логикой
        # Чем выше частота посещений и сумма покупок, тем выше вероятность совершить покупку
        purchase_probability = (
            (visit_frequency / 30) + 
            (average_purchase_value / 1000) + 
            (1 - days_since_last_visit / 60) + 
            (0.2 if is_subscribed == 'Yes' else 0) + 
            (0.1 if customer_feedback_score >= 4 else 0)
        )
        target = 1 if purchase_probability > uniform(0, 1.5) else 0  # Искусственно регулируем сложность
        
        data.append([
            customer_id, age, gender, registration_date.strftime('%Y-%m-%d'),
            average_purchase_value, visit_frequency, days_since_last_visit, 
            purchase_last_30_days, customer_feedback_score, is_subscribed, 
            is_first_time_visitor, target
        ])
    
    # Создаем DataFrame
    columns = [
        'customer_id', 'age', 'gender', 'registration_date', 
        'average_purchase_value', 'visit_frequency', 'days_since_last_visit', 
        'purchase_last_30_days', 'customer_feedback_score', 
        'is_subscribed', 'is_first_time_visitor', 'target'
    ]
    df = pd.DataFrame(data, columns=columns)
    
    # Сохранение в CSV файл
    df.to_csv(output_file, index=False)
    print(f"Структурированный датасет сохранен в '{output_file}'.")

# Генерация датасета с логикой
generate_structured_dataset(1000)
