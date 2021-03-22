# GIT 使用概述

为什么要使用版本控制？
1. 多人协同开发
2. 保留修改的历史记录，方便回退版本，尤其是当代码出现bug时

版本控制：可以解决多人协同开发，也可以保留修改的历史记录

分布式：每台本地电脑都保存有代码的全部备份
集中式：只有中央服务器保留有代码的全部备份

git-->分布式

## 安装

LINUX:Ubuntu为例
`$ sudo apt-get install git`

windows:      
直接官网下载并安装           
[下载地址](https://git-scm.com/)  
建议不要使用图形版，因为难以看懂       
更新：`git update-git-for-windows`       
ps:不翻墙容易出错

## 基本概念  
1. 工作区：写代码的文件夹  
2. 版本库：  
   + 暂存区：暂时存放修改好的代码
   + 代码库：确定修改好之后的代码就可以提交到代码库
   + 远程仓库：把代码存放在云端
      - github(国外)
      - gitee(国内)

# 本地操作

基本流程:     
在文件夹创建仓库 --> 在工作区编写文件，包括文件的增删改 --> 把修改提交到暂存区 --> 把暂存区的修改提交到仓库 --> 提交到云端

## 创建仓库

1. 新建文件夹test
2. linux输入git init --> ls -l -->可以发现新创建了一个.git文件夹
3. windows右键-->git bash here-->git init-->创建了一个.git文件夹(默认隐藏)

*注意：是在当前工作目录创建，可用pwd命令查看*

## 创建版本

1. 新建一个文本文件test.txt
2. git add test.txt
3. git commit -m 'version0.1'  --> 起一个有意义的内容
4. git log --> 查看版本记录 --> 可以发现commit后有版本信息
5. 修改test.txt内容
6. git add test.txt
7. git commit -m 'version0.2' --> 有两个版本

git记录的是修改的内容，后面的版本依赖于前面的版本
![描述1](image/1.png)

## 查看版本

    git log
    git log --graph        # 图形化查看
    git log --graph --pretty=format:"%h %s"   # 指定格式查看
    git log --pretty=oneline --graph     # 指定格式查看，显示简易内容

## 版本回退

1. 创建好一个新的版本后，默认会有一个HEAD指向当前版本
![HEAD](image/2.png)

2. HEAD之前版本的表示方法：
第一种方法：HEAD^-->前一个版本；HEAD^^-->前两个版本
第二种方法：HEAD~1-->前一个版本；HEAD~100-->前100个版本

3. git reset --hard HEAD^ --> 回到版本1，即指针指向了版本1
![版本回退](image/3.png)   
git log 查看版本信息，可以看到只有一个版本，但是版本2并没有删掉
记住：--hard是将已经commit的记录回退

4. 如何回到版本2？此时已无法使用HEAD，HEAD只可以用于之前的版本回退
使用版本号来回退，版本好就是git log后出现的commit后面的内容
版本号很长，用前几个即可  
`git reset --hard [版本号]`

![版本回退](image/4.png)

这个过程很快，只是把HEAD移动到版本2处

**当HEAD在版本1时，如何查看其他版本的版本号(commit号)?**      
      
git reflog --> 查看操作记录，最前面一栏即为版本号

## 工作区与暂存区

文件所在的文件夹即为工作区，即git init的文件夹        
该文件夹中的.git目录为git的版本库，其中最重要的就是称为stage/index的暂存区           
默认的分支为master分支，在git2.23版本以后默认分支改为main分支              

**工作区与暂存区的关系如下图：**
![工作区与暂存区](image/5.png)

*可以多次add，然后一次性commit*          
add的作用就是把修改放入到暂存区中   
commit的就是一次性把暂存区的所有修改记录放入版本库中         

查看工作区的状态`git status`
如果对工作区的文件进行了修改，就可以知道哪些文件被修改，新增了哪些（显示未跟踪）     
注意：git add后可以加多个文件，也可以加目录，即可以把整个目录的修改都保存           
比较常用的有`git add .`即把当前目录的修改都放入暂存区            
一旦提交后，如果你又没有对工作区做任何修改，那么工作区就是“干净的”         

**注意：如果修改文件后，不用add将修改放入暂存区，commit的时候就不会记录该修改**            
也就是说，commit只记录暂存区的修改，任何没有加入到暂存区的修改都不会被记录            

## 丢弃改动

1. 尚未add(放入暂存区)及commit(放入版本库)丢弃改动：`git checkout -- [文件名]`

2. 如果已经把改动后的加入到暂存区，就需要以下命令来取消暂存`git reset HEAD [文件名]`
  
通过`git status`可以发现文件已经被取消暂存，可以用git checkout来放弃改动

## 对比文件

对比工作区和某个版本文件的不同   
`git diff HEAD -- [文件名(工作区中的文件)]`

1. 减号（－）对应着HEAD文件
2. 加号（＋）对应着工作区中的文件
3. 没有加号或减号的表示两个文件共有的

最下面的＋表示工作区中的文件比版本库中的文件多出的内容，如果是减号则相反         

**对比两个版本之间的不同**         
如对比HEAD与HEAD^的不同         
`git diff HEAD HEAD^ -- [文件名]`

## 删除文件

在工作的增、删、改都属于改动范畴      
在工作区中删除某个文件后，可以使用git checkout来丢弃修改          

如果确实删除文件，先删除文件，然后使用如下命令         
`git rm [文件名]`  
把删除修改添加到暂存区       
`git commit -m '说明'`        

*如何以简短的方式显示版本记录？*
git log --pretty=oneline

## 分支

在开发过程中，通常是一边运营一边修改，在项目上线之后，主分支(master/main)分支运行的是稳定版本，一般不动  
这时要新增或删除功能怎么办？  
这个时候就需要分支功能，在主分支之外新建一个分支来继续开发，待测试稳定再合并入主分支  

1. 查看分支：`git branch`
2. 创建并切换分支：`git checkout -b dev`，再次查看分支(git branch)可以看到有两个分支              

建议：使用git2.23以后版本使用的swich命令可以区分checkout的不同，因为checkout也可以表示取消修改  

本质上，分支是创建了一个新的指针，不影响原指针的位置         
把HEAD指针指向新创建的分支上         
此后，所有的修改操作均在新分支上进行，不会对原纪录产生任何影响
查看：git log --pretty=oneline

**切换分支**   
`git checkout master`   
直接让HEAD重新指向master

在git的2.23版本以后，切换分支可以使用switch   
`git switch <分支名> # 切换分支 `   
`git switch -c <分支名> # 创建并切换分支`  
可以把-c理解为create  

**合并操作**   
`git merge dev`
记住：在合并之前把当前分支切换到主分支上，然后把dev分支上的内容合并到master分支上 
快速合并(fast-forward)，把master指针连同HEAD指向dev的位置   
可以使用快速合并时默认使用快速合并

合并之后可以删除dev分支        
`git branch -d dev`   
即直接删除dev的指针  

![分支流程](image/6.png)
![分支流程](image/7.png)
![分支流程](image/8.png)
![分支流程](image/9.png)

### 冲突

冲突的产生：两个分支都对**同一个文件**进行了修改并提交就会出现冲突   
如果对不同的文件进行修改不会产生冲突   
![冲突产生](image/10.png)  
如果执行git merge dev就会报错，并指出哪个文件发生了冲突   
git status也会指出冲突发生的位置   

**解决方法**
打开产生冲突的文件，可以看到冲突的内容   
然后对其进行修改并提交，产生一个新的版本即可解决冲突   
![解决冲突](image/11.png)   

查看分支图`git log --graph --pretty=oneline`

### 分支管理策略

快速合并时，直接移动指针          
有时，快速合并不能成功，但是又没有冲突，这时合并会做一次新的提交       
但是这种模式下删除分支后会丢掉分支的信息          

例：
1. 创建并切换分支dev
2. 在dev上创建新的文件并提交
3. 切换master分支并修改文件，然后提交
4. 此时git merge dev无法实现快速合并
5. 出现弹窗后提示输出信息
6. 这个界面表示git做了一次新的提交，而不是快速合并

有时需要禁用fast-forward来保存dev分支的记录！   
`git merge --no-ff -m '说明信息' dev`  
对比一下默认的快速合并模式   
`git merge dev`

### bug分支

遇到BUG时，新建一个bug临时分支，修复之后合并到master分支，然后删除bug分支         

场景：
1. 当前正在dev分支上进行开发，但是软件运行过程中发现bug需要立即修复
2. 因当前dev分支上的开发工作尚未完成无法提交

`git stash  --> 保存当前工作区`   
`git status  --> 发现工作区干净了`

操作流程：

    回到master分支并创建一个临时bug分支
    git checkout master
    git checkout -b bug-001
    修复bug之后
    git add [文件名]
    git commit -m '修复bug001'
 
    回到master分支并合并，需要禁用ff
    git checkout master
    git merge --no-ff -m '修复bug001' bug-001  --> 删除bug-001后不会丢 信息

    回到dev
    git checkout dev
    git status  --> 发现是干净的
    git stash list --> 列出保存的工作区
    如何回复工作现场
    git stash pop

`git stash`保存的是当前工作的分支  

## rebase变基 --可选操作//TODO

rebase使得git记录简洁

git log容易变得冗长

把某些记录整合成一条
`git rebase -i <版本号x> --> 即把当前的记录到版本号x之间进行合并`
`git rebase -i <HEAD~X> --> 如果x=3，即把当前记录到版本3之前进行合并`

注意：合并记录时，不要合并已经push到远程仓库的记录

# 远程操作 

远程操作作用：备份，共享

`gitignore:在github中，选择某一语言，会自动创建需要忽略跟踪的文件`

## 配置git

项目的配置：.git文件夹中的config文件

1. 查看配置：`git config --list`
2. 设置用户名：`git config --global user.name 'xxx'`
3. 设置用户名邮箱：`git config --global user.email 'xxx@xx.com'`
4. 设置远程推送网址：`git remote add <url>`

以上的global均可以换成local，此时这些配置只对当前文件夹有效

## ssh模式 --> 可选

把本机ssh公钥保存至github账户中      

如何生成ssh公钥？       
linux中：
1. 进入用户家目录编辑.gitconfig，即git的配置文件，里面保存了github账户名和邮箱地址
2. 执行命令ssh-keygen -t rsa -C '邮箱地址'
该命令生成一个文件夹.ssh，其中有三个文件：id_rsa、id_rsa.pub、known_hosts        
其中id_rsa是私钥自己保留，id_rsa.pub是公钥          
把公钥内容复制到github中              

## 克隆项目

克隆一个项目就是下载云端的代码库  
`git clone [ssh方式/HTTPS方式]`   
该命令会在当前目录下新建一个目录，把内容全部放在新目录中  

克隆出错执行下面的命令(linux)  
`eval "$(ssh-agent -s)"`   
`ssh-add`   

## 上传分支

通常不在master分支上进行开发，新建一个自己的分支进行开发          
先在本机上进行开发并提交版本           

**推送至github**  
`git push origin [分支名称]`  
例：git push origin dev  
*origin代表的是远程分支*  
如果远程没有dev分支，则新建一个   

*将本地分支跟踪远程分支*  
跟踪之后，本地提交与远程的不一样会有提示  
`git branch --set-upstream-to=origin/dev dev`  
这里的最后一个dev与前面的origin/dev分别代表本地分支和远程分支  
`git status`  

*跟踪之后，使用git push后面不用加远程分支名*        

如果push报错：修改.git/config文件           
将

    [remote "origin"]
    url = "https://github.com/用户名/仓库名.git

修改为

    [remote "origin"]
    url = "https://用户名:密码@github.com/用户名/仓库名.git

## 远程分支拉取代码

`git pull origin dev  --> 从dev分支拉取代码，并合并到本地所在分支`

# github

*github基本概念：*
1. repository:仓库
2. star:收藏
3. fork:复制克隆项目-->将别人的仓库完整复制到自己的仓库中，标记为forked from xx/x仓库
fork的仓库独立存在，在自己的仓库做任何修改不影响被fork的仓库
可以通过自己的仓库向原仓库发起*pull request*
如果原仓库作者同意，可以合并到原仓库
4. watch:关注 --> 项目有更新会提示，类似朋友圈
5. issue:问题 --> 发现代码BUG，但没有成型代码，需要讨论

sign in:登陆

sign up:注册

*开源项目贡献流程*

1. 新建Issue
2. 发起pull request

## 个人主页

访问地址：
https://用户名.github.io

搭建步骤：
1. 创建个人站点 --> 新建仓库（注：仓库名必须是【用户名.github.io】）
2. 在仓库下新建index.html的文件即可 --> 主页

注意：github个人主页仅支持静态网页

## 项目主页

访问地址：
https://用户名.github.io/仓库名

搭建步骤：
1. 进入项目主页，点击settings，点击[Launch automatic page generator]


gitlab在国内访问比较快，可以通过gitlab来下载github的项目


# 总结

![区域切换](image/区域切换.png)

1. 进入文件夹
2. git init --> 生成了.git 文件夹，开始管理该文件夹，即工作区
3. 配置：
   + 用户名：git config --global user.name 'xxx'
   + 邮箱：git config --global user.email 'xx@xxx'
   + 也可以使用--local参数，来表示该配置只适用于当前文件夹
4. git status --> 检测整个目录下文件的状态，即工作区的状态
    + 两种颜色:
    - 红色-->未被管理的文件或修改了以后的文件
    - 绿色-->已经管理了，但是没有生成版本  
5. git checkout <文件名/目录名> --> 放弃修改
6. git add <文件名/目录名> --> 加入到暂存区，git add .管理整个目录
7. git commit -m '自定义版本信息' --> 提交版本到版本库
8. git log --> 查看当前版本记录
9. git reflog --> 查看全部版本记录 
10. git reset <版本号>或者<HEAD> --> 回滚操作，从暂存区挪到工作区
11. git reset --hard <版本号>或者<HEAD> --> 回滚操作，从版本库挪到工作区未修改状态
12. git reset --soft <版本号>或者<HEAD> --> 回滚操作，从版本库挪到暂存区
13. git reset --mix <版本号>或者<HEAD> --> 回滚操作，从版本库挪到工作区已修改状态
14. git checkout -- <文件名> --> 放弃修改
15. git branch --> 查看分支
16. git branch <分支名> --> 创建分支，可以创建多个分支，不仅仅是两个
17. git checkout <分支名> --> 切换分支
18. git merge <分支名>  --> 合并分支，回到master分支进行操作
19. git branch -d <分支名> --> 删除分支
20. git remote --> 查看远程库信息
21. git remote -v  --> 查看远程库的详细信息
22. git remote add origin [链接]  --> 链接至远程仓库，此处origin是别名
23. git push -u origin master  --> 推送至远程仓库（主分支）
24. git push -u origin <分支名> --> 推送其他分支，-u可省略
25. git clone <url>  --> 复制代码，包含分支，不一定显示分支，可直接切换
26. git pull origin <分支名> --> 更新代码，clone之后用pull来更新代码
+ git pull =  git fetch + git merge
+ git fetch origin --> 将远程代码拉取到本地的版本库
+ git merge origin/<分支名> --> 合并代码，因为是远程拉取的，所有有前缀origin/
25. git branch --set-upstream-to=origin/dev dev --> 将本地分支跟踪远程分支，最后两个dev表示本地与远程的对应




