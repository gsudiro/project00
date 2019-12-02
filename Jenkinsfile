pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
            echo "Step 1 - Build"
            sh "pip3 install -r requirements.txt"
            sh "python3 app.py"
            }
        }
        stage('Test'){
            steps{
            echo "Step 2 - Test"
            sh "python3 -m unittest test_app.py"    
            }
        }
        stage('Deploy'){
            steps{
            echo "Step 3 - Deploy"
            }
        }
    }
}
