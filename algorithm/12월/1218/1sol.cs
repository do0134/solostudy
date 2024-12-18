// 5567 결혼식

using System.Collections;

int n = int.Parse(Console.ReadLine());
int m = int.Parse(Console.ReadLine());

Dictionary<string, HashSet<string>> friends = new Dictionary<string, HashSet<string>>();
friends["1"] = new HashSet<string>();

for (int i = 0; i < m; i++)
{
    string[] inputs = Console.ReadLine().Split(' ');
    if (!friends.ContainsKey(inputs[0]))
        friends[inputs[0]] = new HashSet<string>();
    if (!friends.ContainsKey(inputs[1]))
        friends[inputs[1]] = new HashSet<string>();
    friends[inputs[1]].Add(inputs[0]);
    friends[inputs[0]].Add(inputs[1]);
}

HashSet<string> answer = new HashSet<string>();
answer.Add("1");

foreach (string f in friends["1"])
{
    answer.Add(f);
    foreach (string f2 in friends[f])
    {
        answer.Add(f2);
    }
}

Console.WriteLine(answer.Count - 1);