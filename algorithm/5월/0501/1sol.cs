// HackerRank Time Conversion

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
     * Complete the 'timeConversion' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING s as parameter.
     */

    public static string timeConversion(string s)
    {
        bool IsAm = s.Contains("AM");
        
        if (IsAm) {
            s.Replace("AM", "");
        } else {
            s.Replace("PM", "");
        }
        
        Range HourRange = 0..2;
        string hour = s[HourRange];
        Range MinuteRange = 3..5;
        string minute = s[MinuteRange];
        Range SecondRange = 6..8;
        string second = s[SecondRange];
        
        string answer = "";
        
        if (!IsAm & hour != "12") {
            int newHour = int.Parse(hour) + 12;
            answer += newHour.ToString();
        } else if (hour == "12" & IsAm) {
            answer += "00";
        } else {
            answer += hour;
        }
        
        answer += ":";
        
        return answer + minute + ":" + second;
        
        
        return hour; 
    }

}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        string s = Console.ReadLine();

        string result = Result.timeConversion(s);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
