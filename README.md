# 🛡️ CryptoHub: Digital Security & Mathematics Suite

A modern, web-based cryptography toolbox built with **Django** and **Tailwind CSS**. This application provides an interactive interface for performing image steganography and fundamental cryptographic mathematical operations.

![Steganography Demo](https://img.shields.io/badge/Cryptography-Steganography-rose)
![Mathematics Demo](https://img.shields.io/badge/Mathematics-Euclidean-emerald)
![Framework](https://img.shields.io/badge/Framework-Django%206.0-092e20)

---

## ✨ Features

### 1. 👁️ Image Steganography (LSB)
*   **Secure Encoding:** Conceal secret text messages within the Least Significant Bits (LSB) of an image's pixels.
*   **Data Integrity:** Automatically generates and downloads a **PNG** file to prevent lossy compression from destroying hidden data.
*   **Stealth Extraction:** Upload an encoded image to instantly retrieve and decrypt the hidden "Intel."

### 2. 🧮 Euclidean GCD
*   **High-Speed Computation:** Quickly find the Greatest Common Divisor of two large integers.
*   **Clean Interface:** Modern, wide-input layout for ease of use during demonstrations.

### 3. 🧬 Extended Euclidean Algorithm
*   **Linear Combinations:** Find integers $x$ and $y$ such that $ax + by = \gcd(a, b)$.
*   **Equation Solver:** Displays the complete linear Diophantine equation alongside the computed coefficients.

---

## 🚀 Getting Started

### Prerequisites
*   Python 3.10+
*   pip

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/crypto-toolbox.git
   cd crypto-toolbox
   ```

2. **Install dependencies:**
   ```bash
   pip install django pillow
   ```

3. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Start the application:**
   *   **Windows:** Double-click `run.bat`
   *   **Linux/Mac:** `python manage.py runserver`

5. **Open your browser:**
   Navigate to `http://127.0.0.1:8000`

---

## 🎨 UI Design
The application features a **Dark Slate & Rose** aesthetic designed for a modern "security suite" feel.
*   **Responsive Sidebar:** Seamless navigation between tools.
*   **Tailwind CSS:** Utility-first styling for a sleek, floating-card UI.
*   **Font Awesome:** Integrated iconography for intuitive interaction.

## 🛠️ Tech Stack
*   **Backend:** Python, Django
*   **Frontend:** HTML5, Tailwind CSS, JavaScript
*   **Image Processing:** Pillow (PIL)
*   **Icons:** Font Awesome 6.0

---

## 📝 License
Distributed under the MIT License. See `LICENSE` for more information.

---
*Created for Cryptography Coursework - 2026*
