// HackerRank Climbing the Leaderboard

namespace _0518
{
    public class _1sol
    {
        public static List<int> climbingLeaderboard(List<int> ranked, List<int> player)
        {
            PriorityQueue<int, int> rankPriority = new PriorityQueue<int, int>();
            PriorityQueue<int, int> playerPriority = new PriorityQueue<int, int>();

            HashSet<int> rankHash = new HashSet<int>(ranked);

            foreach (int i in rankHash)
            {
                rankPriority.Enqueue(i, -i);
            }

            for (int i = 0; i < player.Count; i++)
            {
                playerPriority.Enqueue(i, -player[i]);
            }

            int[] answer = new int[player.Count];

            int rank = 1;

            while (playerPriority.Count > 0)
            {
                int now = playerPriority.Dequeue();

                if (rankPriority.Count > 0 && rankPriority.Peek() > player[now])
                {
                    while (rankPriority.Count > 0 && rankPriority.Peek() > player[now])
                    {
                        rankPriority.Dequeue();
                        rank += 1;
                    }
                }
                else if (rankPriority.Count > 0 && player[now] >= rankPriority.Peek())
                {
                    answer[now] = rank;
                }
                answer[now] = rank;

            }


            return answer.ToList<int>();
        }
    }
}
