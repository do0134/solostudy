// HackerRank Number Line Jumps

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
     * Complete the 'kangaroo' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts following parameters:
     *  1. INTEGER x1
     *  2. INTEGER v1
     *  3. INTEGER x2
     *  4. INTEGER v2
     */

    public static string kangaroo(int x1, int v1, int x2, int v2)
    {   
        string bigger;
        if (x1 > x2) {
            bigger = "x1";
        } else if (x1 < x2) {
            bigger = "x2";
        } else {
            return "YES";
        }
        
        if (x1 != x2 & (v1 == 0 | v2 == 0)) {
            return "NO";
        } else if (x1 != x2 & v1 == v2) {
            return "NO";
        }
        
        int diff = x1-x2;
        if (diff < 0) {
            diff *= -1;
        }
        
        while (true) {
            x1 += v1;
            x2 += v2;
            
            if (x1 == x2) {
                return "YES";
            }
            
            if (x1 > x2 & bigger == "x2") {
                return "NO";
            } else if (x2 > x1 & bigger == "x1") {
                return "NO";
            }
            
            if (diff < x1-x2 | diff < (x1-x2)*-1) {
                return "NO";
            }
        }
    }

}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        string[] firstMultipleInput = Console.ReadLine().TrimEnd().Split(' ');

        int x1 = Convert.ToInt32(firstMultipleInput[0]);

        int v1 = Convert.ToInt32(firstMultipleInput[1]);

        int x2 = Convert.ToInt32(firstMultipleInput[2]);

        int v2 = Convert.ToInt32(firstMultipleInput[3]);

        string result = Result.kangaroo(x1, v1, x2, v2);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
