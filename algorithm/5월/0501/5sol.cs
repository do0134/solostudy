// HackerRank Between Two Sets

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
     * Complete the 'getTotalX' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER_ARRAY a
     *  2. INTEGER_ARRAY b
     */

    public static int getTotalX(List<int> a, List<int> b)
    {
        int answer = 0;
        HashSet<int> commonDivide = new HashSet<int>();
        
        for (int i = 1; i < 101; i++) {
            bool isCommonDivide = true;
            
            foreach (int bValue in b) {
                if (bValue % i != 0) {
                    isCommonDivide = false;
                    break;
                }
            }
            
            if (isCommonDivide) {
                commonDivide.Add(i);
            }
        }
        
        if (commonDivide.Count == 0) {
            return 0;
        }
        
        foreach (int commonValue in commonDivide) {
            bool isCommonMultiple = true;
            foreach (int aValue in a) {
                if (commonValue % aValue != 0) {
                    isCommonMultiple = false;
                    break;
                }
            }
            
            if (isCommonMultiple) {
                answer += 1;
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

        string[] firstMultipleInput = Console.ReadLine().TrimEnd().Split(' ');

        int n = Convert.ToInt32(firstMultipleInput[0]);

        int m = Convert.ToInt32(firstMultipleInput[1]);

        List<int> arr = Console.ReadLine().TrimEnd().Split(' ').ToList().Select(arrTemp => Convert.ToInt32(arrTemp)).ToList();

        List<int> brr = Console.ReadLine().TrimEnd().Split(' ').ToList().Select(brrTemp => Convert.ToInt32(brrTemp)).ToList();

        int total = Result.getTotalX(arr, brr);

        textWriter.WriteLine(total);

        textWriter.Flush();
        textWriter.Close();
    }
}
