# 挿入ソート（insertion sort）

"""
挿入ソート（insertion sort）
人がトランプの並べ替えなどで自然と行うようなアルゴリズム
「任意の要素を適切な位置に挿入する」という操作を繰り返す
"""


def insertion_sort(a: list):
    """挿入ソート（insertion sort）

    最初に列の先頭のみを整列済み部分と呼ぶことにする。

    1. 「適切な位置への挿入」の手順を行う
    2. 挿入された要素も含めて整列済み部分とし、1.に戻る

    整列済み部分が列全体に達したら停止する
    """
    for i in range(len(a)):
        target = a[i]
        

def insert(a):
    
