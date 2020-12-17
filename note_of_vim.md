# 基本配置

    在gvim的安装目录下找到_vimrc文件，没有就新建一个
    打开gvim，然后把_vimrc拖入gvim的窗口中
    或者点击文件--》打开，找到该文件

    打开Vim，输入:echo $MYVIMRC，然后按Enter键。Vim会显示它正在使用的.vimrc的路径。

    把以下基本配置粘贴进去
    注意：vim的注释为"

    syntax on "支持语法高亮显示
    filetype plugin indent on "启用根据文件类型自动缩进
    set autoindent "开始新行时处理缩进
    set expandtab "将制表符TAB展开为空格，这对Python尤其有用
    set tabstop=4 "要计算的空格数
    set shiftwidth=4 "用于自动缩进的空格数
    set backspace=2 "在多数终端上修正退格键BACKSPACE的行为
    colorscheme murphy "修改配色

    "set directory=%USERDATA%.vim\swap// 把vim产生的交换文件统一存放在某个目录中
    set noswapfile "禁止产生的swap文件

    set nu "显示行号

    set undofile "启用持久性撤销
    if !isdirectory("%USERPROFILE%_vim")
            call mkdir("%USERPROFILE%_vim", "p")
    endif
    set undodir="%USERPROFILE%_vim"

    packloadall "加载所有插件 
    silent! helptags ALL "为所有插件加载帮助文档

    配色：输入：colorscheme (name) 或者：colorscheme(空格) (tab键) 选择

    重新加载vimrc:
    1、重启vim
    2、执行命令:source $MYVIMRC
    3、:w | source $MYVIMRC

## 设置工作目录

    在配置文件中加入cd (工作目录路径) 
    启动gvim后，可使用
    :pwd查看当前工作路径
    :cd +(路径) 更改工作路径
    也可以在配置中加入
    :set autochdir

# 光标移动&&插入模式

    h,j,k,l键用于上下左右移动，前面可以加上数字进行精确移动 

## 光标移动

    按照单词移动：
    w, e, b, W, E, B为按照单词移动，小写为狭义单词，大写为广义单词--即以空格隔开的单词。 
    段落移动：
    {、}这两个为按照段落移动，两个空行之间视为段落 
    以上命令之前均可加数字

    t键：until，后面接一个字符，用于在当前行内搜索该字符，并将光标置于此字符之前；T键则用于反向搜索
    f键：find，后面接一个字符，用于在当前行内搜索该字符，并将光标置于此字符之上；F键则用于反向搜索
    0键：将光标置于行首
    $键：将光标置于行尾

    · Shift+(和Shift+)分别将光标移动到句子的开头和结尾。
    · H将跳转到当前窗口的顶部，而L将跳转到当前窗口的底部。
    · Ctrl+f（或PageDown键）在当前缓冲区中向下翻页，而Ctrl+b（或PageUp键）为上翻页。
    · /接一个字符串，用于在文档中搜索该字符串，而?（Shift+/）用于反向搜索。
    · gg用于跳转到文件开头。
    · G用于跳转到文件结尾。

    >>: 整行右移
    <<: 整行左移

    :N（按Enter键）跳转到第N行，其中N为绝对行号。比如，跳到第20行，可通过命令:20（按Enter键）实现。

### EasyMontion插件(可选，非必须)

    仓库：easymotion/vim-easymotion
    启动方法：连续按两次先导键\(\为vim的默认先导键)，然后按某个移动键
    
    \\w 触发逐个单词的移动

    EasyMotion默认支持下列移动命令（所有命令都要加上两个先导符）。
    · f用于向右查找一个字符，F则用于向左查找字符。
    · t用于向右移动直到找到该字符，T则用于向左移动直到查找该字符。
    · w用于向后跳过一个狭义单词（W向后跳过一个广义单词）。
    · b用于向前跳过一个狭义单词（B向前跳过一个广义单词）。
    · e用于向前跳到狭义单词末尾（E向前跳到广义单词末尾）。
    · ge用于向后跳到狭义单词的末尾（gE向后跳到广义单词的末尾）。
    · k和j分别用于跳到上一行或下一行的开关。
    · n和N分别用于跳到上一个或下一个的搜索结果（在用/或?搜索之后）。
    EasyMotion还保留了很多快捷键没有使用，因此读者可以构建自己的快捷键映射。
    :help easymotion命令可查看EasyMotion的所有功能。

## 插入模式

    · a键用于在光标后面进入插入模式。
    · A键用于在当前行行尾进入插入模式（等价于$a）。
    · I键用于在当前行行首（在缩进之后）进入插入模式（等价于_i）。
    · o键用于在光标下面新增一行，在新的一行里进入插入模式。
    · O键用于在光标上面新增一行，在新的一行里进入插入模式。
    · gi用于在最后退出的位置进入插入模式。

    · C用于删除光标右边的文字（直到行尾），然后进入插入模式。
    · cc或S用于删除当前行的内容，然后进入插入模式，但会保留缩进。
    · s用于删除单个字符（如果前面加了数字，则会删除多个字符），然后进入插入模式。

    :d3w[刚好是删除（delete）3个单词（word）的英文缩写]可以删除后面3个词
    :ci"[改变（change）引号里面（inside）的英文缩写]则可以改变引号里面的文本。
    cc删除整行进入编辑模式并保持缩进

    注意：Windows样式的换行符和Linux样式的换行符，因为Windows和Linux处理换行的方式不同。
         如果在Vim中遇到^M字符无法识别，则对相应的文件执行dos2unix命令就可以解决。
        Vim可以支持的所有功能列表参见:help feature-list。

## 文本对象

    文本对象是Vim中额外增加的对象类型，比如括号内或引号内的文本都可以称作文本对象。
    通过文本对象，可以更方便地处理代码。
    文本对象只能与其他操作符组合起来使用，比如修改命令、删除命令或可视模式
    文本对象有两种：
    1.内对象（以i开头），不包含空白字符（或周围其他字符）
    2.外对象（以a开头），包含空白字符
    :help text-objects查看所有文本对象
    w\W表示狭义\广义单词
    s表示句子
    p表示段落
    t表示HTML/XML标签
    [],{},"",''等等内的内容都可以作为文本对象
    使用方法：
    1.
    将光标置于括号内任意位置
    输入di)
    发现整个括号内的内容删除了
    2.
    将光标放在一个单词上
    输入c2aw
    发现删除光标后的两个单词，包括周围的空格，并进入插入模式


# 搜索

    Vim中最快的文本浏览方式是搜索指定的字符串。

## 页面内搜索

    步骤：
    1.搜索方法是按/键（从正常模式进入命令模式），然后输入待搜索的字符串。
    2.按Enter键之后，光标将移动到第一个匹配的地方。
    3.按n键可以在同一个缓冲区中循环遍历所有匹配的位置，而按N键则可以开始反向遍历。

    :noh 清除高亮显示
    
    配置：
    set hlsearch "启用高亮每个匹配项
    set incsearch "跳转光标到第一个匹配处

## 跨文件搜索

    :vimgrep <模式><路径> 其中模式可以是一个字符串，也可以是一个vim风格的正则表达式。
                        路径通常为一个通配符，当路径为**时，表示对目录递归搜索
                        或者使用**\*.py搜索具体的文件类型
    在底部显示匹配的个数
    :cn 或 :cp 逐个浏览各匹配项
    :copen 可视化显示的快速恢复列表
    :q 退出列表

# 基本编辑

    :w(write) 保存，写入。后面可以接一个新的文件名表示另存为工作目录
    :q(quit) 退出
    ! 表示强制，例如:q! 
    命令可组合
    :wq!

    所有命令均遵循命令+数字+移动或一个文本对象
    dd删除整行
    u撤销最后一次操作
    ctrl+r可以重做u操作

## 打开/查看文件

    :e+文件名（路径）表示edit编辑文件

    :help进入vim手册
    可以用简写版的help命令，:h
    还可以在该命令后面加上关键字来具体搜索需要查看的内容
    如  :h search
        :h autochdir

    :ls查看当前所有缓冲区

## 缓冲区切换

    :ls 查看缓冲区
    :b+数字，切换缓冲区bn或bp用来表示前一个缓冲区和后一个，bd表示删除缓冲区，未保存会提示

    vim-unimpaired插件,它为很多内置命令（以及一些新的命令）添加映射。
    · ]b和[b循环遍历缓冲区。
    · ]f和[f循环遍历同一目录中的文件，并打开为当前缓冲区。
    · ]l和[l遍历位置列表（参见第5章）。
    · ]q和[q遍历快速修复列表（参见第5章）。
    · ]t和[t遍历标签列表（参见第4章）。

## 粘贴&复制

    y后面接一个移动命令或一个文本对象。
    yy复制一行
    ye复制文本直到下一个单词结尾
    然后，将光标移动到待粘贴的位置（文本将插入光标之后）
    然后，按p键将文本粘贴到指定位置

    粘贴操作p的前面可以加数字，从而实现多次粘贴

### 寄存器

    在Vim中复制和粘贴文本时，文本是储存在Vim寄存器里面的。
    Vim支持多种寄存器，每个寄存器用字母、数字或特殊符号来标识。

    寄存器的访问方式是引号键"，后面接寄存器的标识符，然后是针对指定寄存器的操作。

    a～z所标识的寄存器用于手动复制数据。
    比如，将一个单词复制到a寄存器，可以使用"ayw命令，而粘贴命令为"ap。

    前面介绍的复制和粘贴操作使用的都是默认的无名寄存器。
    这个无名寄存器用双引号"来标识，读者可以用这个标识符来显式访问寄存器。
    比如，""p用于从无名寄存中粘贴文本，等同于p。

    还有一些很有用的只读寄存器：
    %存储了当前文件名
    #存储了上次打开的文件名
    .中为最后插入的文本
    :为最后执行的命令

    Ctrl+r组合键允许读者在插入模式或命令行模式下粘贴某个寄存器的内容。
    比如，在插入模式下，按Ctrl+r组合键，"会在光标处粘贴无名寄存器中的内容。

    读者可以在任何时候通过:reg <寄存器标识符>命令来访问某个寄存器的内容。
    比如，:reg a b命令可同时得到a和b寄存器中的内容

    :reg命令列出所有寄存器的内容

    y命令会重写寄存器内的内容，而字母命令的寄存器（a～z）是可以附加内容的，方法是使用大写的寄存器标识符。
    比如，若想附加一个单词到寄存器a中，可以先将光标置于此单词开头，然后执行"Ayw命令。

    与外部世界交互：
    · *寄存器表示系统的主粘贴板（macOS和Windows系统中的默认粘贴板，在Linux系统中为终端的鼠标选择内容）
    · +寄存器（只针对Linux）用于Windows风格的Ctrl+c组合键和Ctrl+v组合键操作
        ［称为粘贴板选择器（Clipboard selection）］

    这两个寄存器的使用方式与其他寄存器相同。比如，"*p命令用于从系统主粘贴板中将文本粘贴进来，
    "+yy命令则将一行文本复制到Linux的粘贴板选择器中。
    如果读者希望默认使用这些寄存器，可以在.vimrc文件中设置clipboard变量，将其设置为unamed时，
    表示默认使用*寄存器进行复制和粘贴。
    set clipboard=unamed "复制到系统寄存器（*）
    set clipboard=unnamedplus "复制到系统寄存器（+）
    set clipboard=unnamed,unnamedplus "复制到系统寄存器（*，+）
    在.vimrc文件中完成设置之后，y和p命令将分别从指定的默认寄存器中复制和粘贴。




# 安装插件

    git clone https://github.com/xxx/xxx.git
    Linux创建以下目录
    ~/.vim/pack/plugins/start
    Windows创建以下目录
    vim的安装目录创建vimfiles文件夹
    vimfiles\pack\plugins\start
    最后的xxx/xxx表示github仓库的唯一标识。

    自动加载插件及文档，添加以下配置
    packloadall
    silent! helptags ALL

# 窗口管理

    使用：ls命令后的一些信息：
    · 1为缓冲区编号，在整个Vim会话中，它的值保持不变。而且唯一，除非退出vim
    · % 表示该缓冲区位于当前窗口中。· a 表示该缓冲区处于活动状态，即它已被加载并可见。
    · "animal_farm.py"为文件名。
    · line 30表示当前光标位置。

    只要知道Vim支持哪些窗口操作，剩下的操作可以通过查看文档。
    使用:help window-moving和:help window-resize打开Vim手册中相应的条目，即可找到所有相关的快捷键

    窗口命令的快捷键都要先按Ctrl+w组合键    

    窗口编号与缓冲区不同，随着布局变化而改变。
    原则：窗口编号顺序由上至下、由左至右递增。

## 分割窗口

    :split<空格><文件名> (简化版：:sp)上下分割窗口，打开新文件，光标出现在新窗口
    :vsplit<空格><文件名> (简化版：:vs)水平分割窗口，打开新文件，光标出现在新窗口
    
    C+w h\j\k\l 光标可以在各个窗口之间移动。
    以上命令重新绑定，在配置中加入以下命令：
    noremap <c-h> <c-w><c-h>
    noremap <c-j> <c-w><c-j>
    noremap <c-k> <c-w><c-k>
    noremap <c-l> <c-w><c-l>

    C - w,o (或：only, 或：on命令)关闭除当前窗口之外的所有窗口

    :qa 关闭所有窗口并退出vim
    :wqa 保存所有打开的文件，在退出vim

    如果只想关闭缓冲区，而保留它所在的窗口，则可以在.vimrc文件中加入如下配置。
    command! Bd :bp | :sp | :bn | :bd
    然后，读者就可以使用:Bd来关闭缓冲区，而保留分割窗口。

## 窗口移动

    窗口命令的快捷键都要先按Ctrl+w组合键，后面跟一个大写的方向键（H、J、K和L中的一个），
    当前窗口会被移动到相应的位置。
    · 使用Ctrl+w,H组合键将当前窗口移动到屏幕的最左边。
    · 使用Ctrl+w,J组合键将当前窗口移动到屏幕的底部。
    · 使用Ctrl+w,K组合键将当前窗口移动到屏幕的顶部。
    · 使用Ctrl+w,L组合键将当前窗口移动到屏幕的最右边。

### 窗口内容的移动

    c - w r 将当前行或当前列（行优先于列）中的每个窗口的内容向右或向下移动
    c - w R 与上面的操作方向相反

    使用Ctrl+w,x组合键将当前窗口与下一个窗口的内容交换（如果当前窗口是最后一个，则与前一个交换）。

## 改变窗口大小

    窗口默认宽高比为50/50

    C - w = 将每个窗口的宽和高调整一致

    :resize命令会增加或减少当前窗口的高度，
    :vertical resize将调整窗口的宽度。

    具体使用:
    · :resize +N用于将当前窗口的高度增加N行。
    · :resize -N用于将当前窗口的高度减少N行。
    · :vertical resize +N用于将当前窗口的宽度增加N列。
    · :vertical resize -N用于将当前窗口的宽度减少N列。 
    :resize和:vertical resize可分别简写为:res和:vert res。
    · :resize N用于将窗口高度设置为N。
    · :vertical resize N用于将窗口宽度设置为N。

    将窗口高度和宽度改变一行/列的快捷键：
    Ctrl-w -和Ctrl+w +用于调整高度，
    Ctrl+w >和Ctrl+w <用于调整宽度。

## 标签页（TABS）
    
    一个标签页可以包含多个窗口，用标签页可以更方便地管理窗口集合。
    标签页通常用来在同一个vim会话中区分不同的问题或者文件集合。

    标签的用途：
    1、在不同项目或同一项目的不同上下文之间切换
    2、使用标签的diff功能，diff作用于一个标签页内

    :tabnew 新建标签页
    :tabnew <文件名> 新建标签页并打开一个文件
    在其中，可以用:e命令打开文件，也可以用:b来切换缓冲区

    标签页之间跳转
    gt或:tabnext 切换到下一个标签页
    gT或:tabprevious 切换到上一个标签页

    :tabclose 关闭标签，同时关闭标签页中的窗口，如果只有一个标签页，则需要:q命令

    :tabmove N 将当前标签页移动到第N个标签页之后（如果N为0，则编程第一个标签页）


# 折叠代码

    折叠的依据可以是预定义的规则，也可以是手动添加的折叠标记。

    在配置文件中加入以下代码：
    set foldmethod=indent  ==>按照缩进折叠，python式

    zo 将光标移动到其中一个折叠行上，打开折叠
    zc 只要光标在一个潜在折叠文本中，即可折叠代码
    za 切换折叠状态。（最常用）

    :set foldcolumn=N 其中N取值0-12，用来在屏幕的最左边显示折叠的情况，
                        -号表示一个打开的折叠，|表示打开的折叠的内容，+号表示关闭的折叠
    
    :zR  同时打开所有折叠
    :zM  同时关闭所有折叠

    折叠方法：
    · manual：手动折叠，这种方法对于长文本而言并不适用。
    · indent：基于缩进的折叠，这对于依赖缩进的编程语言非常合适（不管哪种语言，标准的编码风格中总是会采用某种一致性的
             缩进。因此，当读者想要快速隐藏不关心的代码时，indent折叠方式不失为一种高效率的选择）。
    · expr：基于正则表达式的折叠。如果读者想要用复杂的规则来定义折叠，那么可以选择这种方式。
    · marker：使用文本中特殊的标记来定义折叠，比如{{{和}}}。这种方法对于管理很长的.vimrc文件非常有效，但是在Vim之
             外不常用，因为这种方式需要修改文件内容。
    · syntax：提供了可识别语法的折叠，但它并非对所有语言都开箱即用（不支持Python）。
    · diff：当Vim处于diff模式时会自动采用这种折叠方式，diff模式下需要展示两个文件的不同之处，而相同之处往往需要隐藏
            起来

# 文件数的浏览

    vim可以用来浏览系统的各种文件及目录，通过内置或外部插件还可管理文件和目录。

## 内置插件--Netrw
    vim的内置文件管理器--Netrw
    :Ex(完整命令为:Explore)打开文件浏览窗口。该命令可显示隐藏文件及.开头的文件
        Enter键用于打开文件和目录
        -键进入上一层目录
        D键删除一个文件或目录
        R键重命名一个文件或目录
    :e . 这个命令打开当前目录，调用Netrw，不显示隐藏文件，不显示以.开头的文件

    Netrw的窗口可以在分割窗口或标签页中打开
    :Vex 左右分割打开Netrw
    :Sex 上下分割打开Netrw
    :Lex 左右分割打开Netrw,当前Netrw窗口位于最左边，且高度占满整个屏幕

    I键，显示/隐藏顶部帮助栏
    shift+~ 打开用户主目录
    还是用:cd . + :e .比较好用，这个主目录由用户在.vimrc中设置

## 支持文件菜单的:e命令

    在配置中加入：
    set wildmenu
    set wildmode=list:longest,full
    上述设置允许读者在第一次按Tab键时将部分路径补全为最长的匹配字符串（并且还会展示所有的可能项）；
    第二次按Tab键时遍历wildmenu中的文件。

## NERDTree插件(可选)

    在屏幕边缘用一个分割的缓冲区来展示文件树。
    GITHUB仓库：scrooloose/nerdtree
    :NERDTree 启动NERDTree功能
    :NERDTreeClose 关闭NERDTree功能
    在NERDTree中，使用hjkl键移动，使用Enter键或o键打开选中的文件。
    使用shift+?查看全部快捷键，再按一次shift+?退出查看

    书签功能：
    :Bookmark 该命令来收藏当前光标选择的目录
    :Bookmark <名字> 给书签起个名字
    (大写)B键--》在窗口顶部显示/隐藏所有书签

    在NERDTree窗口中保持显示，添加配置：
    let NERDTreeShowBookmarks=1

    在NERDTree变成最后一个窗口时自动关闭，添加配置：
    autocmd bufenter * if (winr("$")==1 && exists("b:NERDTree") && 
    \ b:NERDTree.isTabTree()) | q | endif

    有用户觉得文件列表容易让人分心，转而又会返回到更简洁的Netrw。

    如果读者同时安装了NERDTree和Vinegar，则Vinegar会使用NERDTree窗口，而不是Netrw。为了避免NERDTree取代
    Netrw（而且使-键之类的命令保持可用），读者需要在.vimrc文件中设置
    let NERDTreeHijackNetrw= 0。

## 文件模糊补全插件--CtrlP

    github仓库：ctrlpvim/ctrlp.vim
    使用步骤：
    1.在vim中按Ctrl + p组合键启动，在屏幕下方出现CtrlP窗口，其中列出了项目目录中的文件列表
    2.输入文件名或目录中的关键字
    3.C-j或C-k组合键来上下遍历列表
    4.Enter键打开选中的文件
    5.Esc键退出CtrlP窗口

    CtrlP有三种搜索位置：当前目录，缓冲区，最近使用的文件
    以上可以用c - f和c - b来循环切换
    以上也可以用命令来实现
    :CtrlPBuffer 列出缓冲区
    :CtrlPMRU    列出最近使用的文件
    :CtrlPMixed  同时显示文件、缓冲区和最近使用的文件

# 插件管理

    在windows系统中，在vim的安装文件夹内，在vimfiles下git clone这个junegunn/vim-plug插件
    然后将vim-plug文件夹改名为autoload，不然无法识别

    下面修改_vimrc文件：-->所有需要的插件放在call plug#begin()和call plug#end()中间
    call plug#begin()  " 使用vim-plug管理插件
    Plug 'ctrlpvim/ctrlp.vim'
    Plug 'easymotion/vim-easymotion'
    "Plug 'mileszs/ack.vim'
    Plug 'scrooloose/nerdtree', { 'on': 'NERDTreeToggle' }
    Plug 'tpope/vim-unimpaired'
    Plug 'tpope/vim-vinegar' 
    call plug#end()

    加入配置之后使用:w | source $MYVIMRC或重启vim来使配置生效
    执行:PlugInstall来安装插件

    这里有个问题：vim-plug总是把插件放到vim的$HOME变量的文件夹下。
            在windows10中，这个变量要自己新建在用户的环境变量下，手动新建
        这里插播几个查看vim环境变量的命令
        :echo $HOME
        :echo $VIMRUNTIME
        :echo $VIM

    vim-plug有两个主要的命令
    · :PlugUpdate用于更新所有已安装的插件。
    · :PlugClean用于删除.vimrc中已经移除的插件。如果不执行:PlugClean，则没有激活的插件
        （.vimrc中删除或注释掉的那些Plug...行）将仍然保存在文件系统中。

    运行:PlugUpdate将更新vim-plug所管理的插件，但不包括它自己。
    如果想要更新vim-plug，需要运行:PlugUpgrade命令，然后重载.vimrc文件
    （执行:source $MYVIMRC或重启Vim）。

    延迟加载：
    on参数：在命令执行时加载
    Plug 'scrooloose/nerdtree', {'on': 'NERDTreeToggle'}

    for参数：只对特定文件类型加载某个插件
    Plug 'junegunn/goyo.vim', {'for':'markdown'}

    手动管理插件：不推荐

## 分析插件启动

    vim --startuptime <文件名> 将vim启动时的每个行为记录到一个文件中
    例如：
    vim --startuptime startuptime.log

    windows中
    gVim --startuptime startuptime.log

    退出vim打开startuptime.log查看结果
    
    当某个插件启动时间达到500ms（半秒）以上时，才会感觉到慢


# 模式

    命令行模式：
    输入冒号：或者/或?进行搜索
    其中，上下箭头与c - p 和c - n可以浏览命令的历史记录
    c - b和c - e可以跳转到命令的开头(beginning)和结尾(ending)
    shift键和ctrl键结合左右箭头可以逐个单词移动光标

    在命令行模式下，输入c - f可以打开一个可编辑的窗口，其中显示的时之前运行过的命令的历史记录
    该窗口是一个普通的可编辑窗口，使用c - c组合键可以编辑此缓冲区
    将光标移动到某个命令上，按enter键可以运行该命令
    更多命令行模式请查看文档:help cmdline-editing

    插入模式：
    i键光标所在位置之前插入
    a键光标所在位置之后插入
    o键光标所在位置的下一行插入一个新的空白行
    在插入模式下，使用c - o组合键来执行正常模式下的命令，然后回到插入模式
    例如：
    c - o gg 跳转到第一行
    c - o G  跳转到最后一行
    c - o :  输入命令

    可视模式和选择模式：
    v  字符可视模式（状态栏显示--VISUAL--）
    V  行可视模式（状态栏显示--VISUAL LINE--）
    c - v 块可视模式（状态栏显示--VISUAL BLOCK--）
    进入任意可视模式后，可以使用任意移动光标指令
    例如：
    v -> 3e -> l(小写L)
    控制可视模式下的文本选择：
    o键跳转到高亮选中文本的另一端
    对于块可视，o键可以跳转到当前行的另一端

    替换模式和虚拟替换模式：
    在其他编辑器里，按Insert键进入替换模式，其效果是擦除其他文本。
    在Vim下，替换模式也类似，输入的文本会覆盖已有的文本（而不像插入模式下，输入文本会移动已有文本）。
    R键进入替换模式(状态栏显示--REPLACE--)
    r键进入单字符替换模式，替换单个字符后立刻切换会正常模式
    Vim还提供了虚拟替换模式，它和替换模式类似，只不过操作的对象是屏幕上的显示，而非直接针对文件中的字符。
    主要的区别包括Tab键会替换多个字符（而替换模式下只会替换单个字符）；按Enter键不会新增一行，但会移动到下一行。
    虚拟替换模式的进入方式是输入gR。
    详情参见帮助文档:helpvreplace-mode。

    终端模式：
    在一个分割窗口中运行一个终端环境，vim8.1以后的版本
    :terminal
    在windows中运行的是cmd，所以只支持cmd命令，如dir等。
    在linux中运行的是默认的shell。
    该终端窗口中只有插入模式，在window下无法用快捷键切换回原窗口，可使用exit命令退出
    在linux或macos中，可以使用tmux命令或screen命令来与vim的终端模式配合使用
    !!!可以使用:term执行单个命令，并把输入存放于一个缓冲区中。
    例如：
    :term python animal_farm.py cat dog
    默认水平分割窗口，该窗口可以:q退出

# 命令的重映射

## 基本快捷键重置

    即重新设置vim的快捷键
    :map       递归映射
    :noremap   非递归映射
    这意味着经:map重映射的命令可以识别自定义映射，而:noremap则针对系统默认映射。
    即更改的原快捷键不同，map更改全部的快捷键，noremap只能更改系统定义的快捷键
    :help index 查看内置的按键绑定列表
    :map       查看插件和自定义的映射
    :map g      查看所有以g键开头的映射

    自定义映射：
    在.vimrc中修改
    例
    noremap ; :  "用分好取代默认的冒号，用于输入命令
    使用noremap表示希望用分号进入命令行模式，而无论冒号是否已经被重映射都不会影响这一点。

    :unmap命令如果想显式移除自定义或插件定义的映射。
    :mapclear，它会将读者定义的映射和默认映射都清除掉。

    特殊字符和命令映射，例如
    noremap <c-u> :w<cr> "使用c - u来保存文件
    vim中ctrl修饰符表示为<c-_>，其中_表示某个字符
    命令后面接<cr>表示回车（Enter键）。
    如果没有按Enter键，则命令虽然输入了，却不会被执行，会停留在命令行模式下。
    其他：
    · <a-_>或<m-_>表示Alt键加上某个键，比如<m-b>表示Alt+b组合键。
    · <s-_>表示Shift键加某个键，比如<s-f>表示Shift+f组合键。
    一些特殊字符：
    · <space>表示空格。
    · <esc>表示Esc键。
    · <cr>和<enter>表示Enter键。
    · <tab>表示制表符Tab键。
    · bs表示退格键。
    · <up>、<down>、<left>和<right>表示箭头键。
    · <pageup>、<pagedown>表示上下翻页键。
    · <f1>～<f12>表示12个功能键。
    · <home>、<insert>、<del>和<end>分别表示Home、Insert、Delete和End键。

    还可以将一个键映射为<nop>（无操作no operation的缩写），表示这个键不起任何作用。
    有时候，读者希望习惯使用hjkl风格的光标移动方式，而禁止自己使用箭头键，这个映射此时会派上用场。
    可以在.vimrc中加入如下配置。
    map <up> <nop>
    map <down> <nop>

## 为某个模式定制映射（快捷键）

   :map命令和:noremap命令都可用于正常模式、可视模式、选择模式和操作待决模式（operator pending mode）。
   · :nmap和:nnoremap用于正常模式。
   · :vmap和:vnoremap用于可视和选择模式。
   · :xmap和:xnoremap用于可视模式。
   · :smap和:snoremap用于选择模式。
   · :omap和:onoremap用于操作待决模式。
   · :map!和:noremap!用于插入和命令行模式。
   · :cmap和:cnoremap用于命令行模式。
   · :imap和:inoremap用于插入模式。<---常用

    "按对插入括号，引号等，并把光标放在内部
    inoremap ' ''<esc>i
    inoremap " ""<esc>i
    inoremap ( ()<esc>i
    inoremap { {}<esc>i
    inoremap [ []<esc>i

    "在插入模式下快速回到正常模式
    inoremap fd <esc>

## 先导键

    先导键-->leader key，本质上是使用者或插件定义的快捷方式的命名空间。
    先按先导键，然后按下的任何键都来自于该命名空间

    默认先导键为反斜线\
    逗号是目前比较流行的重新自定义的先导键
    在.vimrc文件中加入配置
    let mapleader=','

    推荐使用空格键
    let mapleader="\<space>"
    先导键的设置要放在.vimrc的顶部，因为新定义的先导键只会在定义之后生效。
    这里<space>之前的转义符\是必要的，因为mapleader变量中不含特殊字符（如空格符）。
    对于这个转义来说，只能用双引号，而不能是单引号，因为单引号中只能存字面量字符串，而不含转义字符。

## 查看某插件的说明文档

    :help ctrlp 打开ctrlp的说明文档
    /options    搜索关键字options
    c - ]       打开链接

# 编程-->自动补全、浏览代码库

## kite--智能自动补全插件

再用，所有教程均来自bing搜索

## 推荐插件-->自动补全插件YouCompleteMe

    首先要下载cmake和llvm
    windows、linux和mac都要下载
    linux--ubuntu下：
    sudo apt-get install cmake llvm

    下载之后在配置中添加
    let g:plug_timeout=300 "为YouCompleteMe增加vim-plug的超时时间
    Plug 'Valloric/YouCompleteMe', {'do': './install.py}

    下载完之后出现unable to load python
    暂时搁置
    经搜寻网络，提示该插件配置过难....

## 浏览变量定义--自带功能

    将光标置于需要查看的变量上，
    输入gd，即可跳转到该变量的定义处。
    gd优先查看局部变量声明，
    gD查看全局声明（从文件开头开始查找，而不限于当前的作用域）

    vim可以基于标签进行查找，需要外部工具来生成标签文件。

    在linux系统中使用ctags比较方便，还可以自动更新标签。

# 撤销树

## Gundo插件

    地址："sjl/gundo.vim"
    :w | so $MYVIMRC | PlugInstall
    不知为何无法使用
    错误提示信息：需要python解释器2.4以上，实际安装3.7