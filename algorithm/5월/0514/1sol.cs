// 프로그래머스 가장 많이 받은 선물

using System;
using System.Collections.Generic;

public class Solution
{
    public int solution(string[] friends, string[] gifts)
    {
        int answer = 0;
        Dictionary<string, Dictionary<string, int>> FriendDict = new Dictionary<string, Dictionary<string, int>>();
        Dictionary<string, int> GiftNo = new Dictionary<string, int>();
        Dictionary<string, int> forAnswer = new Dictionary<string, int>();

        foreach (string friend in friends)
        {
            GiftNo.Add(friend, 0);
            FriendDict.Add(friend, new Dictionary<string, int>());
            forAnswer.Add(friend, 0);
            foreach (string fr in friends)
            {
                if (fr != friend)
                {
                    FriendDict[friend].Add(fr, 0);
                }

            }
        }

        foreach (string gift in gifts)
        {
            string[] doGift = gift.Split(' ');
            string sender = doGift[0];
            string giver = doGift[1];

            FriendDict[sender][giver] += 1;
            GiftNo[sender] += 1;
            GiftNo[giver] -= 1;
        }

        for (int i = 0; i < friends.Length; i++)
        {
            for (int j = i + 1; j < friends.Length; j++)
            {
                string a = friends[i];
                string b = friends[j];
                if (FriendDict[a][b] > FriendDict[b][a])
                {
                    forAnswer[a] += 1;
                }
                else if (FriendDict[a][b] < FriendDict[b][a])
                {
                    forAnswer[b] += 1;
                }
                else
                {
                    if (GiftNo[a] < GiftNo[b])
                    {
                        forAnswer[b] += 1;
                    }
                    else if (GiftNo[a] > GiftNo[b])
                    {
                        forAnswer[a] += 1;
                    }
                    else
                    {
                        continue;
                    }
                }
            }
        }

        foreach (string friend in friends)
        {
            if (forAnswer[friend] > answer)
            {
                answer = forAnswer[friend];
            }
        }

        return answer;
    }
}