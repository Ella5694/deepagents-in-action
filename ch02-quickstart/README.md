# Ch02 Quickstart — Deep Agents 快速上手

Datawhale《Deep Agents 实战》第 2 章实验代码与笔记。

## 本目录有什么

| 文件 | 说明 |
|------|------|
| `hello_agent.py` | Hello World：自定义天气工具 |
| `hello_no_tool.py` | 无工具对照 |
| `calc_agent.py` | 计算器 + 货币换算（多工具串联） |
| `research_agent.py` | Tavily 联网研究 + TodoList 中间件 |
| `任务2-快速上手-学习笔记.md` | 过程笔记、踩坑与实验总结 |
| `assets/` | 笔记配图 |

## 环境

- Python 3.11+（本机用 uv）
- 硅基流动 API Key（或其它 OpenAI 兼容接口）
- 研究助手还需 `TAVILY_API_KEY`；可选 LangSmith Trace

```bash
cd ~/projects/deepagents-in-action/ch02-quickstart
source $HOME/.local/bin/env   # 若 uv 不在 PATH
uv sync
set -a && source ~/.env && set +a   # 按你实际 env 路径调整
```

## 怎么跑

```bash
uv run python hello_agent.py
uv run python calc_agent.py
uv run python research_agent.py
```

模型可通过环境变量切换，例如：

```bash
export MODEL_NAME="Qwen/Qwen2.5-7B-Instruct"
```

## 注意

- `.env` / API Key 不要提交进 Git
- 详细步骤与排错见 `任务2-快速上手-学习笔记.md`
