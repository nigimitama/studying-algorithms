

## グラフの探索アルゴリズム

### 幅優先探索（breadth first search）

- まず、根ノードに隣接した全てのノードを探索する。それからこれらの最も近いノードのそれぞれに対して同様のことを繰り返して探索対象ノードをみつける。
- 幅優先探索は解を探すために、グラフの全てのノードを網羅的に展開・検査する。
  - 最良優先探索とは異なり、ノード探索にヒューリスティクスを使わずに、グラフ全体を目的のノードがみつかるまで、目的のノードに接近しているかどうかなどは考慮せず探索する。



#### 最良優先探索（best-first search）

- 幅優先探索を拡張し、最も望ましいノードを選択するようにしたもの
- [最良優先探索 - Wikipedia](https://ja.wikipedia.org/wiki/%E6%9C%80%E8%89%AF%E5%84%AA%E5%85%88%E6%8E%A2%E7%B4%A2)
  - [ダイクストラ法 - Wikipedia](https://ja.wikipedia.org/wiki/%E3%83%80%E3%82%A4%E3%82%AF%E3%82%B9%E3%83%88%E3%83%A9%E6%B3%95)



### 深さ優先探索（depth-first search）

- 根ノードから子ノードへとどんどん深く探索していき、行き着いたらバックトラック（一歩逆戻り）して別のノードを探索する
- [深さ優先探索 - Wikipedia](https://ja.wikipedia.org/wiki/%E6%B7%B1%E3%81%95%E5%84%AA%E5%85%88%E6%8E%A2%E7%B4%A2)









## コンテスト

[AtCoder Typical Contest 001](https://atcoder.jp/contests/atc001/tasks)

- 深さ優先探索、union-find、高速フーリエ変換について出題されている

#### union-find

https://pyteyon.hatenablog.com/entry/2019/03/11/200000
https://atcoder.jp/contests/atc001/tasks/unionfind_a


