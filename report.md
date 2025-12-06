# Report: AI Impact On Jobs 2030

This dataset contains job titles and associated categories which estimates the impact of AI on occupations by 2030, I got it from Kaggle. The file includes columns such as `Job_Title`, `Average_Salary`, `Automation_Probability_2030`, `AI_Exposure_Index`, and `Risk_Category`. I used the CSV file located in the `data/` folder for all analysis steps.

I performed the these pandas operations in `analyze_data.py`: loading a CSV into a DataFrame (`pd.read_csv`), inspecting the data with `head()`, `info()`, and `describe()` as mentioned in the assignment, accessing rows and slices with `loc` and `iloc`, selecting a single column, reading a single cell by label, filtering with boolean conditions (single comparison and a combined `&` condition), adding a derived column (`AI_Risk_Score`), dropping a column with `.drop(axis=1)`, and grouping by a categorical column (`Risk_Category`) to compute mean `Average_Salary` using `groupby().mean()`.

From these operations I observed that average salaries vary meaningfully across risk categories and that jobs with higher automation probabilities tend to have diverse salary ranges: some high-paying roles still show notable automation risk. For limitations, the dataset contains some missing values in a few columns and column name conventions had to be exact (e.g., underscores and capitalization). 
