pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                   if ! command -v python3 &> /dev/null; then
                       echo "Python3 could not be found, installing..."
                       sudo apt update && sudo apt install python3 python3-venv python3-pip -y
                   fi

                   python3 -m venv venv
                   . venv/bin/activate
                   pip install --upgrade pip
                   pip install pandas scikit-learn joblib
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                   . venv/bin/activate
                   python train_model.py
                '''
            }
        }

        stage('Validate Model') {
            steps {
                sh '''
                   . venv/bin/activate
                   python validate_model.py
                '''
            }
        }

        stage('Deploy Model') {
            steps {
                sh '''
                   . venv/bin/activate
                   python deploy_model.py
                '''
            }
        }
    }
}
