# REYieldCast

**REYieldCast** (Renewable Energy Yield Forecasting) is a modular, production-grade forecasting pipeline that translates real-time renewable energy generation data into actionable financial projections such as IRR, DSCR, and cashflow curves. The project leverages publicly available sensor datasets, probabilistic ML models, and financial modeling to empower better investment decisions in wind and solar energy assets.

---

## 🌍 Project Motivation

Energy infrastructure is increasingly dependent on **accurate, dynamic forecasting**. Static financial models often underestimate volatility in renewable asset performance, leading to suboptimal investment, maintenance, and hedging strategies. **REYieldCast** closes this gap by combining:

- Real-time, high-resolution data from public repositories
- Machine learning-based forecasting models (LSTM, XGBoost, Monte Carlo)
- Financial modeling including discounted cashflow (DCF), payback, IRR
- Modular pipelines, scalable infrastructure, and production-readiness

---

## 🎯 Project Objectives

| Objective                         | Target Value                     |
|----------------------------------|----------------------------------|
| Forecast MAE (Production)        | ≤ 5% for next-quarter forecasts  |
| IRR Forecast Error               | ≤ 2 percentage points            |
| DSCR (Debt Service Coverage)     | ≥ 1.3                            |
| Data Capture Latency             | ≤ 5 seconds                      |
| Model Drift Monitoring           | Daily retrain or trigger alert  |

---

## 🔍 Project Features

- ✅ **Public Dataset Ingestion**: Wind, solar, and irradiance data from Zenodo, NREL, and IEA
- 📦 **Ingestion Pipelines**: Modular ETL with Airflow/Prefect (planned)
- 🤖 **Forecasting Models**: LSTM, Gradient Boosting, Monte Carlo, Stacked Ensembles
- 💰 **Financial Projection**: IRR, DSCR, DCF over 20+ years
- 📊 **Scenario Dashboards**: Energy-to-Cash, sensitivity sliders for prices/wind
- 🔁 **CI/CD**: GitHub Actions, automated testing, linting, model packaging
- 📦 **Docker-Ready**: Containerized for local and cloud deployment

---

## 📊 Example Outputs

- 📈 Forecasted production (P50, P75, P90 scenarios)
- 💵 Monthly and annual net cashflows
- 📉 IRR vs price volatility curve
- 🧩 SHAP/LIME-based explainability for forecasts
- 🧮 Probabilistic scenarios via Monte Carlo simulations

---

## 📡 Data Sources

| Dataset | Provider | Frequency | Access |
|--------|----------|-----------|--------|
| NREL OEDI | US Department of Energy | Hourly | [OpenEI/OEDI](https://data.openei.org/) |
| Zenodo Renewable Output | Multi-decade wind/solar | Hourly | [Zenodo DOI:10.5281/zenodo.8240163](https://doi.org/10.5281/zenodo.8240163) |
| PVOD | Single-site PV output | 15-min | [Mendeley Data](https://doi.org/10.17632/gxc6j5btrx.1) |
| IEA Renewables 2024 | Country-level | Annual | [IEA.org](https://www.iea.org/data-and-statistics) |

---

## ⚙️ Technologies Used

| Category              | Tools / Frameworks                    |
|-----------------------|---------------------------------------|
| Language              | Python 3.10                           |
| ML/DL Frameworks      | Scikit-learn, XGBoost, TensorFlow     |
| Workflow Orchestration| Prefect / Apache Airflow              |
| Experiment Tracking   | MLflow (Planned)                      |
| Infrastructure        | Docker, GitHub Actions, Terraform (planned) |
| Monitoring            | Prometheus, OpenTelemetry (Planned)  |
| Versioning            | Git, DVC (optional)                   |
| Visualization         | Streamlit, Tableau/PowerBI            |

---

## 🚀 Quick Start

### 1. Clone and Setup

```bash
git clone https://github.com/yourusername/REYieldCast.git
cd REYieldCast
pip install -r requirements.txt
```

### 2. Run a Sample Test

```bash
pytest
```

## 🛠️ Development Roadmap

| Milestone                                      | Status     |
|-----------------------------------------------|------------|
| ✅ Initial project structure and folder setup  | Completed  |
| ✅ GitHub Actions CI/CD pipeline               | Completed  |
| 🏗️  Real-time dataset ingestion (Zenodo, NREL) | In Progress|
| 🧠 Forecasting models (LSTM, XGBoost, Monte Carlo) | In Progress|
| 📉 Financial metrics integration (IRR, DSCR, DCF) | Planned    |
| 📊 Scenario dashboard (Streamlit or Tableau)   | Planned    |
| 🔁 Data versioning with DVC                    | Planned    |
| 🚢 Dockerization & cloud deployment            | Planned    |
| 📈 Model explainability (SHAP, LIME)           | Planned    |
| 🔔 Monitoring & model retraining automation    | Planned    |

---

## 🤝 How to Contribute

While REYieldCast is a solo-led project, ideas, discussions, and community collaboration are welcome.

### Ways You Can Contribute

- 💡 Open issues with feedback, dataset ideas, or feature suggestions
- 🛠 Submit pull requests (for ingestion scripts, model improvements, or visualizations)
- 🧪 Improve test coverage or CI configurations
- 📖 Help improve documentation or tutorials

> 🧩 All contributions must follow clean code principles, be well-documented, and include tests where appropriate.

---

## 📚 References & Research Inspiration

REYieldCast is built on a foundation of domain insights, best practices, and current research. Key resources include:

- **AAAI 2024** — [Multimodal Fusion in Solar Forecasting](https://ojs.aaai.org/index.php/AAAI/article/view/30459)
- **MDPI** — [Sensor Fusion for Renewable Asset Monitoring](https://www.mdpi.com/1996-1073/16/19/6833)
- **Jeremy Jordan** — [ML Project Best Practices](https://www.jeremyjordan.me/ml-projects-guide/)
- **OSTI.gov** — [Multi-Decade Renewable Dataset](https://www.osti.gov/servlets/purl/1883201)
- **Label Studio** — [Guide to ML Project Maturity & Tools](https://labelstud.io/learningcenter/the-complete-guide-to-machine-learning-tools/)
- **IEA 2024 Data** — [International Energy Agency](https://www.iea.org/data-and-statistics/data-product/renewables-2024-dataset)

More dataset links and academic citations can be found in the `/docs/` folder and in the ingestion scripts.

---

## 👤 Author

**Swarnabh Roy** — Final-year CS student | AI & Renewable Energy Enthusiast  
Building bridges between **machine learning** and **climate-conscious finance**.

- 💼 LinkedIn: [linkedin.com/in/swarnabhroy](https://linkedin.com/in/swarnabhroy)
- 💻 GitHub: [github.com/SwarnabhR](https://github.com/SwarnabhR)
- 📫 Contact: [workspace.swarnabh@gmail.com](mailto:workspace.swarnabh@gmail.com)

---

## 📜 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute the code with attribution.

See [`LICENSE`](./LICENSE) for full legal terms.

---

## 🌟 Acknowledgements

- To all the open data platforms making real-world modeling accessible.
- To the solo developers pushing boundaries in public.
- And to you — for believing in the power of good data, clean code, and climate-forward tools.

---
