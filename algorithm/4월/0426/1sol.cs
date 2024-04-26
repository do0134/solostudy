// HackerRank Array - DS

public static List<int> reverseArray(List<int> a)
{
    List<int> answer = new List<int>();

    for (int i = a.Count-1; i >= 0; i--)
    {
        answer.Add(a[i]);
    }

    return answer;
}