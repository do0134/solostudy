// HackerRank Subarray Division

public static int birthday(List<int> s, int d, int m)
{
    int n = s.Count;
    int answer = 0;

    for (int i = 0; i < n; i++)
    {
        int temp = s[i];
        for (int j = i + 1; j < Math.Min(n, i + m); j++)
        {
            temp += s[j];
        }

        if (temp == d)
        {
            answer++;
        }
    }

    return answer;
}