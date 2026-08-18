def backtrack():

    if 满足结束条件:
        保存答案
        return

    for 每一种选择:

        做选择

        backtrack()

        撤销选择

Backtracking = DFS + Undo（恢复现场）。
