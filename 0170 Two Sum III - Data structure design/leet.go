type TwoSum struct {
    comp map[int]int
}


func Constructor() TwoSum {
    return TwoSum{
        make(map[int]int),
    }
}


func (this *TwoSum) Add(number int)  {
    this.comp[number]++
}


func (this *TwoSum) Find(value int) bool {
    // O(n)
    for k, _ := range this.comp {
        diff := value - k
        // O(1)
        if val, ok := this.comp[diff]; ok == true {
            if diff == k {
                if val > 1 {
                    return true
                }
            } else {
                return true
            }
        }
    }
    return false
}


/**
 * Your TwoSum object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(number);
 * param_2 := obj.Find(value);
 */