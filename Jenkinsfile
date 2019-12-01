pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
            echo "Step 1 - Build"
	    sh "git clone https://github.com/gsudiro/project00.git"
            }
        }
        stage('Test'){
            steps{
            echo "Step 2 - Test"
            }
        }
        stage('Deploy'){
            steps{
            echo "Step 3 - Deploy"
            }
        }
    }
}
