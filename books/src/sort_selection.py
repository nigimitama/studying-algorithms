# 選択ソート（selection sort）

def minimize(a: list):
    """最小値を探すアルゴリズム
    - 隣り合う整数を比較し、トーナメント戦のように最小値が勝ち進んでいくような比較をする（計算回数＝n(n-1)/2回）
    """
    for i in range(len(a)):
        if i == 0:
            min_x = a[i]
        else:
            if a[i] < min_x:
                min_x = a[i]
    return min_x


def selection_sort(a: list):
    """選択ソート（selection sort）

    1. ソート対象の列の中から最小値を見つけ，その値と先頭を交換する
    2. 先頭を除いた残りの列をソート対象とし，1．に戻る
       ソート対象の列の要素が1 個になったら停止する 
    
    比較回数：1+2+...+(n-1) = n(n-1)/2
    最小値を先頭に交換する回数：n-1回
    """
    for i in range(len(a)):
        target = a[i:]
        if len(target)== 1:
            break
        else:
            min_ = minimize(target)
            a[a.index(min_)] = a[i]
            a[i] = min_
    return a



def selection_sort2(a: list):
    """選択ソートの随時交換版
    「先頭との交換を，最小値を求めた後ではなく，先頭より小さい数が見つかるたびに行う」という方針に変更したもの

    計算回数の最小値同士で比較すると随時交換版のほうが少なくなり、計算回数の最大値すなわち最悪計算量（worst case complexity）で比較すると選択ソートのほうが少なくなる。
    """
    for i in range(len(a)):
        target = a[i:]
        if len(target)== 1:
            break
        else:
            for j in range(len(target)):
                if target[j] < a[i]:
                    a[a.index(target[j])] = a[i]
                    a[i] = target[j]
    return a


if __name__ == "__main__":
    a = [4,5,2,1,3]
    selection_sort(a)
    selection_sort2(a)
