# docs


### api bindings for python

A lot of my code depends on the bindings file being available in your python environment.
For e.g. I may have a venv_3.8. I have to place the [ob.py](https://github.com/dwillington/open-brush/blob/main/docs/api_bindings/ob.py) file there.

```
unlink ~/venv_3.8/lib/python3.8/site-packages/ob.py
#ln -s /root/temp/git_repos/open-brush/docs/api_bindings/ob.py ~/venv_3.8/lib/python3.8/site-packages/ob.py
ln -s /mnt/c/temp/git_repos/open-brush/docs/api_bindings/ob.py ~/venv_3/lib/python3.10/site-packages/ob.py

ipython
from ob import ob

ob.new()
ob.viewonly.toggle()


```

Original: https://gist.github.com/andybak/c700120232ca68a90adc791f75c8a16c
