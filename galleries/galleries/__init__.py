import pymysql
# install pymysql as mysql database driver.
pymysql.version_info = (1, 4, 0, "final", 0)
pymysql.install_as_MySQLdb()