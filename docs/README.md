# docs


### api bindings for python

https://gist.github.com/andybak/c700120232ca68a90adc791f75c8a16c

```
unlink ~/venv_3.8/lib/python3.8/site-packages/ob.py
#ln -s /root/temp/git_repos/open-brush/docs/api_bindings/ob.py ~/venv_3.8/lib/python3.8/site-packages/ob.py
ln -s /mnt/c/temp/git_repos/open-brush/docs/api_bindings/ob.py ~/venv_3/lib/python3.10/site-packages/ob.py

ipython
from ob import ob

ob.new()
ob.viewonly.toggle()


```
