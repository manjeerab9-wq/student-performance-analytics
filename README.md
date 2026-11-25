# Student Performance Analytics

A Python data analytics project that explores student academic performance using **Pandas** and **Matplotlib**. It calculates student averages and grades, summarizes subject performance, and creates visualizations to explore the relationship between study hours and scores.

> **Dataset note:** The included CSV contains fictional sample data created for demonstration and learning purposes.

## Project objectives

- Calculate each student's average score across Mathematics, Science, and English.
- Assign a grade based on the average score.
- Identify the highest-performing student.
- Compare average marks across subjects.
- Explore the relationship between daily study hours and average scores.
- Export summary reports and charts.

## Technologies used

- Python
- Pandas — data loading, cleaning, calculations, and summaries
- Matplotlib — data visualization

## Repository structure

```text
student-performance-analytics/
├── data/
│   └── student_performance.csv
├── outputs/
│   └── .gitkeep
├── src/
│   └── analyze.py
├── requirements.txt
└── README.md
```

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/manjeerab9-wq/student-performance-analytics.git
cd student-performance-analytics
```

### 2. (Optional) Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\\Scripts\\activate
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the analysis

```bash
python src/analyze.py
```

The script prints key findings in the terminal and saves its reports and charts in the `outputs/` folder.

## Dataset description

The sample dataset includes:

| Column | Description |
|---|---|
| student_id | Unique sample student identifier |
| gender | Student gender category in the sample |
| study_hours | Average study hours per day |
| attendance | Attendance percentage |
| math_score | Mathematics score |
| science_score | Science score |
| english_score | English score |

## Outputs

After running the script, the `outputs/` folder contains:

- `student_results.csv` — student scores, calculated averages, and grades.
- `subject_summary.csv` — average score for each subject.
- `grade_summary.csv` — number of students in each grade.
- `subject_averages.png` — bar chart comparing subject averages.
- `study_hours_vs_score.png` — scatter plot comparing study hours and average scores.

## Grading method

| Average score | Grade |
|---|---|
| 90–100 | A |
| 80–89.99 | B |
| 70–79.99 | C |
| 60–69.99 | D |
| Below 60 | F |

## Possible improvements

- Add more student records and explore larger datasets.
- Compare attendance with academic performance.
- Add filtering by subject or student group.
- Build an interactive dashboard using Streamlit.
- Add automated tests for the analysis functions.

## Author

**Manjeera Bavisetti**

GitHub: [@manjeerab9-wq](https://github.com/manjeerab9-wq)
