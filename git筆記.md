‵git config --global user.name "name"     ‵           # name 是你的學號

git config --global user.email name@example.com     # name@example.com 是你的信箱

git clone [--]

git checkout [--]                                   # 切換至 [--] 分支

更動檔案

git status                                          # 紅字代表未 add 的檔案

git add -A                                          # add 全部更動的檔案         # -A 意即 --all

git status                                          # 綠字代表已 add 的檔案

git commit -m "message"                             # -m 意即快速提交

git push
