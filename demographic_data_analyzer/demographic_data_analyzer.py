import pandas as pd


def calculate_demographic_data(print_data=True):

    columns = [
        'age', 'workclass', 'fnlwgt', 'education',
        'education-num', 'marital-status', 'occupation',
        'relationship', 'race', 'sex', 'capital-gain',
        'capital-loss', 'hours-per-week', 'native-country',
        'salary'
    ]

    df = pd.read_csv(
        "adult.data.csv",
        header=None,
        names=columns,
        skipinitialspace=True
    )

    # 1 number of people of each race
    race_count = df['race'].value_counts()

    # 2. men's average age
    average_age_men = round(
        df[df['sex'] == 'Male']['age'].mean(), 1
    )

    # 3. bachelor's percentage
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1
    )

    # 4. % with advanced education that earn >50K
    higher_education = df['education'].isin(
        ['Bachelors', 'Masters', 'Doctorate']
    )

    higher_education_rich = df[
        higher_education & (df['salary'] == '>50K')
    ]

    percentage_higher_education_rich = round(
        (len(higher_education_rich) / len(df[higher_education])) * 100, 1
    )

    # 5. % without advanced education that earn >50K
    lower_education = ~higher_education

    lower_education_rich = df[
        lower_education & (df['salary'] == '>50K')
    ]

    percentage_lower_education_rich = round(
        (len(lower_education_rich) / len(df[lower_education])) * 100, 1
    )

    # 6. minimum work hours per week
    min_work_hours = df['hours-per-week'].min()

    # 7. % of rich among those who work minimum hours
    min_workers = df[df['hours-per-week'] == min_work_hours]

    rich_min_workers = min_workers[
        min_workers['salary'] == '>50K'
    ]

    rich_percentage = round(
        (len(rich_min_workers) / len(min_workers)) * 100, 1
    )

    # 8. country with highest percentage of rich
    country_salary = (
        df[df['salary'] == '>50K']
        .groupby('native-country')
        .size()
        / df.groupby('native-country').size()
    ) * 100

    highest_earning_country = country_salary.idxmax()
    highest_earning_country_percentage = round(
        country_salary.max(), 1
    )

    # 9. occupation with highest percentage of rich Indians
    india_rich = df[
        (df['native-country'] == 'India') &
        (df['salary'] == '>50K')
    ]

    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors:", percentage_bachelors)
        print("Higher education rich:", percentage_higher_education_rich)
        print("Lower education rich:", percentage_lower_education_rich)
        print("Min work hours:", min_work_hours)
        print("Rich percentage among min workers:", rich_percentage)
        print("Country with highest % earning >50K:", highest_earning_country)
        print("Highest earning country percentage:", highest_earning_country_percentage)
        print("Top occupation in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'percentage_higher_education_rich': percentage_higher_education_rich,
        'percentage_lower_education_rich': percentage_lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
