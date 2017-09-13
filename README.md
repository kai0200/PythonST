#生成密钥
ssh-keygen -t rsa -C "Your email"

#
在github上添加了ssh的id_rsa.pub后需要执行一下命令yes后免密码可push
ssh -T git@github.com

git 方法
git add *
git commit -m "学习Python各种模块"

git push -u origin master


#2017-01-19 将HTML文档转化为文本显示在UNIX终端上
001-html-to-term.py

# Python3 标准模块尝试    https://pymotw.com/3/string/index.html
## Text
### string - Text Constants and Templates
Time: 2017-09-12

###  问题

如何在""" """ 里添加注释


### Ubunto16.04 美化
---
https://segmentfault.com/a/1190000006111345
https://github.com/anmoljagetia/Flatabulous
https://github.com/robbyrussell/oh-my-zsh
https://github.com/amix/vimrc

### 增加终端字体   FSEX300.ttf
---
```
https://my.oschina.net/itblog/blog/278566
sudo mkdir -p /usr/share/fonts/winFonts
sudo cp ~/Desktop/font/*.ttf  /usr/share/fonts/winFonts/
sudo chmod 644 /usr/share/fonts/winFonts/*.ttf
cd /usr/share/fonts/winFonts/
sudo mkfontscale （创建雅黑字体的fonts.scale文件，它用来控制字体旋转缩放）
sudo mkfontdir （创建雅黑字体的fonts.dir文件，它用来控制字体粗斜体产生）
sudo fc-cache -fv （建立字体缓存信息，也就是让系统认识雅黑）
```

终端字体调节大小  ```Ctrl  -``` ```Ctrl  +``

### K-vim 管理插件的命令
```
:PlugInstall     install                      安装插件
:PlugUpdate      install or update            更新插件
:PlugClean       remove plugin not in list    删除本地无用插件
:PlugUpgrade     Upgrade vim-plug itself      升级本身
:PlugStatus      Check the status of plugins  查看插件状态
```

更新以后要重新编译YouCompleteMe

```
# /tmp/b.sh
echo "Step4: compile YouCompleteMe"
echo "It will take a long time, just be patient!"
echo "If error,you need to compile it yourself"
echo "cd $CURRENT_DIR/bundle/YouCompleteMe/ && python install.py --clang-completer"
cd $CURRENT_DIR/bundle/YouCompleteMe/
git submodule update --init --recursive
if [ `which clang` ]   # check system clang
then
    python install.py --clang-completer --system-libclang   # use system clang
else
    python install.py --clang-completer
fi
```

snippets  插件
Python vim tab 快捷键
~/.vim/bundle/vim-snippets/snippets/python.snippets

### 多行选择
===

``` Ctrl + m```

实现相同字段排量修改

```,gd``  跳到声明位置, 仅 filetypes: c, cpp, objc, objcpp, python 有效

### k-vim 快捷键

```C-w-L```  vim 分屏以后从s 转到v
```C-w-K```  vim 分屏以后从v 转到s
```z-M```    all折行操作
```z-R```    all折行操作
```z-c```    单独折行操作
```z-o```    单独折行操作

### k-vim  git 同步最新版

git reset --hard
git pull




