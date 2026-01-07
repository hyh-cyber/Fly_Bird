## 计划概述
将当前目录下的所有文件上传到指定的GitHub仓库 `https://github.com/hyh-cyber/Fly_Bird`

## 实施步骤
1. **更新远程仓库地址**：将当前远程仓库地址从默认值修改为目标GitHub仓库地址
2. **添加所有文件到暂存区**：包括新文件和已修改的文件
3. **提交更改**：创建一个新的提交，包含所有文件
4. **推送到远程仓库**：将本地提交推送到GitHub仓库的master分支

## 具体命令
```bash
# 更新远程仓库地址
git remote set-url origin https://github.com/hyh-cyber/Fly_Bird

# 添加所有文件到暂存区
git add .

# 提交更改
git commit -m "上传所有项目文件"

# 推送到远程仓库
git push -u origin master
```

## 预期结果
- 所有文件（答辩PPT、项目APP、项目工程、项目文档等）将被上传到指定的GitHub仓库
- 远程仓库地址将被更新为目标地址
- 所有更改将被提交并推送到master分支