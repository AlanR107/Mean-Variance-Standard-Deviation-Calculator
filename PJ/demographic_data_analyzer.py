import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # 1. Race count
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degree
    total_people = len(df)
    bachelors = len(df[df['education'] == 'Bachelors'])
    percentage_bachelors = round((bachelors / total_people) * 100, 1)

    # 4. Higher education >50K
    higher_edu = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_edu_rich = len(higher_edu[higher_edu['salary'] == '>50K'])
    higher_education_rich = round((higher_edu_rich / len(higher_edu)) * 100, 1)

    # 5. Lower education >50K
    lower_edu = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_edu_rich = len(lower_edu[lower_edu['salary'] == '>50K'])
    lower_education_rich = round((lower_edu_rich / len(lower_edu)) * 100, 1)

    # 6. Min hours per week
    min_work_hours = df['hours-per-week'].min()

    # 7. Rich among min workers
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = len(min_workers[min_workers['salary'] == '>50K'])
    rich_percentage = round((rich_min_workers / len(min_workers)) * 100, 1)

    # 8. Country with highest % rich
    countries = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean() * 100)
    highest_earning_country = countries.idxmax()
    highest_earning_country_percentage = round(countries.max(), 1)

    # 9. Top occupation in India for rich
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors:", percentage_bachelors)
        print("Higher education rich %:", higher_education_rich)
        print("Lower education rich %:", lower_education_rich)
        print("Min work hours:", min_work_hours)
        print("Rich % among min workers:", rich_percentage)
        print("Highest earning country:", highest_earning_country)
        print("Top occupation in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }