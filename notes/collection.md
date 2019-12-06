# Collection

[特集！知らないと損をする計算量の話 - Qiita](https://qiita.com/drken/items/18b3b3db5735241465ef)



- listは検索（`"hoge" in List`）するとき$O(n)$
- setは検索するとき$O(1)$

- listでsortすると、要素数の分だけ計算量かかる
- heapq（ヒープキュー、優先度つきキュー）で保持すると、最小値や最大値しか取り出せないが、頻繁に最小値や最大値を参照するときはlistで保持して毎回sortするより効率がいい（[ABC141D - Powerful Discount Tickets](https://atcoder.jp/contests/abc141/tasks/abc141_d)）


