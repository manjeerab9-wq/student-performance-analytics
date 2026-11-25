"""Analyze student scores and create summary reports and charts."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT_DIR / "data" / "student_performance.csv"
OUTPUT_DIR = ROOT_DIR / "outputs"

REQUIRED_COLUMNS = [
    "student_id",
    "study_hours",
    "attendance",
    "math_score",
    "science_score",
    "english_score",
]
SUBJECT_COLUMNS = ["math_score", "science_score", "english_score"]


def assign_grade(average: float) -> str:
    """Return a simple grade based on the student's average score."""
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def load_data() -> pd.DataFrame:
    """Load the CSV file and check that required columns are present."""
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found at {DATA_FILE}. "
            "Make sure data/student_performance.csv exists."
        )

    data = pd.read_csv(DATA_FILE)
    missing_columns = [column for column in REQUIRED_COLUMNS if column not in data.columns]

    if missing_columns:
        raise ValueError(f"Dataset is missing required columns: {missing_columns}")

    return data


def analyze_data(data: pd.DataFrame) -> pd.DataFrame:
    """Calculate each student's average score and grade."""
    result = data.copy()
    result["average_score"] = result[SUBJECT_COLUMNS].mean(axis=1)
    result["grade"] = result["average_score"].apply(assign_grade)
    return result


def save_summary(data: pd.DataFrame) -> None:
    """Save key performance summaries as CSV files."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    subject_summary = data[SUBJECT_COLUMNS].mean().rename("average_score")
    subject_summary.to_csv(OUTPUT_DIR / "subject_summary.csv")

    grade_summary = data["grade"].value_counts().sort_index().rename_axis("grade")
    grade_summary.to_csv(OUTPUT_DIR / "grade_summary.csv")

    data.sort_values("average_score", ascending=False).to_csv(
        OUTPUT_DIR / "student_results.csv", index=False
    )


def create_charts(data: pd.DataFrame) -> None:
    """Create and save two charts for the project."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Chart 1: Average score in each subject
    subject_averages = data[SUBJECT_COLUMNS].mean()
    subject_names = ["Mathematics", "Science", "English"]

    plt.figure(figsize=(8, 5))
    plt.bar(subject_names, subject_averages.values)
    plt.title("Average Score by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Average Score")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "subject_averages.png", dpi=150)
    plt.close()

    # Chart 2: Study hours compared with average score
    plt.figure(figsize=(8, 5))
    plt.scatter(data["study_hours"], data["average_score"])
    plt.title("Study Hours vs Average Score")
    plt.xlabel("Study Hours per Day")
    plt.ylabel("Average Score")
    plt.ylim(0, 100)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "study_hours_vs_score.png", dpi=150)
    plt.close()


def main() -> None:
    data = load_data()
    results = analyze_data(data)
    save_summary(results)
    create_charts(results)

    print("\nSTUDENT PERFORMANCE ANALYSIS")
    print("-" * 32)
    print(f"Number of students: {len(results)}")
    print(f"Class average: {results['average_score'].mean():.2f}")
    print(f"Average attendance: {results['attendance'].mean():.2f}%")

    top_student = results.loc[results["average_score"].idxmax()]
    print(
        "Top student: "
        f"{top_student['student_id']} "
        f"({top_student['average_score']:.2f} average)"
    )

    print("\nAverage score by subject:")
    print(results[SUBJECT_COLUMNS].mean().round(2).to_string())
    print(f"\nReports and charts saved in: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
