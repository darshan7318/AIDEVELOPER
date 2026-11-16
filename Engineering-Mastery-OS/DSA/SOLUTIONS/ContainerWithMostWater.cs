// Two Pointers canonical solution: Container With Most Water
// LeetCode #11
using System;

namespace EngineeringMastery.DSA.Solutions
{
    public static class ContainerWithMostWater
    {
        public static int MaxArea(int[] height)
        {
            if (height == null || height.Length < 2) return 0;

            int left = 0;
            int right = height.Length - 1;
            int maxArea = 0;

            while (left < right)
            {
                int h = Math.Min(height[left], height[right]);
                int width = right - left;
                int area = h * width;

                if (area > maxArea)
                {
                    maxArea = area;
                }

                // Invariant: Move the pointer with the smaller height to search for a taller wall
                if (height[left] < height[right])
                {
                    left++;
                }
                else
                {
                    right--;
                }
            }

            return maxArea;
        }
    }
}
