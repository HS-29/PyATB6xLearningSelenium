# 🌐 Mastering Web Automation with Selenium 4.x

> **Author:** Harsh  
> **Website:** [thetestingacademy.com](https://thetestingacademy.com)  
> **Course Notes By:** Pramod Sir — TheTestingAcademy

---

## 📋 Table of Contents

- [About](#about)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Topics Covered](#topics-covered)
- [Running Tests](#running-tests)
- [CI/CD with Jenkins](#cicd-with-jenkins)
- [References](#references)

---

## About

This repository contains notes, code examples, and automation scripts from the **Mastering Web Automation with Selenium 4.x** course by TheTestingAcademy (Pramod Sir).

Selenium is an open-source suite that automates web browsers. This course covers everything from the basics of Selenium WebDriver to advanced topics like Grid, POM, CI/CD with Jenkins, and cloud execution.

---

## Tech Stack

| Tool/Library         | Purpose                            |
|----------------------|------------------------------------|
| Python 3.x           | Primary language                   |
| Selenium 4.x         | Web browser automation             |
| Pytest               | Test framework                     |
| Allure Report        | Test reporting                     |
| openpyxl             | Data-driven testing (Excel)        |
| pytest-xdist         | Parallel test execution            |
| pytest-html          | HTML reports                       |
| Faker                | Test data generation               |
| python-dotenv        | Environment variable management    |
| PyYAML               | YAML config support                |
| Jenkins              | CI/CD automation                   |
| Docker / Selenoid    | Grid execution                     |

---

## Project Structure

```
PyWebAutomation/
│
├── src/
│   ├── pageobjects/        # Page Object Model classes
│   └── utils/              # Helper utilities
│
├── tests/
│   ├── login/              # Login test cases
│   ├── practice/           # Practice automation scripts
│   └── __init__.py
│
├── resources/
│   ├── constants/          # Constant values
│   └── testdata/           # Excel / CSV / JSON test data
│
├── reports/                # Allure & HTML test reports
├── conftest.py             # Pytest fixtures (driver setup/teardown)
├── base_test.py            # Base test class
├── requirements.txt        # Python dependencies
├── pytest.ini              # Pytest configuration & logging
└── README.md
```

---

## Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/selenium-python-automation.git
cd selenium-python-automation
```

### 2. Create and Activate Virtual Environment

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Key packages:**
```bash
pip install selenium pytest allure-pytest pytest-html openpyxl \
            pyyaml faker pytest-xdist python-dotenv selenium-page-factory
```

### 4. Browser Driver Setup

Selenium 4.x handles browser drivers automatically via **Selenium Manager**.  
Supported browsers:

| Browser          | Maintained By    | Supported OS              |
|------------------|------------------|---------------------------|
| Chrome/Chromium  | Google           | Windows / macOS / Linux   |
| Firefox          | Mozilla          | Windows / macOS / Linux   |
| Edge             | Microsoft        | Windows / macOS / Linux   |
| Safari           | Apple            | macOS High Sierra+        |

---

## Topics Covered

### 🔩 Core Selenium
- Selenium WebDriver Architecture (JSON Wire Protocol → W3C Protocol)
- Selenium Suite: WebDriver, IDE, Grid
- ChromeOptions, Proxy, PageLoadStrategy
- Remote WebDriver setup

### 🔎 Locators
- ID, Name, Class Name, Tag Name
- Link Text, Partial Link Text
- CSS Selectors (attribute, wildcard, nth-child, etc.)
- XPath — Absolute vs Relative
- XPath Functions: `text()`, `contains()`, `starts-with()`, `normalize-space()`
- XPath Axes: ancestor, child, descendant, following-sibling, etc.

### ⌛ Waits
- Implicit Wait
- Explicit Wait with Expected Conditions
- Fluent Wait

### 🧭 Navigation
- `driver.get()`, `driver.back()`, `driver.forward()`, `driver.refresh()`
- Quit vs Close

### ⚙️ Web Interactions
- Static & Dynamic Dropdowns (`Select` class + XPath/CSS)
- Alerts: Simple, Confirmation, Prompt
- Checkboxes & Radio Buttons
- Web Tables (Static & Dynamic)
- File Upload
- Windows & Tabs switching
- iFrames (by index, name/id, WebElement)
- Drag and Drop
- Keyboard & Mouse Actions (`ActionChains`)
- JavaScript Executor
- SVG Elements
- Shadow DOM
- Relative Locators (Selenium 4): `above()`, `below()`, `near()`, `toLeftOf()`, `toRightOf()`

### 🏗️ Framework Design
- Page Object Model (POM)
- Page Factory
- Data-Driven Testing with Excel (`openpyxl`)
- Logging with `pytest` (`pytest.ini` / `pyproject.toml`)
- Virtual Environment isolation

### 🔁 CI/CD & Grid
- Selenium Grid 3 & 4 (Standalone, Hub-Node, Fully Distributed)
- Running Selenium on Docker
- Selenoid setup
- Jenkins installation on AWS EC2
- Running tests via Jenkins (Freestyle + Pipeline)
- Cloud testing with BrowserStack / SauceLabs

---

## Running Tests

### Run all tests:
```bash
pytest tests/ -v
```

### Run specific test file:
```bash
pytest tests/login/test_vwo_login.py -v
```

### Run with Allure report:
```bash
pytest tests/ --alluredir=./reports
allure serve ./reports
```

### Run with HTML report:
```bash
pytest tests/ --html=report.html
```

### Run in parallel:
```bash
pytest tests/ -n 4
```

### Run by marker:
```bash
pytest -m actions
```

---

## CI/CD with Jenkins

### Jenkins Setup on AWS EC2

```bash
# Step 1: Install Java
sudo apt update
sudo apt install openjdk-11-jre -y

# Step 2: Install Jenkins
curl -fsSL https://pkg.jenkins.io/debian/jenkins.io.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update && sudo apt-get install jenkins

# Step 3: Start Jenkins
sudo systemctl enable jenkins
sudo systemctl start jenkins
```

Access Jenkins at: `http://<your-ec2-ip>:8080`

### Jenkins Build Script (Mac/Linux)

```bash
cd "/path/to/your/project"
pip3 install -r requirements.txt
pytest tests/ -s -v --html=report.html --alluredir=./reports
```

### Jenkins Build Script (Windows)

```batch
set path="C:\Users\<user>\AppData\Local\Programs\Python\Python312"
set path="C:\Users\<user>\AppData\Local\Programs\Python\Python312\Scripts"
pip install -r requirements.txt
pytest tests\
```

---

## References

- [Selenium Official Docs](https://www.selenium.dev/documentation/)
- [W3C WebDriver Spec](https://www.w3.org/TR/webdriver/)
- [XPath Axes Reference](https://devhints.io/xpath)
- [CSS Selectors Reference](https://www.geeksforgeeks.org/css-selectors-complete-reference/)
- [TheTestingAcademy](https://thetestingacademy.com)
- [Selenium vs Playwright vs Cypress Comparison](https://blog.checklyhq.com/cypress-vs-selenium-vs-playwright-vs-puppeteer-speed-comparison/)
- [SelectorsHub](https://selectorshub.com/)
- [Mockaroo — Test Data Generator](https://www.mockaroo.com/)
- [BrowserStack](https://www.browserstack.com/)

---

> 💡 *"Selenium automates browsers. That's it! What you do with that power is entirely up to you."*

---

**© TheTestingAcademy | Author: Harsh | [thetestingacademy.com](https://thetestingacademy.com)**