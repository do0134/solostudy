// 백준 25374 등급 계산하기
using System.Collections;

int n = int.Parse(Console.ReadLine());
string[] ss = Console.ReadLine().Split(' ');

List<int> scores = new List<int>();
foreach (string s in ss)
{
    scores.Add(int.Parse(s));
}

scores = scores.OrderByDescending(x => x).ToList();

List<int> grade = new List<int> { 4, 11, 23, 40, 60, 77, 89, 96, 100 };

int[] answer = new int[9];

int idx = 0;
int prev = -1;
int cnt = 0;
int total = 1;

foreach (int s in scores)
{
    if (prev == -1)
    {
        cnt++;
        total++;
        prev = s;
    }
    else if (prev == s)
    {
        cnt++;
        total++;
        prev = s;
    }
    else if (total > grade[idx])
    {
        answer[idx] = cnt;
        while (idx < 9 && grade[idx] < total)
        {
            idx += 1;
        }

        cnt = 1;
        prev = s;
        total++;
    }
    else
    {
        cnt++;
        total++;
        prev = s;
    }
}
if (answer.Sum() != n)
{
    answer[idx] = n - answer.Sum();
}

foreach (int i in answer)
{
    Console.WriteLine(i);
}