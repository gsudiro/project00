pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
            echo "Step 1 - Build"
            sh "pip3 install -r requirements.txt"
            }
        }
        stage('Test'){
            steps{
            echo "Step 2 - Test"
            sh "python3 test_app.py"    
            }
        }
    }
}
