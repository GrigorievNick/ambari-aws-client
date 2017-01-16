ambari-aws-client

Ambari service package for aws clihttp://docs.aws.amazon.com/cli/latest/reference

Use `sbt packaheBin` to build zip file.

Copy package to ambari resorces: 
`scp /target/universal/ambari-aws-client-1.0.zip :/var/lib/ambari-server/resources/stacks/HDP/2.5/services/`
 
Restart ambari service `ambari-service restart`
 
Go ambaru UI and use add service button, find and  install AWS Client
