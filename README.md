
# 🌐 Internet Speed Test GUI

A simple Python desktop application to test your internet speed with a clean Tkinter-based graphical interface. It measures your **Download**, **Upload**, and **Ping** using the `speedtest` library.


---

## 🚀 Features

- ✅ One-click internet speed test
- 📊 Shows download/upload speed and ping in real-time
- 🎨 Simple and clean GUI using Tkinter
- 💻 Cross-platform (Windows, Linux, Mac)

---

## 🛠 Requirements

Install required dependencies with:

```bash
pip install -r requirements.txt
```

Required libraries:

- `tkinter` (comes built-in with Python)
- `speedtest-cli`

> Or install manually:
```bash
pip install speedtest-cli
```

---

## 📁 Project Structure

```
internet_speed_test/
│
├── gui/
│   └── app.py               # Main Tkinter GUI logic
│
├── core/
│   └── speed_checker.py     # Backend speed test function
│
├── README.md
├── requirements.txt
└── run.py                   # Entry-point script to launch the GUI
```

---

## 📌 How to Run

1. Clone the repository:
```bash
git clone https://github.com/yourusername/internet_speed_test.git
cd internet_speed_test
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
python run.py
```

---

## 🧠 What You Learn

- How to use external APIs in Python (Speedtest)
- GUI design with `tkinter`
- Structuring small desktop apps with clean separation
- Error handling and UX design


## 🧑‍💻 Author

**Hassan Khan**  
Computer Science student | Python developer | Cybersecurity learner

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
