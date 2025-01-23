
from setuptools import setup, find_packages

# 定义包的元数据
setup(
    name='ShenlunChat',  # 包的名称
    version='0.1.0',  # 包的版本号
    author='Guo Chaoqun',  # 包的作者
    author_email='chaoqunguo1998@gmail.com',  # 作者的电子邮件地址
    description='GPT to grade answers of gongkao',  # 包的简短描述
    # long_description=open('README.md').read(),  # 包的长描述，通常是README.md文件的内容
    # long_description_content_type='text/markdown',  # 长描述的格式
    # url='https://github.com/your_username/my_package',  # 包的主页或源代码仓库
    packages=find_packages(),  # 要安装的包，自动查找所有包
    install_requires=[  # 包的依赖项
        'numpy',
        'json5',
        "openai",
        "langchain",
        "langgraph",
        "openai",
        "qianfan"
        # 添加其他依赖项
    ],
    classifiers=[  # 用于PyPI分类的元数据
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.6',  # 指定支持的Python版本
)