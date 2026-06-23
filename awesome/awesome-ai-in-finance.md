# AI in Finance

[![GitHub stars](https://img.shields.io/github/stars/georgezouq/awesome-ai-in-finance?style=flat)](https://github.com/georgezouq/awesome-ai-in-finance/stargazers)

# Awesome AI in Finance [![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome) [![Community](https://img.shields.io/discord/733027681184251937.svg?style=flat&label=Join%20Community&color=7289DA)](https://discord.gg/cqaUf47)

There are millions of trades made in the global financial market every day. Data grows very quickly and people are hard to understand.
With the power of the latest artificial intelligence research, people analyze & trade automatically and intelligently. This list contains the research, tools and code that people use to beat the market.

[[中文资源](./chinese.md)]

## Contents

- [Agents](#agents)
- [LLMs](#llms)
- [Papers](#papers)
- [Courses & Books](#courses--books)
- [Strategies & Research](#strategies--research)
  - [Time Series Data](#time-series-data)
  - [Portfolio Management](#portfolio-management)
  - [High Frequency Trading](#high-frequency-trading)
  - [Event Drive](#event-drive)
  - [Crypto Currencies Strategies](#crypto-currencies-strategies)
  - [Technical Analysis](#technical-analysis)
  - [Lottery & Gamble](#lottery--gamble)
  - [Arbitrage](#arbitrage)
- [Data Sources](#data-sources)
- [Research Tools](#research-tools)
- [Trading System](#trading-system)
- [TA Lib](#ta-lib)
- [Exchange API](#exchange-api)
- [Articles](#articles)
- [Others](#others)

## Agents

- 🌟🌟 [nofx](https://github.com/NoFxAiOS/nofx) [![GitHub stars](https://img.shields.io/github/stars/NoFxAiOS/nofx?style=flat)](https://github.com/NoFxAiOS/nofx/stargazers) - A multi-exchange Al trading platform with multi-Ai competition self-evolution, and real-time dashboard.
- [TradingAgents](https://github.com/TauricResearch/TradingAgents) [![GitHub stars](https://img.shields.io/github/stars/TauricResearch/TradingAgents?style=flat)](https://github.com/TauricResearch/TradingAgents/stargazers) - Multi-Agents LLM Financial Trading Framework.
- 🌟 [FinRobot](https://github.com/AI4Finance-Foundation/FinRobot) [![GitHub stars](https://img.shields.io/github/stars/AI4Finance-Foundation/FinRobot?style=flat)](https://github.com/AI4Finance-Foundation/FinRobot/stargazers) - An Open-Source AI Agent Platform for Financial Analysis using LLMs.
- [AgentFund](https://github.com/RioBot-Grind/agentfund) [![GitHub stars](https://img.shields.io/github/stars/RioBot-Grind/agentfund?style=flat)](https://github.com/RioBot-Grind/agentfund/stargazers) - Decentralized crowdfunding platform for AI agents with milestone-based escrow on Base blockchain.
- 🌟 [ATLAS](https://github.com/chrisworsey55/atlas-gic) [![GitHub stars](https://img.shields.io/github/stars/chrisworsey55/atlas-gic?style=flat)](https://github.com/chrisworsey55/atlas-gic/stargazers) - Self-improving AI trading system with 25 agents, Karpathy-style autoresearch, Darwinian selection, autonomous agent spawning, and multi-cohort meta-weighting.
- [InvicTrade](https://invictrade.com) - AI-powered trading signals with 74% historical win rate, combining strategies from legendary investors using multi-model AI intelligence.
- [OpenFinClaw](https://github.com/cryptoSUN2049/openFinclaw) [![GitHub stars](https://img.shields.io/github/stars/cryptoSUN2049/openFinclaw?style=flat)](https://github.com/cryptoSUN2049/openFinclaw/stargazers) - AI-native one-person hedge fund platform. Expert agent teams turn natural language into quant strategies in 60s. Multi-market (US/HK/CN/Crypto), self-evolving strategy pipeline with community leaderboard.
- [Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) [![GitHub stars](https://img.shields.io/github/stars/HKUDS/Vibe-Trading?style=flat)](https://github.com/HKUDS/Vibe-Trading/stargazers) - Multi-agent finance research workspace for strategy generation, backtests, portfolio analysis, and research insights.
- [ProfitPlay Agent Arena](https://github.com/jarvismaximum-hue/profitplay-starter) [![GitHub stars](https://img.shields.io/github/stars/jarvismaximum-hue/profitplay-starter?style=flat)](https://github.com/jarvismaximum-hue/profitplay-starter/stargazers) - Open prediction market arena where AI agents compete in real-time BTC/ETH/SOL prediction games. Python and Node.js SDKs, 9 live markets, REST + WebSocket APIs.
- [oracle3](https://github.com/YichengYang-Ethan/oracle3) [![GitHub stars](https://img.shields.io/github/stars/YichengYang-Ethan/oracle3?style=flat)](https://github.com/YichengYang-Ethan/oracle3/stargazers) - Prediction-market trading agent for Kalshi, Polymarket, and Solana DFlow, with Wang Transform pricing and arbitrage strategies.

## LLMs

- 🌟🌟🌟 [Nof1](https://thenof1.com/) - Benchmark designed to measure AI's investing abilities. Each model is given $10,000 of real money, in real markets, with identical prompts and input data.
- 🌟 [AI Hedge Fund](https://github.com/virattt/ai-hedge-fund) [![GitHub stars](https://img.shields.io/github/stars/virattt/ai-hedge-fund?style=flat)](https://github.com/virattt/ai-hedge-fund/stargazers) - Explore the use of AI to make trading decisions.
- 🌟🌟 [MarS](https://github.com/microsoft/MarS) [![GitHub stars](https://img.shields.io/github/stars/microsoft/MarS?style=flat)](https://github.com/microsoft/MarS/stargazers) - A Financial Market Simulation Engine Powered by Generative Foundation Model.
- 🌟🌟 [Financial Statement Analysis with Large Language Models](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4835311) - GPT-4 can outperform professional financial analysts in predicting future earnings changes, generating useful narrative insights, and resulting in superior trading strategies with higher Sharpe ratios and alphas, thereby suggesting a potential central role for LLMs in financial decision-making.
- [FinRpt](https://arxiv.org/abs/2511.07322) - Dataset, Evaluation System and LLM-based Multi-agent Framework for Equity Research Report Generation.
- [PIXIU](https://github.com/chancefocus/PIXIU) [![GitHub stars](https://img.shields.io/github/stars/chancefocus/PIXIU?style=flat)](https://github.com/chancefocus/PIXIU/stargazers) - An open-source resource providing a financial large language model, a dataset with 136K instruction samples, and a comprehensive evaluation benchmark.
- [FinGPT](https://github.com/AI4Finance-Foundation/FinGPT) [![GitHub stars](https://img.shields.io/github/stars/AI4Finance-Foundation/FinGPT?style=flat)](https://github.com/AI4Finance-Foundation/FinGPT/stargazers) - Provides a playground for all people interested in LLMs and NLP in Finance.
- [MACD + RSI + ADX Strategy (ChatGPT-powered) by TradeSmart](https://www.tradingview.com/script/GxkUyJKW-MACD-RSI-ADX-Strategy-ChatGPT-powered-by-TradeSmart/ ) - Asked ChatGPT on which indicators are the most popular for trading. We used all of the recommendations given.
- [A ChatGPT trading algorithm delivered 500% returns in stock market. My breakdown on what this means for hedge funds and retail investors](https://www.reddit.com/r/ChatGPT/comments/13duech/a_chatgpt_trading_algorithm_delivered_500_returns/)
- [Use chatgpt to adjust strategy parameters](https://twitter.com/0xUnicorn/status/1663413848593031170)
- [Hands-on LLMs: Train and Deploy a Real-time Financial Advisor](https://github.com/iusztinpaul/hands-on-llms) [![GitHub stars](https://img.shields.io/github/stars/iusztinpaul/hands-on-llms?style=flat)](https://github.com/iusztinpaul/hands-on-llms/stargazers) - Train and deploy a real-time financial advisor chatbot with Falcon 7B and CometLLM.
- [ChatGPT Strategy by OctoBot](https://blog.octobot.online/trading-using-chat-gpt) - Use ChatGPT to determine which cryptocurrency to trade based on technical indicators.
- [LLMs Meet Finance](https://arxiv.org/abs/2504.13125) - A three-stage fine-tuning pipeline (SFT → DPO → synthetic-data RL) that adapts Qwen2.5 and DeepSeek-R1 to financial tasks on the Open FinLLM Leaderboard, with findings on cross-task transfer and data scaling laws in finance.

## Skills

- [XVARY Stock Research](https://github.com/xvary-research/claude-code-stock-analysis-skill) [![GitHub stars](https://img.shields.io/github/stars/xvary-research/claude-code-stock-analysis-skill?style=flat)](https://github.com/xvary-research/claude-code-stock-analysis-skill/stargazers) — Claude Code skill for public SEC EDGAR + market data: `/analyze`, `/score`, `/compare`. MIT.
- [CFA Institute Bias Detection](https://github.com/CFA-Institute-RPC/skills/tree/main/skills/bias-detection) [![GitHub stars](https://img.shields.io/github/stars/CFA-Institute-RPC/skills/tree/main/skills/bias-detection?style=flat)](https://github.com/CFA-Institute-RPC/skills/tree/main/skills/bias-detection/stargazers) - Claude skill for bias detection in investment analysis. Apache 2.0.
- [Ethical Capital Skills](https://github.com/ethicalcapital/skills) [![GitHub stars](https://img.shields.io/github/stars/ethicalcapital/skills?style=flat)](https://github.com/ethicalcapital/skills/stargazers) - Claude skills for investment research, screening, compliance, and marketing workflows.

## Papers

- [The Theory of Speculation L. Bachelier, 1900](http://www.radio.goldseek.com/bachelier-thesis-theory-of-speculation-en.pdf) - The influences which determine the movements of the Stock Exchange are.
- [Brownian Motion in the Stock Market Osborne, 1959](http://m.e-m-h.org/Osbo59.pdf) - The common-stock prices can be regarded as an ensemble of decisions in statistical equilibrium.
- [An Investigation into the Use of Reinforcement Learning Techniques within the Algorithmic Trading Domain, 2015](http://www.doc.ic.ac.uk/teaching/distinguished-projects/2015/j.cumming.pdf)
- [A Deep Reinforcement Learning Framework for the Financial Portfolio Management Problem](https://arxiv.org/pdf/1706.10059.pdf)
- [Reinforcement Learning for Trading, 1994](http://papers.nips.cc/paper/1551-reinforcement-learning-for-trading.pdf)
- [Dragon-Kings, Black Swans and the Prediction of Crises Didier Sornette](https://arxiv.org/pdf/0907.4290.pdf) - The power laws in the distributions of event sizes under a broad range of conditions in a large variety of systems. 
- [Financial Trading as a Game: A Deep Reinforcement Learning Approach](https://arxiv.org/pdf/1807.02787.pdf) - Deep reinforcement learning provides a framework toward end-to-end training of such trading agent.
- [Machine Learning for Trading](https://cims.nyu.edu/~ritter/ritter2017machine.pdf) - With an appropriate choice of the reward function, reinforcement learning techniques can successfully handle the risk-averse case.
- [Ten Financial Applications of Machine Learning, 2018](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3197726) - Slides review few important financial ML applications.
- [FinRL: A Deep Reinforcement Learning Library for Automated Stock Trading in Quantitative Finance, 2020](https://arxiv.org/abs/2011.09607) - Introduce a DRL library FinRL that facilitates beginners to expose themselves to quantitative finance and to develop their own stock trading strategies.
- [Deep Reinforcement Learning for Automated Stock Trading: An Ensemble Strategy, 2020](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3690996) - Propose an ensemble strategy that employs deep reinforcement schemes to learn a stock trading strategy by maximizing investment return.

## Courses & Books & Blogs

- 🌟 [QuantResearch](https://github.com/letianzj/QuantResearch) [![GitHub stars](https://img.shields.io/github/stars/letianzj/QuantResearch?style=flat)](https://github.com/letianzj/QuantResearch/stargazers) - Quantitative analysis, strategies and backtests https://letianzj.github.io/
- [NYU: Overview of Advanced Methods of Reinforcement Learning in Finance](https://www.coursera.org/learn/advanced-methods-reinforcement-learning-finance/home/welcome)
- [Udacity: Artificial Intelligence for Trading](https://www.udacity.com/course/ai-for-trading--nd880)
- [AI in Finance](https://cfte.education/) - Learn Fintech Online.
- [The Automation Ahead](https://github.com/CFA-Institute-RPC/The-Automation-Ahead) [![GitHub stars](https://img.shields.io/github/stars/CFA-Institute-RPC/The-Automation-Ahead?style=flat)](https://github.com/CFA-Institute-RPC/The-Automation-Ahead/stargazers) - CFA Institute examples for GenAI-driven investment workflows.
- [Advanced-Deep-Trading](https://github.com/Rachnog/Advanced-Deep-Trading) [![GitHub stars](https://img.shields.io/github/stars/Rachnog/Advanced-Deep-Trading?style=flat)](https://github.com/Rachnog/Advanced-Deep-Trading/stargazers) - Experiments based on "Advances in financial machine learning" book.
- [Advances in Financial Machine Learning](https://www.amazon.com/Advances-Financial-Machine-Learning-Marcos-ebook/dp/B079KLDW21/ref=sr_1_1?s=books&ie=UTF8&qid=1541717436&sr=1-1) - Using advanced ML solutions to overcome real-world investment problems.
- [Build Financial Software with Generative AI](https://www.manning.com/books/build-financial-software-with-generative-ai?ar=false&lpse=B&) - Book about how to build financial software hands-on using generative AI tools like ChatGPT and Copilot.
- [Financial AI in Practice](https://www.manning.com/books/financial-ai-in-practice) - A book about creating profitable, regulation-compliant financial applications.
- [Investing for Programmers](https://www.manning.com/books/investing-for-programmers) - A book about maximizing your portfolio, analyzing markets, and making data-driven investment decisions using Python and generative AI
- [Mastering Python for Finance](https://github.com/jamesmawm/mastering-python-for-finance-second-edition) [![GitHub stars](https://img.shields.io/github/stars/jamesmawm/mastering-python-for-finance-second-edition?style=flat)](https://github.com/jamesmawm/mastering-python-for-finance-second-edition/stargazers) - Sources codes for: Mastering Python for Finance, Second Edition.
- [MLSys-NYU-2022](https://github.com/jacopotagliabue/MLSys-NYU-2022/tree/main) [![GitHub stars](https://img.shields.io/github/stars/jacopotagliabue/MLSys-NYU-2022/tree/main?style=flat)](https://github.com/jacopotagliabue/MLSys-NYU-2022/tree/main/stargazers) - Slides, scripts and materials for the Machine Learning in Finance course at NYU Tandon, 2022.
- [Train and Deploy a Serverless API to predict crypto prices](https://github.com/Paulescu/hands-on-train-and-deploy-ml) [![GitHub stars](https://img.shields.io/github/stars/Paulescu/hands-on-train-and-deploy-ml?style=flat)](https://github.com/Paulescu/hands-on-train-and-deploy-ml/stargazers) - In this tutorial you won't build an ML system that will make you rich. But you will master the MLOps frameworks and tools you need to build ML systems that, together with tons of experimentation, can take you there.
- [KeepRule](https://keeprule.com) - AI-powered investment discipline platform with principles from 26 legendary investors including Buffett, Munger, and Dalio.

## Strategies & Research

### Time Series Data

Price and Volume process with Technology Analysis Indices

- 🌟🌟 [stockpredictionai](https://github.com/borisbanushev/stockpredictionai) [![GitHub stars](https://img.shields.io/github/stars/borisbanushev/stockpredictionai?style=flat)](https://github.com/borisbanushev/stockpredictionai/stargazers) - A complete process for predicting stock price movements.
- 🌟 [Personae](https://github.com/Ceruleanacg/Personae) [![GitHub stars](https://img.shields.io/github/stars/Ceruleanacg/Personae?style=flat)](https://github.com/Ceruleanacg/Personae/stargazers) - Implements and environment of Deep Reinforcement Learning & Supervised Learning for Quantitative Trading.
- 🌟 [Ensemble-Strategy](https://github.com/AI4Finance-LLC/Deep-Reinforcement-Learning-for-Automated-Stock-Trading-Ensemble-Strategy-ICAIF-2020) [![GitHub stars](https://img.shields.io/github/stars/AI4Finance-LLC/Deep-Reinforcement-Learning-for-Automated-Stock-Trading-Ensemble-Strategy-ICAIF-2020?style=flat)](https://github.com/AI4Finance-LLC/Deep-Reinforcement-Learning-for-Automated-Stock-Trading-Ensemble-Strategy-ICAIF-2020/stargazers) - Deep Reinforcement Learning for Automated Stock Trading.
- [FinRL](https://github.com/AI4Finance-LLC/FinRL-Library) [![GitHub stars](https://img.shields.io/github/stars/AI4Finance-LLC/FinRL-Library?style=flat)](https://github.com/AI4Finance-LLC/FinRL-Library/stargazers) - A Deep Reinforcement Learning Library for Automated Stock Trading in Quantitative Finance.
- [AutomatedStockTrading-DeepQ-Learning](https://github.com/sachink2010/AutomatedStockTrading-DeepQ-Learning) [![GitHub stars](https://img.shields.io/github/stars/sachink2010/AutomatedStockTrading-DeepQ-Learning?style=flat)](https://github.com/sachink2010/AutomatedStockTrading-DeepQ-Learning/stargazers) - Build a Deep Q-learning reinforcement agent model as automated trading robot.
- [tf_deep_rl_trader](https://github.com/miroblog/tf_deep_rl_trader) [![GitHub stars](https://img.shields.io/github/stars/miroblog/tf_deep_rl_trader?style=flat)](https://github.com/miroblog/tf_deep_rl_trader/stargazers) - Trading environment(OpenAI Gym) + PPO(TensorForce).
- [trading-gym](https://github.com/6-Billionaires/trading-gym) [![GitHub stars](https://img.shields.io/github/stars/6-Billionaires/trading-gym?style=flat)](https://github.com/6-Billionaires/trading-gym/stargazers) - Trading agent to train with episode of short term trading itself.
- [trading-rl](https://github.com/Kostis-S-Z/trading-rl) [![GitHub stars](https://img.shields.io/github/stars/Kostis-S-Z/trading-rl?style=flat)](https://github.com/Kostis-S-Z/trading-rl/stargazers) - Deep Reinforcement Learning for Financial Trading using Price Trailing.
- [deep_rl_trader](https://github.com/miroblog/deep_rl_trader) [![GitHub stars](https://img.shields.io/github/stars/miroblog/deep_rl_trader?style=flat)](https://github.com/miroblog/deep_rl_trader/stargazers) - Trading environment(OpenAI Gym) + DDQN (Keras-RL).
- [Quantitative-Trading](https://github.com/Ceruleanacg/Quantitative-Trading) [![GitHub stars](https://img.shields.io/github/stars/Ceruleanacg/Quantitative-Trading?style=flat)](https://github.com/Ceruleanacg/Quantitative-Trading/stargazers) - Papers and code implementing Quantitative-Trading.
- [gym-trading](https://github.com/hackthemarket/gym-trading) [![GitHub stars](https://img.shields.io/github/stars/hackthemarket/gym-trading?style=flat)](https://github.com/hackthemarket/gym-trading/stargazers) - Environment for reinforcement-learning algorithmic trading models.
- [zenbrain](https://github.com/carlos8f/zenbrain) [![GitHub stars](https://img.shields.io/github/stars/carlos8f/zenbrain?style=flat)](https://github.com/carlos8f/zenbrain/stargazers) - A framework for machine-learning bots.
- [DeepLearningNotes](https://github.com/AlphaSmartDog/DeepLearningNotes) [![GitHub stars](https://img.shields.io/github/stars/AlphaSmartDog/DeepLearningNotes?style=flat)](https://github.com/AlphaSmartDog/DeepLearningNotes/stargazers) - Machine learning in quant analysis.
- [stock_market_reinforcement_learning](https://github.com/kh-kim/stock_market_reinforcement_learning) [![GitHub stars](https://img.shields.io/github/stars/kh-kim/stock_market_reinforcement_learning?style=flat)](https://github.com/kh-kim/stock_market_reinforcement_learning/stargazers) - Stock market trading OpenAI Gym environment with Deep Reinforcement Learning using Keras.
- [Chaos Genius](https://github.com/chaos-genius/chaos_genius) [![GitHub stars](https://img.shields.io/github/stars/chaos-genius/chaos_genius?style=flat)](https://github.com/chaos-genius/chaos_genius/stargazers) - ML powered analytics engine for outlier/anomaly detection and root cause analysis..
- [mlforecast](https://github.com/Nixtla/mlforecast) [![GitHub stars](https://img.shields.io/github/stars/Nixtla/mlforecast?style=flat)](https://github.com/Nixtla/mlforecast/stargazers) - Scalable machine learning based time series forecasting.
- [patternity](https://github.com/quantium-ai/patternity) [![GitHub stars](https://img.shields.io/github/stars/quantium-ai/patternity?style=flat)](https://github.com/quantium-ai/patternity/stargazers) - Deterministic algorithm for stock price prediction, focusing on pattern recognition in historical data.
- [Quantium Research](https://github.com/quantium-ai/research) [![GitHub stars](https://img.shields.io/github/stars/quantium-ai/research?style=flat)](https://github.com/quantium-ai/research/stargazers) - Research experiments exploring uncommon quant techniques.

### Portfolio Management

- [Deep-Reinforcement-Stock-Trading](https://github.com/Albert-Z-Guo/Deep-Reinforcement-Stock-Trading) [![GitHub stars](https://img.shields.io/github/stars/Albert-Z-Guo/Deep-Reinforcement-Stock-Trading?style=flat)](https://github.com/Albert-Z-Guo/Deep-Reinforcement-Stock-Trading/stargazers) - A light-weight deep reinforcement learning framework for portfolio management.
- [qtrader](https://github.com/filangel/qtrader) [![GitHub stars](https://img.shields.io/github/stars/filangel/qtrader?style=flat)](https://github.com/filangel/qtrader/stargazers) - Reinforcement Learning for portfolio management.
- [PGPortfolio](https://github.com/ZhengyaoJiang/PGPortfolio) [![GitHub stars](https://img.shields.io/github/stars/ZhengyaoJiang/PGPortfolio?style=flat)](https://github.com/ZhengyaoJiang/PGPortfolio/stargazers) - A Deep Reinforcement Learning framework for the financial portfolio management problem.
- [DeepDow](https://github.com/jankrepl/deepdow) [![GitHub stars](https://img.shields.io/github/stars/jankrepl/deepdow?style=flat)](https://github.com/jankrepl/deepdow/stargazers) - Portfolio optimization with deep learning.
- [skfolio](https://github.com/skfolio/skfolio) [![GitHub stars](https://img.shields.io/github/stars/skfolio/skfolio?style=flat)](https://github.com/skfolio/skfolio/stargazers) - Python library for portfolio optimization built on top of scikit-learn.

### High Frequency Trading

- [High-Frequency-Trading-Model-with-IB](https://github.com/jamesmawm/High-Frequency-Trading-Model-with-IB) [![GitHub stars](https://img.shields.io/github/stars/jamesmawm/High-Frequency-Trading-Model-with-IB?style=flat)](https://github.com/jamesmawm/High-Frequency-Trading-Model-with-IB/stargazers) - A high-frequency trading model using Interactive Brokers API with pairs and mean-reversion.
- 🌟 [SGX-Full-OrderBook-Tick-Data-Trading-Strategy](https://github.com/rorysroes/SGX-Full-OrderBook-Tick-Data-Trading-Strategy) [![GitHub stars](https://img.shields.io/github/stars/rorysroes/SGX-Full-OrderBook-Tick-Data-Trading-Strategy?style=flat)](https://github.com/rorysroes/SGX-Full-OrderBook-Tick-Data-Trading-Strategy/stargazers) - Solutions for high-frequency trading (HFT) strategies using data science approaches (Machine Learning) on Full Orderbook Tick Data.
- [HFT_Bitcoin](https://github.com/ghgr/HFT_Bitcoin) [![GitHub stars](https://img.shields.io/github/stars/ghgr/HFT_Bitcoin?style=flat)](https://github.com/ghgr/HFT_Bitcoin/stargazers) - Analysis of High Frequency Trading on Bitcoin exchanges.

### Event Drive

- 🌟🌟 [stockpredictionai](https://github.com/borisbanushev/stockpredictionai) [![GitHub stars](https://img.shields.io/github/stars/borisbanushev/stockpredictionai?style=flat)](https://github.com/borisbanushev/stockpredictionai/stargazers) - Complete process for predicting stock price movements.
- 🌟 [trump2cash](https://github.com/maxbbraun/trump2cash) [![GitHub stars](https://img.shields.io/github/stars/maxbbraun/trump2cash?style=flat)](https://github.com/maxbbraun/trump2cash/stargazers) - A stock trading bot powered by Trump tweets.

### Crypto Currencies Strategies

- [LSTM-Crypto-Price-Prediction](https://github.com/SC4RECOIN/LSTM-Crypto-Price-Prediction) [![GitHub stars](https://img.shields.io/github/stars/SC4RECOIN/LSTM-Crypto-Price-Prediction?style=flat)](https://github.com/SC4RECOIN/LSTM-Crypto-Price-Prediction/stargazers) - Predicting price trends in crypto markets using an LSTM-RNN for trading.
- [tforce_btc_trader](https://github.com/lefnire/tforce_btc_trader) [![GitHub stars](https://img.shields.io/github/stars/lefnire/tforce_btc_trader?style=flat)](https://github.com/lefnire/tforce_btc_trader/stargazers) - TensorForce Bitcoin trading bot.
- [Tensorflow-NeuroEvolution-Trading-Bot](https://github.com/SC4RECOIN/Tensorflow-NeuroEvolution-Trading-Bot) [![GitHub stars](https://img.shields.io/github/stars/SC4RECOIN/Tensorflow-NeuroEvolution-Trading-Bot?style=flat)](https://github.com/SC4RECOIN/Tensorflow-NeuroEvolution-Trading-Bot/stargazers) - A population model that trade cyrpto and breed and mutate iteratively.
- [gekkoga](https://github.com/gekkowarez/gekkoga) [![GitHub stars](https://img.shields.io/github/stars/gekkowarez/gekkoga?style=flat)](https://github.com/gekkowarez/gekkoga/stargazers) - Genetic algorithm for solving optimization of trading strategies using Gekko.
- [Gekko_ANN_Strategies](https://github.com/markchen8717/Gekko_ANN_Strategies) [![GitHub stars](https://img.shields.io/github/stars/markchen8717/Gekko_ANN_Strategies?style=flat)](https://github.com/markchen8717/Gekko_ANN_Strategies/stargazers) - ANN trading strategies for the Gekko trading bot.
- [gekko-neuralnet](https://github.com/zschro/gekko-neuralnet) [![GitHub stars](https://img.shields.io/github/stars/zschro/gekko-neuralnet?style=flat)](https://github.com/zschro/gekko-neuralnet/stargazers) - Neural network strategy for Gekko.
- [bitcoin_prediction](https://github.com/llSourcell/bitcoin_prediction) [![GitHub stars](https://img.shields.io/github/stars/llSourcell/bitcoin_prediction?style=flat)](https://github.com/llSourcell/bitcoin_prediction/stargazers) - Code for "Bitcoin Prediction" by Siraj Raval on YouTube.
- [DeepAlpha](https://github.com/stefanoviana/deepalpha) [![GitHub stars](https://img.shields.io/github/stars/stefanoviana/deepalpha?style=flat)](https://github.com/stefanoviana/deepalpha/stargazers) - AI-powered crypto trading bot with 3-model ML ensemble (XGBoost, LightGBM, CatBoost), 12 exchanges via CCXT, walk-forward validated.

### Technical Analysis

- [QTradeX](https://github.com/squidKid-deluxe/QTradeX-Algo-Trading-SDK) [![GitHub stars](https://img.shields.io/github/stars/squidKid-deluxe/QTradeX-Algo-Trading-SDK?style=flat)](https://github.com/squidKid-deluxe/QTradeX-Algo-Trading-SDK/stargazers) - A powerful and flexible Python framework for designing, backtesting, optimizing, and deploying algotrading bots
- [quant-trading](https://github.com/je-suis-tm/quant-trading) [![GitHub stars](https://img.shields.io/github/stars/je-suis-tm/quant-trading?style=flat)](https://github.com/je-suis-tm/quant-trading/stargazers) - Python quantitative trading strategies.
- [Gekko-Bot-Resources](https://github.com/cloggy45/Gekko-Bot-Resources) [![GitHub stars](https://img.shields.io/github/stars/cloggy45/Gekko-Bot-Resources?style=flat)](https://github.com/cloggy45/Gekko-Bot-Resources/stargazers) - Gekko bot resources.
- [gekko_tools](https://github.com/tommiehansen/gekko_tools) [![GitHub stars](https://img.shields.io/github/stars/tommiehansen/gekko_tools?style=flat)](https://github.com/tommiehansen/gekko_tools/stargazers) - Gekko strategies, tools etc.
- [gekko RSI_WR](https://github.com/zzmike76/gekko) [![GitHub stars](https://img.shields.io/github/stars/zzmike76/gekko?style=flat)](https://github.com/zzmike76/gekko/stargazers) - Gekko RSI_WR strategies.
- [gekko HL](https://github.com/mounirlabaied/gekko-strat-hl) [![GitHub stars](https://img.shields.io/github/stars/mounirlabaied/gekko-strat-hl?style=flat)](https://github.com/mounirlabaied/gekko-strat-hl/stargazers) - Calculate down peak and trade on.
- [EthTradingAlgorithm](https://github.com/Philipid3s/EthTradingAlgorithm) [![GitHub stars](https://img.shields.io/github/stars/Philipid3s/EthTradingAlgorithm?style=flat)](https://github.com/Philipid3s/EthTradingAlgorithm/stargazers) - Ethereum trading algorithm using Python 3.5 and the library ZipLine.
- [gekko_trading_stuff](https://github.com/thegamecat/gekko-trading-stuff) [![GitHub stars](https://img.shields.io/github/stars/thegamecat/gekko-trading-stuff?style=flat)](https://github.com/thegamecat/gekko-trading-stuff/stargazers) - Awesome crypto currency trading platform.
- [forex.analytics](https://github.com/mkmarek/forex.analytics) [![GitHub stars](https://img.shields.io/github/stars/mkmarek/forex.analytics?style=flat)](https://github.com/mkmarek/forex.analytics/stargazers) - Node.js native library performing technical analysis over an OHLC dataset with use of genetic algorithmv.
- [Bitcoin_MACD_Strategy](https://github.com/VermeirJellen/Bitcoin_MACD_Strategy) [![GitHub stars](https://img.shields.io/github/stars/VermeirJellen/Bitcoin_MACD_Strategy?style=flat)](https://github.com/VermeirJellen/Bitcoin_MACD_Strategy/stargazers) - Bitcoin MACD crossover trading strategy backtest.
- [crypto-signal](https://github.com/CryptoSignal/crypto-signal) [![GitHub stars](https://img.shields.io/github/stars/CryptoSignal/crypto-signal?style=flat)](https://github.com/CryptoSignal/crypto-signal/stargazers) - Automated crypto trading & technical analysis (TA) bot for Bittrex, Binance, GDAX, and more.
- [Gekko-Strategies](https://github.com/xFFFFF/Gekko-Strategies) [![GitHub stars](https://img.shields.io/github/stars/xFFFFF/Gekko-Strategies?style=flat)](https://github.com/xFFFFF/Gekko-Strategies/stargazers) - Strategies to Gekko trading bot with backtests results and some useful tools.
- [gekko-gannswing](https://github.com/johndoe75/gekko-gannswing) [![GitHub stars](https://img.shields.io/github/stars/johndoe75/gekko-gannswing?style=flat)](https://github.com/johndoe75/gekko-gannswing/stargazers) - Gann's Swing trade strategy for Gekko trade bot.
- [Chartscout](https://chartscout.io) - Real-time cryptocurrency chart pattern detection with automated alerts using pattern recognition algorithms
* [MarginSafe.ai](https://marginsafe.ai) - AI stock analysis platform specialized in intrinsic value and Wyckoff timing.

### Lottery & Gamble

- [LotteryPredict](https://github.com/chengstone/LotteryPredict) [![GitHub stars](https://img.shields.io/github/stars/chengstone/LotteryPredict?style=flat)](https://github.com/chengstone/LotteryPredict/stargazers) - Use LSTM to predict lottery.

### Arbitrage

- [ArbitrageBot](https://github.com/BatuhanUsluel/ArbitrageBot) [![GitHub stars](https://img.shields.io/github/stars/BatuhanUsluel/ArbitrageBot?style=flat)](https://github.com/BatuhanUsluel/ArbitrageBot/stargazers) - Arbitrage bot that currently works on bittrex & poloniex.
- [r2](https://github.com/bitrinjani/r2) [![GitHub stars](https://img.shields.io/github/stars/bitrinjani/r2?style=flat)](https://github.com/bitrinjani/r2/stargazers) - Automatic arbitrage trading system powered by Node.js + TypeScript.
- [cryptocurrency-arbitrage](https://github.com/manu354/cryptocurrency-arbitrage) [![GitHub stars](https://img.shields.io/github/stars/manu354/cryptocurrency-arbitrage?style=flat)](https://github.com/manu354/cryptocurrency-arbitrage/stargazers) - A crypto currency arbitrage opportunity calculator. Over 800 currencies and 50 markets.
- [bitcoin-arbitrage](https://github.com/maxme/bitcoin-arbitrage) [![GitHub stars](https://img.shields.io/github/stars/maxme/bitcoin-arbitrage?style=flat)](https://github.com/maxme/bitcoin-arbitrage/stargazers) - Bitcoin arbitrage opportunity detector.
- [blackbird](https://github.com/butor/blackbird) [![GitHub stars](https://img.shields.io/github/stars/butor/blackbird?style=flat)](https://github.com/butor/blackbird/stargazers) - Long / short market-neutral strategy.

## Data Sources

#### Traditional Markets

- 🌟 [Quandl](https://www.quandl.com/tools/api) - Get millions of financial and economic dataset from hundreds of publishers via a single free API.
- [yahoo-finance](https://github.com/lukaszbanasiak/yahoo-finance) [![GitHub stars](https://img.shields.io/github/stars/lukaszbanasiak/yahoo-finance?style=flat)](https://github.com/lukaszbanasiak/yahoo-finance/stargazers) - Python module to get stock data from Yahoo! Finance.
- [Tushare](https://github.com/waditu/tushare) [![GitHub stars](https://img.shields.io/github/stars/waditu/tushare?style=flat)](https://github.com/waditu/tushare/stargazers) - TuShare is a utility for crawling historical data of China stocks.
- [Congressional Stock Brain](https://congressionalstockbrain.com) - Free AI-powered tool that scores U.S. STOCK Act congressional trade disclosures by significance. Committee weighting, timing analysis, 537 members tracked.
- [Financial Data](https://financialdata.net/) - Stock Market and Financial Data API.
- [FinanceKit MCP](https://github.com/vdalhambra/financekit-mcp) [![GitHub stars](https://img.shields.io/github/stars/vdalhambra/financekit-mcp?style=flat)](https://github.com/vdalhambra/financekit-mcp/stargazers) - MCP server for stock quotes, technical analysis, crypto data, risk metrics, and portfolio analysis. No API keys for core data.
- [Tapetide](https://tapetide.com) - Indian market data API and MCP server for NSE/BSE stocks, financials, screeners, and institutional flows.
- [FXMacroData](https://fxmacrodata.com) - Macroeconomic and FX data API with central bank announcements, policy rates, inflation, employment, GDP, release calendars, and MCP access for 18 currencies.
- [StockAInsights](https://stockainsights.com) - Institutional-grade financial statements API with AI extraction from SEC filings — not XBRL. Covers domestic and foreign filers (20-F, 6-K, 40-F), normalized quarterly and annual data.
- [13F Insight](https://13finsight.com) - AI-powered 13F SEC filing tracker. Monitor hedge fund and institutional investor portfolio changes, with smart money move alerts and historical holding comparisons.
- [ValueRay](https://www.valueray.com/api) - Technical, quantitative and sentiment data for stocks and ETFs with risk metrics, peer percentiles and market regime signals. Optimized for AI/LLM agents.
- [BenchGecko](https://benchgecko.ai) - AI economy tracking platform. Market cap, funding rounds, AI Bubble Index, company valuations, and compute supply chain data.
- [FilingFirehose](https://filingfirehose.com) - SEC EDGAR JSON API with classified 8-Ks, activist 13D/G tagging, ATM offering detection, and hosted MCP access.

#### Crypto Currencies

- [BitBank.nz](https://bitbank.nz) - AI-powered crypto forecasting and predictions API with machine learning models for 70+ cryptocurrency pairs.
- [CryptoInscriber](https://github.com/Optixal/CryptoInscriber) [![GitHub stars](https://img.shields.io/github/stars/Optixal/CryptoInscriber?style=flat)](https://github.com/Optixal/CryptoInscriber/stargazers) - A live crypto currency historical trade data blotter. Download live historical trade data from any crypto exchange.
- [CoinPulse](https://github.com/soutone/coinpulse-python) [![GitHub stars](https://img.shields.io/github/stars/soutone/coinpulse-python?style=flat)](https://github.com/soutone/coinpulse-python/stargazers) - Python SDK for cryptocurrency portfolio tracking with real-time prices, P/L calculations, backtesting, and price alerts. Free tier: 25 req/hr.
- [Gekko-Datasets](https://github.com/xFFFFF/Gekko-Datasets) [![GitHub stars](https://img.shields.io/github/stars/xFFFFF/Gekko-Datasets?style=flat)](https://github.com/xFFFFF/Gekko-Datasets/stargazers) - Gekko trading bot dataset dumps. Download and use history files in SQLite format.
- [Frostbyte Crypto API](https://agent-gateway-kappa.vercel.app) - Free real-time cryptocurrency price data API. Supports BTC, ETH, SOL, and 20+ tokens. No signup or API key required for basic endpoints. JSON responses with price, 24h change, market cap, and volume.
- [CoinPaprika API](https://api.coinpaprika.com) - Free cryptocurrency market data API with prices, volume, market cap, and OHLCV for 7,000+ coins. No API key required. Includes MCP server for AI agent integration.
- [DexPaprika API](https://api.dexpaprika.com) - Free DEX and DeFi data API — real-time pool data, token prices, OHLCV, and trade history across all chains. No API key, no rate limits. Includes MCP server for AI agents.
- [Philidor](https://docs.philidor.io/docs) - Institutional-grade DeFi risk scoring for 700+ vaults across 9 protocols and 6 chains. REST API and MCP server (Claude, Cursor, Windsurf). Deterministic 0–10 risk scores, tiers (Prime/Core/Edge), portfolio analysis, oracle monitoring. No API key required.
- [PreReason](https://www.prereason.com) - Pre-analyzed financial market briefings optimized for AI agent consumption. 17 briefings covering BTC on-chain, macro (Fed balance sheet, M2, Treasury yields), and cross-asset correlations. Returns regime classification, trend signals, and confidence scores in markdown.
- [Satoshi API](https://github.com/Bortlesboat/bitcoin-api) [![GitHub stars](https://img.shields.io/github/stars/Bortlesboat/bitcoin-api?style=flat)](https://github.com/Bortlesboat/bitcoin-api/stargazers) - Bitcoin fee intelligence API with 108 endpoints for fee estimates, mempool analysis, block data, and mining stats. Self-hostable, Apache 2.0.
- [Sharpe](https://www.sharpe.ai/docs/free-api) - Agent-ready crypto market intelligence API and MCP server for funding, derivatives, arbitrage, narratives, listings, and news.
- [TBD Predict](https://github.com/ego-protocol/tbd-vote-cli) [![GitHub stars](https://img.shields.io/github/stars/ego-protocol/tbd-vote-cli?style=flat)](https://github.com/ego-protocol/tbd-vote-cli/stargazers) - Solana-based prediction market for human opinions with an agent CLI and AGENTS.md spec for AI agents to authenticate, list opinion campaigns, and place bets via JSON-friendly commands.

#### News Data

- [WorldMonitor](https://github.com/koala73/worldmonitor) [![GitHub stars](https://img.shields.io/github/stars/koala73/worldmonitor?style=flat)](https://github.com/koala73/worldmonitor/stargazers) - AI-powered news aggregation, geopolitical monitoring, and infrastructure tracking in a unified situational awareness interface.

#### Alternative Data

- [Adanos Market Sentiment API](https://api.adanos.org/docs/) - Market sentiment API for AI finance agents covering stocks across Reddit, X/Twitter, news, and Polymarket prediction markets with buzz, sentiment, trending, and comparison signals.
- [Pizzint](https://www.pizzint.watch/) - Pentagon Pizza Index (PizzINT) is a real-time Pentagon pizza tracker that visualizes unusual activity at Pentagon-area pizzerias. It highlights a signal that has historically aligned with late-night, high-tempo operations and breaking news.

#### Prediction Markets

- [Parsec API](https://docs.parsecapi.com) - Unified prediction market infrastructure for normalized data, execution, and live streams across Polymarket, Kalshi, Opinion, Limitless, and PredictFun. MCP server for AI agent trading. Generous free tier.
- [PolyMind](https://polyminds.netlify.app/) - Real-time Polymarket trading alerts with multi-AI analysis (Groq, Claude, Gemini). Track whale bets, volume spikes, coordinated wallets, and 12 signal types. Free tier available.

## Research Tools

- [Synthical](https://synthical.com) - AI-powered collaborative environment for Research.
- 🌟🌟 [TensorTrade](https://github.com/tensortrade-org/tensortrade) [![GitHub stars](https://img.shields.io/github/stars/tensortrade-org/tensortrade?style=flat)](https://github.com/tensortrade-org/tensortrade/stargazers) - Trade efficiently with reinforcement learning.
- [ML-Quant](https://www.ml-quant.com/) - Quant resources from ArXiv (sanity), SSRN, RePec, Journals, Podcasts, Videos, and Blogs.
- [JAQS](https://github.com/quantOS-org/JAQS) [![GitHub stars](https://img.shields.io/github/stars/quantOS-org/JAQS?style=flat)](https://github.com/quantOS-org/JAQS/stargazers) - An open source quant strategies research platform.
- [pyfolio](https://github.com/quantopian/pyfolio) [![GitHub stars](https://img.shields.io/github/stars/quantopian/pyfolio?style=flat)](https://github.com/quantopian/pyfolio/stargazers) - Portfolio and risk analytics in Python.
- [alphalens](https://github.com/quantopian/alphalens) [![GitHub stars](https://img.shields.io/github/stars/quantopian/alphalens?style=flat)](https://github.com/quantopian/alphalens/stargazers) - Performance analysis of predictive (alpha) stock factors.
- [empyrical](https://github.com/quantopian/empyrical) [![GitHub stars](https://img.shields.io/github/stars/quantopian/empyrical?style=flat)](https://github.com/quantopian/empyrical/stargazers) - Common financial risk and performance metrics. Used by Zipline and pyfolio.
- [zvt](https://github.com/zvtvz/zvt) [![GitHub stars](https://img.shields.io/github/stars/zvtvz/zvt?style=flat)](https://github.com/zvtvz/zvt/stargazers) - Zero vector trader.
- [CongressionalStockBrain](https://congressionalstockbrain.com) - AI-powered tool that ingests U.S. STOCK Act congressional trade disclosures and converts them into machine-scored signals for retail investors.
- [WalletLens](https://walletlens.live) - Multi-asset portfolio tracker with AI insights, technical analysis, live prices, and local-first data storage.
- [WFGY](https://github.com/onestardao/WFGY) [![GitHub stars](https://img.shields.io/github/stars/onestardao/WFGY?style=flat)](https://github.com/onestardao/WFGY/stargazers) – Open source framework for debugging and stress testing LLM agents and RAG pipelines. Includes a 16 mode failure map and long-horizon stress tests that are useful for financial research agents.
- [ChainPulse](https://github.com/Bortlesboat/chainpulse) [![GitHub stars](https://img.shields.io/github/stars/Bortlesboat/chainpulse?style=flat)](https://github.com/Bortlesboat/chainpulse/stargazers) - AI-powered Bitcoin network intelligence CLI for natural language queries on mempool, fees, blocks, and mining analysis.
- [CRNG](https://github.com/brotto/crng) [![GitHub stars](https://img.shields.io/github/stars/brotto/crng?style=flat)](https://github.com/brotto/crng/stargazers) - Contingency RNG, generates random numbers with real market fat tails (K=5-220) and volatility clustering. Matches 86% of real market metrics vs 14% for NumPy. Includes regime detector.
- [Chart Library](https://chartlibrary.io) - Visual chart pattern search engine. Upload a screenshot or type a ticker+date to find the 10 most similar historical chart patterns and see what happened next. 24M+ embeddings, 19K symbols, REST API + MCP server.
- [Coinugget](https://coinugget.com) - Real-time RSI signals, price action & volume spikes dashboard for crypto traders. Free, no sign-up required.

## Trading System

For Back Test & Live trading

### Traditional Market

**System**

- [the0](https://github.com/alexanderwanyoike/the0) [![GitHub stars](https://img.shields.io/github/stars/alexanderwanyoike/the0?style=flat)](https://github.com/alexanderwanyoike/the0/stargazers) - Self-hosted execution engine for algorithmic trading bots. Supports Python, TypeScript, Rust, C++, C#, Scala, and Haskell. Each bot runs in an isolated container with scheduled or streaming execution.
- 🌟🌟🌟 [OpenBB](https://github.com/OpenBB-finance/OpenBB) [![GitHub stars](https://img.shields.io/github/stars/OpenBB-finance/OpenBB?style=flat)](https://github.com/OpenBB-finance/OpenBB/stargazers) - AI-powered opensource research and analytics workspace.
- 🌟🌟 [zipline](https://github.com/quantopian/zipline) [![GitHub stars](https://img.shields.io/github/stars/quantopian/zipline?style=flat)](https://github.com/quantopian/zipline/stargazers) - A python algorithmic trading library.
- 🌟 [TradingView](http://tradingview.com/) - Get real-time information and market insights.
- [rqalpha](https://github.com/ricequant/rqalpha) [![GitHub stars](https://img.shields.io/github/stars/ricequant/rqalpha?style=flat)](https://github.com/ricequant/rqalpha/stargazers) - A extendable, replaceable Python algorithmic backtest & trading framework.
- [backtrader](https://github.com/backtrader/backtrader) [![GitHub stars](https://img.shields.io/github/stars/backtrader/backtrader?style=flat)](https://github.com/backtrader/backtrader/stargazers) - Python backtesting library for trading strategies.
- [kungfu](https://github.com/taurusai/kungfu) [![GitHub stars](https://img.shields.io/github/stars/taurusai/kungfu?style=flat)](https://github.com/taurusai/kungfu/stargazers) - Kungfu Master trading system.
- [finclaw](https://github.com/NeuZhou/finclaw) [![GitHub stars](https://img.shields.io/github/stars/NeuZhou/finclaw?style=flat)](https://github.com/NeuZhou/finclaw/stargazers) - AI-native quantitative trading engine with 484 alpha factors, genetic algorithm strategy evolution, walk-forward backtesting and paper trading. Supports A-shares, crypto, and MCP server for AI agent integration.
- [lean](https://github.com/QuantConnect/Lean) [![GitHub stars](https://img.shields.io/github/stars/QuantConnect/Lean?style=flat)](https://github.com/QuantConnect/Lean/stargazers) - Algorithmic trading engine built for easy strategy research, backtesting and live trading.

**Combine & Rebuild**

- [pylivetrader](https://github.com/alpacahq/pylivetrader) [![GitHub stars](https://img.shields.io/github/stars/alpacahq/pylivetrader?style=flat)](https://github.com/alpacahq/pylivetrader/stargazers) - Python live trade execution library with zipline interface.
- [CoinMarketCapBacktesting](https://github.com/JimmyWuMadchester/CoinMarketCapBacktesting) [![GitHub stars](https://img.shields.io/github/stars/JimmyWuMadchester/CoinMarketCapBacktesting?style=flat)](https://github.com/JimmyWuMadchester/CoinMarketCapBacktesting/stargazers) - As backtest frameworks for coin trading strategy.

### Crypto Currencies

- [zenbot](https://github.com/DeviaVir/zenbot) [![GitHub stars](https://img.shields.io/github/stars/DeviaVir/zenbot?style=flat)](https://github.com/DeviaVir/zenbot/stargazers) - Command-line crypto currency trading bot using Node.js and MongoDB.
- [bot18](https://github.com/carlos8f/bot18) [![GitHub stars](https://img.shields.io/github/stars/carlos8f/bot18?style=flat)](https://github.com/carlos8f/bot18/stargazers) - High-frequency crypto currency trading bot developed by Zenbot.
- [magic8bot](https://github.com/magic8bot/magic8bot) [![GitHub stars](https://img.shields.io/github/stars/magic8bot/magic8bot?style=flat)](https://github.com/magic8bot/magic8bot/stargazers) - Crypto currency trading bot using Node.js and MongoDB.
- [catalyst](https://github.com/enigmampc/catalyst) [![GitHub stars](https://img.shields.io/github/stars/enigmampc/catalyst?style=flat)](https://github.com/enigmampc/catalyst/stargazers) - An algorithmic trading library for Crypto-Assets in python.
- [QuantResearchDev](https://github.com/mounirlabaied/QuantResearchDev) [![GitHub stars](https://img.shields.io/github/stars/mounirlabaied/QuantResearchDev?style=flat)](https://github.com/mounirlabaied/QuantResearchDev/stargazers) - Quant Research dev & Traders open source project.
- [MACD](https://github.com/sudoscripter/MACD) [![GitHub stars](https://img.shields.io/github/stars/sudoscripter/MACD?style=flat)](https://github.com/sudoscripter/MACD/stargazers) - Zenbot MACD Auto-Trader.
- [abu](https://github.com/bbfamily/abu) [![GitHub stars](https://img.shields.io/github/stars/bbfamily/abu?style=flat)](https://github.com/bbfamily/abu/stargazers) - A quant trading system base on python.

#### Plugins

- [CoinMarketCapBacktesting](https://github.com/JimmyWuMadchester/CoinMarketCapBacktesting) [![GitHub stars](https://img.shields.io/github/stars/JimmyWuMadchester/CoinMarketCapBacktesting?style=flat)](https://github.com/JimmyWuMadchester/CoinMarketCapBacktesting/stargazers) - Tests bt and Quantopian Zipline as backtesting frameworks for coin trading strategy.
- [Gekko-BacktestTool](https://github.com/xFFFFF/Gekko-BacktestTool) [![GitHub stars](https://img.shields.io/github/stars/xFFFFF/Gekko-BacktestTool?style=flat)](https://github.com/xFFFFF/Gekko-BacktestTool/stargazers) - Batch backtest, import and strategy params optimalization for Gekko Trading Bot.

## TA Lib

- [pandas_talib](https://github.com/femtotrader/pandas_talib) [![GitHub stars](https://img.shields.io/github/stars/femtotrader/pandas_talib?style=flat)](https://github.com/femtotrader/pandas_talib/stargazers) - A Python Pandas implementation of technical analysis indicators.
- [finta](https://github.com/peerchemist/finta) [![GitHub stars](https://img.shields.io/github/stars/peerchemist/finta?style=flat)](https://github.com/peerchemist/finta/stargazers) - Common financial technical indicators implemented in Python-Pandas (70+ indicators).
- [tulipnode](https://github.com/TulipCharts/tulipnode) [![GitHub stars](https://img.shields.io/github/stars/TulipCharts/tulipnode?style=flat)](https://github.com/TulipCharts/tulipnode/stargazers) - Official Node.js wrapper for Tulip Indicators. Provides over 100 technical analysis overlay and indicator functions.
- [techan.js](https://github.com/andredumas/techan.js) [![GitHub stars](https://img.shields.io/github/stars/andredumas/techan.js?style=flat)](https://github.com/andredumas/techan.js/stargazers) - A visual, technical analysis and charting (Candlestick, OHLC, indicators) library built on D3.

## Exchange API

Do it in real world!

- [Trade It](https://docs.tradeit.app/mcp) - MCP for trading on common brokerages (Robinhood, ETrade, Schwab, Webull, Public, tastytrade, Coinbase, Kraken so far)
- [IbPy](https://github.com/blampe/IbPy) [![GitHub stars](https://img.shields.io/github/stars/blampe/IbPy?style=flat)](https://github.com/blampe/IbPy/stargazers) - Python API for the Interactive Brokers on-line trading system.
- [HuobiFeeder](https://github.com/mmmaaaggg/HuobiFeeder) [![GitHub stars](https://img.shields.io/github/stars/mmmaaaggg/HuobiFeeder?style=flat)](https://github.com/mmmaaaggg/HuobiFeeder/stargazers) - Connect HUOBIPRO exchange, get market/historical data for ABAT trading platform backtest analysis and live trading.
- [ctpwrapper](https://github.com/nooperpudd/ctpwrapper) [![GitHub stars](https://img.shields.io/github/stars/nooperpudd/ctpwrapper?style=flat)](https://github.com/nooperpudd/ctpwrapper/stargazers) - Shanghai future exchange CTP api.
- [PENDAX](https://github.com/CompendiumFi/PENDAX-SDK) [![GitHub stars](https://img.shields.io/github/stars/CompendiumFi/PENDAX-SDK?style=flat)](https://github.com/CompendiumFi/PENDAX-SDK/stargazers) - Javascript SDK for Trading/Data API and Websockets for cryptocurrency exchanges like FTX, FTXUS, OKX, Bybit, & More

### Framework

- [tf-quant-finance](https://github.com/google/tf-quant-finance) [![GitHub stars](https://img.shields.io/github/stars/google/tf-quant-finance?style=flat)](https://github.com/google/tf-quant-finance/stargazers) - High-performance TensorFlow library for quantitative finance.

### Visualizing

- [playground](https://github.com/tensorflow/playground) [![GitHub stars](https://img.shields.io/github/stars/tensorflow/playground?style=flat)](https://github.com/tensorflow/playground/stargazers) - Play with neural networks.
- [netron](https://github.com/lutzroeder/netron) [![GitHub stars](https://img.shields.io/github/stars/lutzroeder/netron?style=flat)](https://github.com/lutzroeder/netron/stargazers) - Visualizer for deep learning and machine learning models.
- [KLineChart](https://github.com/liihuu/KLineChart) [![GitHub stars](https://img.shields.io/github/stars/liihuu/KLineChart?style=flat)](https://github.com/liihuu/KLineChart/stargazers) - Highly customizable professional lightweight financial charts

### GYM Environment

- 🌟 [TradingGym](https://github.com/Yvictor/TradingGym) [![GitHub stars](https://img.shields.io/github/stars/Yvictor/TradingGym?style=flat)](https://github.com/Yvictor/TradingGym/stargazers) - Trading and Backtesting environment for training reinforcement learning agent.
- [TradzQAI](https://github.com/kkuette/TradzQAI) [![GitHub stars](https://img.shields.io/github/stars/kkuette/TradzQAI?style=flat)](https://github.com/kkuette/TradzQAI/stargazers) - Trading environment for RL agents, backtesting and training.
- [btgym](https://github.com/Kismuz/btgym) [![GitHub stars](https://img.shields.io/github/stars/Kismuz/btgym?style=flat)](https://github.com/Kismuz/btgym/stargazers) - Scalable, event-driven, deep-learning-friendly backtesting library.

## Articles

- [The-Economist](https://github.com/nailperry-zd/The-Economist) [![GitHub stars](https://img.shields.io/github/stars/nailperry-zd/The-Economist?style=flat)](https://github.com/nailperry-zd/The-Economist/stargazers) - The Economist.
- [nyu-mlif-notes](https://github.com/wizardforcel/nyu-mlif-notes) [![GitHub stars](https://img.shields.io/github/stars/wizardforcel/nyu-mlif-notes?style=flat)](https://github.com/wizardforcel/nyu-mlif-notes/stargazers) - NYU machine learning in finance notes.
- [Using LSTMs to Turn Feelings Into Trades](https://www.quantopian.com/posts/watch-our-webinar-buying-happiness-using-lstms-to-turn-feelings-into-trades-now?utm_source=forum&utm_medium=twitter&utm_campaign=sentiment-analysis)

## Others

- [zipline-tensorboard](https://github.com/jimgoo/zipline-tensorboard) [![GitHub stars](https://img.shields.io/github/stars/jimgoo/zipline-tensorboard?style=flat)](https://github.com/jimgoo/zipline-tensorboard/stargazers) - TensorBoard as a Zipline dashboard.
- [gekko-quasar-ui](https://github.com/H256/gekko-quasar-ui) [![GitHub stars](https://img.shields.io/github/stars/H256/gekko-quasar-ui?style=flat)](https://github.com/H256/gekko-quasar-ui/stargazers) - An UI port for gekko trading bot using Quasar framework.
- [Floom](https://github.com/FloomAI/Floom) [![GitHub stars](https://img.shields.io/github/stars/FloomAI/Floom?style=flat)](https://github.com/FloomAI/Floom/stargazers) AI gateway and marketplace for developers, enables streamlined integration and least volatile approach of AI features into products
- [LendTrain](https://www.lendtrain.com) - AI-native mortgage refinance plugin for Claude Code with real-time institutional pricing, state-specific closing costs, FHA Streamline/VA IRRRL detection, and regulatory compliance. Uses MCP (Model Context Protocol) to connect LLMs to live mortgage pricing.
- [Registry Broker](https://github.com/hashgraph-online/hashnet-mcp-js) [![GitHub stars](https://img.shields.io/github/stars/hashgraph-online/hashnet-mcp-js?style=flat)](https://github.com/hashgraph-online/hashnet-mcp-js/stargazers) - Universal AI agent index for discovering trading agents across Virtuals Protocol, NANDA, MCP, and other registries.
- [KeepRule](https://keeprule.com) - AI-powered investment discipline tracking platform with curated principles from 26 legendary investors including Buffett, Munger, and Dalio. Helps traders maintain rational decision-making.
- [Philidor](https://docs.philidor.io/docs) - DeFi risk infrastructure for AI agents: MCP server and REST API for vault risk scores, portfolio analysis, and due diligence. No API key. 700+ vaults, 9 protocols, 6 chains.
- [Hindsight](https://hindsight.vectorize.io) - State-of-the-art long-term memory for AI agents by Vectorize. Open source, self-hostable, with integrations for LangChain, CrewAI, MCP, and more. Gives financial trading agents persistent memory across sessions.

#### Other Resource

- 🌟🌟🌟 [Stock-Prediction-Models](https://github.com/huseinzol05/Stock-Prediction-Models) [![GitHub stars](https://img.shields.io/github/stars/huseinzol05/Stock-Prediction-Models?style=flat)](https://github.com/huseinzol05/Stock-Prediction-Models/stargazers) - Stock-Prediction-Models, Gathers machine learning and deep learning models for Stock forecasting, included trading bots and simulations.
- 🌟🌟 [Financial Machine Learning](https://github.com/firmai/financial-machine-learning) [![GitHub stars](https://img.shields.io/github/stars/firmai/financial-machine-learning?style=flat)](https://github.com/firmai/financial-machine-learning/stargazers) - A curated list of practical financial machine learning (FinML) tools and applications. This collection is primarily in Python.
- 🌟 [Awesome-Quant-Machine-Learning-Trading](https://github.com/grananqvist/Awesome-Quant-Machine-Learning-Trading) [![GitHub stars](https://img.shields.io/github/stars/grananqvist/Awesome-Quant-Machine-Learning-Trading?style=flat)](https://github.com/grananqvist/Awesome-Quant-Machine-Learning-Trading/stargazers) - Quant / Algorithm trading resources with an emphasis on Machine Learning.
- [awesome-quant](https://github.com/wilsonfreitas/awesome-quant) [![GitHub stars](https://img.shields.io/github/stars/wilsonfreitas/awesome-quant?style=flat)](https://github.com/wilsonfreitas/awesome-quant/stargazers) - A curated list of insanely awesome libraries, packages and resources for Quants (Quantitative Finance).
- [FinancePy](https://github.com/domokane/FinancePy) [![GitHub stars](https://img.shields.io/github/stars/domokane/FinancePy?style=flat)](https://github.com/domokane/FinancePy/stargazers) - A Python Finance Library that focuses on the pricing and risk-management of Financial Derivatives, including fixed-income, equity, FX and credit derivatives.
- [Explore Finance Service Libraries & Projects](https://kandi.openweaver.com/explore/financial-services#Top-Authors) - Explore a curated list of Fintech popular & new libraries, top authors, trending project kits, discussions, tutorials & learning resources on kandi.
- [AgentMarket](https://agentmarket.cloud) - B2A marketplace for AI agents. 189 listings, 28M+ real energy data records, LangChain/MCP integration.
- [MeterCall](https://metercall.ai/?v=f&src=github) — One metered API gateway. 21M+ endpoints (payments, SMS, AI, CRMs, gov data). Free tier; pay per call.
