﻿using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

public class Solution
{
    public static void Main(string[] args)
    {
        Console.WriteLine(solution(new[] { 4, 3, 2, 1, 5 }, new[] { 1, 0, 0, 0, 1 }));
    }

    public static int solution(int[] A, int[] B)
    {
        Stack<int> upstreamQueue = new Stack<int>(); // 0's
        Stack<int> downstreamQueue = new Stack<int>(); // 1's

        for (int i = 0; i < A.Length; i++)
        {
            if (B[i] == 0)  // is upstream              
            {
                if (downstreamQueue.Count > 0) // there is fish to eat
                {
                    while (downstreamQueue.Count > 0 && downstreamQueue.Peek() < A[i])
                    {
                        downstreamQueue.Pop();
                    }

                    if (downstreamQueue.Count == 0)
                    {
                        upstreamQueue.Push(A[i]);
                    }
                }
                else
                {
                    upstreamQueue.Push(A[i]);
                }
            }
            else // is downstream
            {
                downstreamQueue.Push(A[i]);
            }
        }

        return upstreamQueue.Count + downstreamQueue.Count;
    }
}

// tests


