import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate 500 random values for Years of Experience (between 0 and 40 years)
years_experience = np.random.randint(0, 21, 500)

# Generate corresponding Salaries using a linear relationship + some noise
salaries = 3000 * years_experience + np.random.normal(20000, 10000, 500)

# Ensure no negative salaries and round to nearest 5000
salaries = np.maximum(salaries, 10000)
salaries = (np.round(salaries / 5000) * 5000).astype(int)

# Generate Performance Score (1-10) based on Years of Experience
performance_score = np.clip(years_experience / 4 + np.random.normal(5, 1, 500), 1, 10).astype(int)

# Create DataFrame
df = pd.DataFrame({
    "Sl. No.": range(1, 501),
    "YearsExperience": years_experience,
    "Salary": salaries,
    "PerformanceScore": performance_score
})

# Save to CSV
file_path = "Salary_dataset.csv"
df.to_csv(file_path, index=False)

# Display first few rows
df.head()
