function subsets(nums: number[]): number[][] {
    const ans: number[][] = []
    const curr: number[] = []

    const bt = (start: number): void => {
        ans.push([...curr])

        for (let i = start; i < nums.length; i++) {
            curr.push(nums[i])
            bt(i + 1)
            curr.pop()
        }
    }

    bt(0)

    return ans;
};