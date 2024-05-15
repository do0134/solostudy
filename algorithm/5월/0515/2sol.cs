// HackerRank Sales by Match

public static int sockMerchant(int n, List<int> ar)
{
    int answer = 0;
    HashSet<int> numSet = new HashSet<int>();

    foreach (int i in ar)
    {
        if (numSet.Contains(i))
        {
            numSet.Remove(i);
            answer += 1;
        }
        else
        {
            numSet.Add(i);
        }
    }

    return answer;
}