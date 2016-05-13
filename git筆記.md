=========================== 更動檔案前 ===========================
設定 git config
`git config --global user.name "name"
git config --global user.email name@example.com`

`git clone [--]`

`git checkout [--]`                                   <tab> 切換至 [--] 分支

=========================== 更動檔案後 ===========================

`git status`                                          <tab> 紅字代表未 add 的檔案

`git add -A`                                          <tab> add 全部更動的檔案         # -A 意即 --all

`git status`                                          <tab> 綠字代表已 add 的檔案

`git commit -m "message"`                             <tab> -m 意即快速提交

`git push`
