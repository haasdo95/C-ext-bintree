from distutils.core import setup, Extension
setup(name="bintree", version="1.0",
      ext_modules=[
          Extension("bintree", sources=["bintree_module.c"])
      ]
)