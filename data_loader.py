import os
import yaml
import pandas as pd
import paramiko
import pymysql
from ftplib import FTP
from datetime import datetime

class SourceLoader:
    def __init__(self, sources_config):
        self.sources_config = sources_config
    
    def load_sources(self):
        for source in self.sources_config:
            if source['type'] == 'ftp':
                self.load_ftp(source)
            elif source['type'] == 'mysql':
                self.load_mysql(source)
    
    def load_ftp(self, source):
        with FTP(source['host']) as ftp:
            if source['protocol'] == 'sftp':
                transport = paramiko.Transport((source['host'], source['port']))
                transport.connect(username=source['username'], password=source['password'])
                sftp = paramiko.SFTPClient.from_transport(transport)
                remote_files = sftp.listdir(source['path'])
            else:
                ftp.login(user=source['username'], passwd=source['password'])
                remote_files = ftp.nlst(source['path'])
            
            for remote_file in remote_files:
                local_path = f"etl/{source['dataset']}/{source['table_name']}/{source['dataset']}_{source['table_name']}_{datetime.now().strftime('%Y%m%d')}.parquet"
                self._download_and_save_file(source, remote_file, local_path)
    
    def _download_and_save_file(self, source, remote_file, local_path):
        # Code to download and save the file from FTP/SFTP to local path
        # Assuming you have implemented this
        
        # Sample code for downloading (replace with your actual implementation)
        # with open(local_path, 'wb') as local_file:
        #     ftp.retrbinary(f"RETR {remote_file}", local_file.write)
        
        print(f"File '{remote_file}' downloaded to '{local_path}'")

    def load_mysql(self, source):
        connection = pymysql.connect(
            host=source['host'],
            port=source['port'],
            user=source['username'],
            password=source['password'],
            db=source['database']
        )
        query = source['query']
        df = pd.read_sql(query, connection)
        
        local_path = f"etl/{source['dataset']}/{source['table_name']}/{source
