import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file into a Pandas DataFrame
    df = pd.read_csv('adult.data.csv')

    # Count the occurrences of each race in the dataset
    race_count = df['race'].value_counts()

    # Calculate the average age of males, rounded to one decimal place
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Calculate the percentage of people who have a Bachelor's degree
    percentage_bachelors = round(df[df['education'] == 'Bachelors'].shape[0] / df.shape[0] * 100, 1)

    # Determine whether a person has an advanced education (Bachelors, Masters, or Doctorate)
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])

    # Determine whether a person's salary is greater than 50K
    high_income = df['salary'] == '>50K'

    # Calculate the percentage of people with advanced education earning >50K
    higher_education_rich = round((advanced_education & high_income).sum() / advanced_education.sum() * 100, 1)

    # Calculate the percentage of people without advanced education earning >50K
    lower_education_rich = round((~advanced_education & high_income).sum() / (~advanced_education).sum() * 100, 1)

    # Find the minimum number of hours a person works per week
    min_work_hours = df['hours-per-week'].min()

    # Calculate the percentage of people working the minimum hours per week who earn >50K
    min_hours_workers = df['hours-per-week'] == min_work_hours
    rich_percentage = round((min_hours_workers & high_income).sum() / min_hours_workers.sum() * 100, 1)

    # Calculate the country with the highest percentage of high earners (>50K)
    country_earning_ratios = (df[high_income]['native-country'].value_counts()
                              / df['native-country'].value_counts() * 100).sort_values(ascending=False)
    highest_earning_country = country_earning_ratios.index[0]
    highest_earning_country_percentage = round(country_earning_ratios.iloc[0], 1)

    # Determine the most popular occupation for high earners (>50K) in India
    top_IN_occupation = df[(df['native-country'] == 'India') & high_income]['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    # Return results as a dictionary
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
