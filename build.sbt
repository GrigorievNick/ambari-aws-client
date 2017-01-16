import com.typesafe.sbt.packager.MappingsHelper._

name := "ambari-aws-client"

version := "1.0"

scalaVersion := "2.12.1"

val metaInfoConfig: String = "metainfo.xml"

lazy val `ambari-aws-client` = project
  .in(file("."))
  .enablePlugins(UniversalPlugin)
  .settings(
    topLevelDirectory := Some("AWSCLI"),
    mappings in(Universal, packageBin) ++= directory("configuration"),
    mappings in(Universal, packageBin) ++= directory("package"),
    mappings in(Universal, packageBin) += {
      val buildVersion = version.value + "-build-" + sys.env.getOrElse("BUILD_NUMBER", "local")
      val content =
        IO.read(file(metaInfoConfig)).replaceFirst("<version>.*</version>", s"<version>$buildVersion</version>")
      val templateFile = file(target.value.getAbsolutePath + "/" + metaInfoConfig)
      IO.write(templateFile, content)
      templateFile
    } -> metaInfoConfig
  )