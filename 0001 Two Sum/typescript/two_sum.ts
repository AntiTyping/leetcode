function twoSum(nums: number[], target: number): number[] {
    const complements: Record<number,number> = {};

    for (const [index, num] of nums.entries()) {
        const complement = target - num;
        if (complement in complements) {
            return [complements[complement], index];
        } else {
            complements[num] = index;
        }
    }
};