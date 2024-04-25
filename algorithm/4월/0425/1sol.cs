// 프로그래머스 음양 더하기

using System;

public class Solution {
    public int solution(int[] absolutes, bool[] signs) {
        int answer = 0;
        int max_idx = absolutes.Length;

        for (int i = 0; i < max_idx; i++)
        {
            if (signs[i] == false)
                answer -= absolutes[i];
            else
                answer += absolutes[i];
        }

        return answer;
    }
}