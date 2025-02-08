以下是TestCaseViewer 应用程序的文档：

1. 这是一个本地运行的网页B/S应用程序。使用Flask框架，使用Vue.js框架。
2. 网页界面分为三个部分，顶部为工具条，左侧为主视图，右侧为属性视图。
3. 主视图用于显示一个树状结构。该树状结构用于显示一个表达式。
3.1 这个表达式只有两种运算符，分别是笛卡尔积和并集。
3.2 并集在树状结构中，表示为两个兄弟节点。
3.3 笛卡尔积，表达为父子节点。连续的笛卡尔积，表达为连续的父子节点。
3.4 兄弟节点上下扩展，父子节点左右扩展。
3.5 树状结构中，每个节点均可以展开和折叠。
3.6 表达式的primitive，称为“Param”。参数有一个参数名，和一个参数值列表。参数在图中以卡片的方式显示。
3.7 每个自表达式，在折叠后，均显示原始的表达式。比如，一个拥有多层子节点的表达式，折叠后应当显示为类似A*B+C*D的形式。
3.8 当鼠标悬停在折叠后的表达式的某个参数上时，应当有悬浮窗口，显示该参数的参数名和参数值列表。
3.9 每个表达式、和参数，都应当可以被选中。选中后，右侧属性视图应当显示选中节点的属性。
4. 表达式的模型类是Union和Cross，参数的模型类是Param。需要为他们生成对应的View或ViewModel类型供UI渲染。
5. 整个表达式，保存于一个.py文件中。具体的例子，请参考BlendTests.py。

# Installation

* Windows
    * MingW with GCC, CMake & Python with `venv` or `conda`
    * OR GCC + bat file, CMake might be changed for Windows environment.
* Install dependencies:
    * flask (`pip install` or `conda install`)

# How to run

1. Write the test plan in `pforge/plans/`.
2. Run `tgen.sh` to generate the test cases.
3. Run `python tview.py` to start the test case viewer.
   * You might be change the `current_test_file` in the script to test view different test plan.
   * It might be configurable in soon.
