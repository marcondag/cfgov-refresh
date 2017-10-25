node {
    triggers {
        pollSCM('* * * * *')
    }
    stages {
        stage('Unit Testing') {
            steps {
                // Abort any still-running stages if one fails
                failFast true
                parallel(
                    'Front-end tests': {
                        def node = tool name: 'Node 8x Current', type: 'jenkins.plugins.nodejs.tools.NodeJSInstallation'
                        env.PATH = '${node}/bin:${env.PATH}'
                        steps {
                            sh './run_travis.sh frontend'
                        }
                    },
                    'Back-end tests': {
                        steps {
                            sh './run_travis.sh backend'
                        }
                    },
                    'Acceptance tests': {
                        def node = tool name: 'Node 8x Current', type: 'jenkins.plugins.nodejs.tools.NodeJSInstallation'
                        env.PATH = '${node}/bin:${env.PATH}'
                        steps {
                            sh './run_travis.sh acceptance'
                        }
                    }
                }
            }
        }
        stage('Coverage') {
            steps {
                parallel {
                    stage('Front-End Coverage') {
                        sleep 1
                        echo 'Hello front-end coverage!'
                    }
                    stage('Back-End Coverage') {
                        sleep 1
                        echo 'Hello back-end coverage!'
                    }
                }
            }
        }
    }
}
