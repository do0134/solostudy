
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

    public static int answer = int.MaxValue;

    /*
     * Complete the 'formingMagicSquare' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts 2D_INTEGER_ARRAY s as parameter.
     */

    public static int formingMagicSquare(List<List<int>> s)
    {
        recur(0, 0, s, 0);
        return Result.answer;
    }

    public recur(int r, int c, List<List<int>> s, int cnt)
    {
        if (cnt > answer)
        {
            return;
        }

        int nr = r;
        int nc = c + 1;
        if (nc == 3)
        {
            nr = r + 1;
            nc = 0;
        }

        if (nr == 3)
        {
            if (check(s))
            {
                this.answer = Math.Min(answer, cnt);
            }
            return;
        }

        int temp = s[r][c];
        for (int i = 1; i < 10; i++)
        {
            s[r][c] = i;
            recur(nr, nc, s, cnt + Math.Abs(temp - i));
        }
        s[r][c] = temp;
    }

    public bool check(List<List<int>>s)
    {
        HashSet<int> set = new HashSet<int>();

        for (int i = 0; i < s.Count; i++) 
        {
            for (int j = 0;  j < s[i].Count; j++)
            {
                set.Add(s[i][j]);
            }
        }

        return set.Count == 9;

    }

}