## 说明
其实本来想再加上RAG以及LayoutLM或者进行微调的，但是钱包的空间（以及5000字）太小放不下

同理，别用太多api不然要破产了

假如能把上面的全弄出来再加点别的应该能发个nc（别抢idea谢谢喵）
### 文件夹
- `abstract`: 生成的标准摘要文件，前五行为STpair.db的值，最后是摘要
- `all-testoutput`: 各项测试的相关文件，例如原始输出和测试结果
- `cases`: 生成CoT用的CoT
- `CoTs`: 生成的CoT
- `demo`: demo相关（例如输入和输出）
- 
### 文件
- `CoTgen.py`: 生成CoT
- `demo.py`: demo
- `garbageAbstract.py`: 提取摘要的辅助函数
- `garbageTrainGen.py`: 生成abstract中的文件
- `promptGen`: 简单的提示词生成函数
- `readdb.py`: 测试读取数据库，没用
- `README.md`: 本文件
- `regEX`: 全文匹配测试
- `result.py`: api的调用测试
- `schemaGen.py`: 生成对应type的schema
- `STpair.db`: 参与的研究[Pairpot: a database with real-time lasso-based analysis tailored for paired single-cell and spatial transcriptomics](https://doi.org/10.1093/nar/gkae986)中用到的STpair数据库
- `test.py`: 实验用文件，没用
- `testGen.py`: 进行PAIR的测试
- `utils.py`: 一些工具函数

其他文件基本都是一些临时文件或者期间用来测试idea的文件