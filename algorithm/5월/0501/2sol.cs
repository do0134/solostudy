// HackerRank Grading Student

using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

class Result
{

    /*
     * Complete the 'gradingStudents' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts INTEGER_ARRAY grades as parameter.
     */

    public static List<int> gradingStudents(List<int> grades)
    {
        List<int> answer = new List<int>();
        
        foreach (int grade in grades) {
            string gradeString = grade.ToString();
            string newGradeString = "";
            if (grade < 5) {
                newGradeString = "5";
            } else if (grade < 10) {
                newGradeString = "10";
            } else if (int.Parse(gradeString[gradeString.Length-1].ToString())<5) {
                newGradeString = gradeString[0] + "5";
            } else {
                int temp = int.Parse(gradeString[0].ToString()) + 1;
                newGradeString = temp.ToString() + "0";
            }
            
            int newGrade = int.Parse(newGradeString);
            if (newGrade < 40) {
                answer.Add(grade);
            } else if (newGrade - grade < 3) {
                answer.Add(newGrade);
            } else {
                answer.Add(grade);
            }
            
        }
        
        return answer;        
    }

}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int gradesCount = Convert.ToInt32(Console.ReadLine().Trim());

        List<int> grades = new List<int>();

        for (int i = 0; i < gradesCount; i++)
        {
            int gradesItem = Convert.ToInt32(Console.ReadLine().Trim());
            grades.Add(gradesItem);
        }

        List<int> result = Result.gradingStudents(grades);

        textWriter.WriteLine(String.Join("\n", result));

        textWriter.Flush();
        textWriter.Close();
    }
}
