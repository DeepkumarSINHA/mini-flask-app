# Flask & Express CI/CD Deployment using Jenkins on AWS EC2

## 📌 Project Overview
This project demonstrates deployment of a Flask backend and an Express frontend on a single Amazon EC2 instance with an automated CI/CD pipeline using Jenkins.

---

## 🏗 Architecture
Browser  
→ AWS EC2 (Ubuntu 22.04)  
→ Jenkins (CI/CD)  
→ PM2 (Process Manager)  
→ Flask (Port 5000)  
→ Express (Port 3000)

---

## 🚀 Technologies Used
- AWS EC2 (Ubuntu 22.04)
- Python (Flask)
- Node.js (Express)
- Jenkins
- PM2
- Git & GitHub

---

## 🔧 Deployment Steps

### 1️⃣ EC2 Setup
- Created EC2 instance (t2.micro)
- Opened ports:
  - 22 (SSH)
  - 5000 (Flask)
  - 3000 (Express)
  - 8080 (Jenkins)

---

### 2️⃣ Flask Deployment
- Cloned Flask repo
- Created Python virtual environment
- Installed dependencies
- Ran Flask app using PM2

Access URL:  
👉 http://13.204.76.72:5000

---

### 3️⃣ Express Deployment
- Cloned Express repo
- Installed Node dependencies
- Ran Express app using PM2

Access URL:  
👉 http://13.204.76.72:3000

---

### 4️⃣ Jenkins CI/CD Pipeline
- Installed Jenkins on EC2
- Installed required plugins:
  - Git
  - GitHub
  - Pipeline
  - NodeJS
- Created Jenkins Pipeline Job
- Pipeline stages:
  - Clone Flask repo
  - Clone Express repo
  - Restart apps using PM2

---

## 📜 Jenkins Pipeline Script

```groovy
pipeline {
    agent any

    stages {
        stage('Clone Flask Repo') {
            steps {
                sh '''
                mkdir -p /opt/apps
                cd /opt/apps
                if [ -d "mini-flask-app" ]; then
                    cd mini-flask-app
                    git pull origin main
                else
                    git clone https://github.com/DeepkumarSINHA/mini-flask-app.git
                fi
                '''
            }
        }

        stage('Clone Express Repo') {
            steps {
                sh '''
                cd /opt/apps
                if [ -d "express-frontend" ]; then
                    cd express-frontend
                    git pull origin main
                else
                    git clone https://github.com/DeepkumarSINHA/express-frontend.git
                fi
                '''
            }
        }

        stage('Restart Apps using PM2') {
            steps {
                sh '''
                pm2 restart flask-app || pm2 start /opt/apps/mini-flask-app/app.py --name flask-app --interpreter python3
                pm2 restart express-app || pm2 start /opt/apps/express-frontend/index.js --name express-app
                pm2 save
                '''
            }
        }
    }
}
