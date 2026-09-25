function subsets(nums: number[]): number[][] {
    var ans = []
    var curr = []

    const bt = (start: number) => {
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