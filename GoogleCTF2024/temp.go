package main

import (
	"fmt"
)
type StockSpanner struct {
    St Stack[Pair]
}

type Pair struct {
	X int
	Y int
}

func Constructor() StockSpanner {
    var St Stack[Pair]
    return StockSpanner{
        St: St,
    }
}

func (this *StockSpanner) Next(price int) int {
    st := this.St
    if st.Empty() || price < st.Seek().X {
        st.Push(Pair{
            X: price,
            Y: 1,
        })
        return 1
    }
    res := 1
    for !st.Empty()&& price >= st.Seek().X{
        res += st.Pop().Y
    }
    st.Push(Pair{
            X: price,
            Y: res,
        })
        return res
}
func main() {
	fmt.Println("Hello World")
}
