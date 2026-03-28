# Control Hazard Analysis & Hardware Branch Prediction Benchmarking

**Author:** Sreedev US  
**Program:** B.Tech Artificial Intelligence (Class of 2028)  
**Institution:** Providence College of Engineering  
**Course:** KTU S4 Computer Organization and Architecture (COA)

---

## 🎯 Project Overview
This project investigates the impact of Control Hazards (pipeline flushes/bubbles) on modern processor architectures. Using the **gem5 cycle-accurate architectural simulator**, this repository automatically benchmarks four distinct hardware branch prediction algorithms to measure their efficiency in mitigating pipeline stalls.

### 🧠 Evaluated Branch Predictors:
1. **Local Predictor:** Baseline historical tracking.
2. **Bi-Mode Predictor:** Dual-table tracking to prevent destructive aliasing.
3. **Tournament Predictor:** A meta-predictor that dynamically selects the best underlying algorithm.
4. **Multiperspective Perceptron (8KB):** A hardware-based neural network that utilizes a weight system to learn software execution patterns on the fly.

---

## 🔬 Methodology & Workloads
The simulation models an **Out-of-Order (O3) CPU** executing compiled C benchmarks. To test the adaptability of the predictors, two distinct workloads were utilized:

* **Random Workload:** Uses `rand() % 100 < 50` to force perfectly unpredictable branches, establishing a baseline where pattern recognition fails.
* **Patterned Workload:** Uses a repeating mathematical sequence (`i % 4 != 0`) to test the ability of advanced predictors (Tournament & Perceptron) to "learn" the sequence and proactively eliminate pipeline squashes.

---

## ⚙️ CI/CD Automation Pipeline
This repository features a fully automated Continuous Integration pipeline using **GitHub Actions**. 

Upon every push to the `main` branch, the cloud workflow:
1. Initializes an Ubuntu server.
2. Pulls the pre-compiled `gem5.opt` binary via Git LFS.
3. Executes 8 full cycle-accurate processor simulations (4 Predictors × 2 Workloads).
4. Parses `stats.txt` for `condIncorrect`, `squashes`, and `simTicks`.
5. Uses `matplotlib` and `python-pptx` to dynamically compile the research data into a formatted PowerPoint presentation.
6. Attaches the `.pptx` as a downloadable build artifact.

## 📊 Results & Real-World Impact
*Detailed graphs and cycle-time analysis can be found in the auto-generated PowerPoint report located in the Actions tab.* The benchmark proves that utilizing advanced prediction architectures (like Tournament or Perceptron) on patterned workloads drastically reduces pipeline flushes, yielding a **~3.5% reduction in total CPU execution time** compared to baseline predictors.
