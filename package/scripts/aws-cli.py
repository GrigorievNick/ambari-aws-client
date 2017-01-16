
from resource_management import *


class SchemaRegistry(Script):
    def install(self, env):
        import params
        env.set_params(params)
        self.install_packages(env)
        Directory(params.data_dir,
                  mode=0755,
                  owner=params.user,
                  group=params.group,
                  create_parents=True,
                  recursive_ownership=True
                  )
        Directory(params.aws_conf_dir,
                  mode=0755,
                  owner=params.user,
                  group=params.group,
                  create_parents=True,
                  recursive_ownership=True
                  )
        Execute("curl {params.download_url} -o {params.data_dir}/awscli-bundle.zip",
                user=params.user,
                logoutput=True)
        Execute("yum -y install unzip")
        Execute("unzip awscli-bundle.zip")
        Execute("./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws")

        File(format("{params.aws_conf_dir}/conf"),
             content=Template("conf.j2"),
             encoding="utf-8"
             )
        File(format("{params.aws_conf_dir}/credentials"),
             content=Template("credentials.j2"),
             encoding="utf-8"
             )
        Execute("aws help",
                user=params.user,
                logoutput=True)

    def status(self, env):
        raise ClientComponentHasNoStatus()


if __name__ == "__main__":
    SchemaRegistry().execute()
