tk_app_dev
====

tkinterでGUIアプリを作成する練習

Usage
---
`./tk_app_base.py`

description
---

### tkinterの階層構造

- root ： 下地みたいなもの。ここになんでも置けるが、Frameを置くものと割り切っておくと整理しやすい。
    - Frame ： 各種ウィジェットのまとまり。決まった形のものを作っておいて、それを並べていくようにすると整理しやすい。
        タブを作ったり、ラベルとボタンのまとまりを作ったりすることがよくある。Frameは入れ子にできる。
        - Label
        - Entry
        - Button
        - etc

Tweet
---
- コーディングの簡略化を考えて、最初はあれもこれもclass化しようとしたが、柔軟なレイアウトを考えると、rootの配置の仕方はべた書きにしたほうが簡単に書けるような気がしてきた。
こまごました部品だけclassにしてしまったほうが効率が良いと思う。


Licence
---

[MIT](https://github.com/shka86/foo/blob/master/LICENCE)

Author
---

[shka86](https://github.com/shka86)
