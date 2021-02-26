
import numpy as np
import pandas as pd


def calculate_averages(gradebook):
    # calculate the averages of each assignment type in the gradebook using pandas groupby and mean methods
    averages = None
    # round the averages to 2 decimal places using the pandas loc and numpy round() methods

    df_i = gradebook.groupby("Assignment Type").mean()
    # just round the whole array, god is dead
    df = np.round(df_i, decimals=2)

    homework = df.loc["Homework", "Assignment Grade"]
    quiz = df.loc["Quiz", "Assignment Grade"]
    exam = df.loc["Exam", "Assignment Grade"]

    # return the three averages  
    return homework, quiz, exam


def high_performers(gradebook):
    # Calculate the highest performing student for exam 1 and the final exam using pandas groupby and idxmax methods
    best_students = None
    df = gradebook.groupby("Assignment Name").idxmax()["Assignment Grade"]
    e1 = gradebook.iloc[df["E1"]]["Name"]
    # Get the highest performers for the two exams using pandas iloc method
    final = gradebook.iloc[df["Final Exam"]]["Name"]
    # return the student names in the order Exam 1 high performer, Final Exam high performer .
    return e1, final


def main():
    # DO NOT MODIFY THIS CODE

    # read in the data 
    filename = input('filename?\n')
    gradebook = pd.read_csv(filename,encoding='utf-8')

    # analyze the data:
    homework, quiz, exam = calculate_averages(gradebook)
    e1, final = high_performers(gradebook)

    # print the averages and high scorers
    print('Homework Average:', homework)
    print('Quiz Average:', quiz)
    print('Exam Average:', exam)
    print()
    print('E1 High Score:', e1)
    print('Final Exam High Score:', final)
    return


if __name__ == '__main__':
    main()
