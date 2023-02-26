import pandas as pd
import os.path as op


class FileOperation:

    def save_csv(self, file_name, df_write):
        if op.exists(file_name):
            df_read = pd.read_csv(file_name)
            max_id = df_read['ID'].max()
            df_write.insert(0, 'ID', [max_id + 1], False)
            df_write.to_csv(file_name, mode='a', index=False, header=False)
        else:
            df_write.insert(0, 'ID', [1], False)
            df_write.to_csv(file_name, index=False)

    def save_json(self, file_name, df_write):
        if op.exists(file_name):
            df_read = pd.read_json(file_name, orient='index')
            max_id = df_read['ID'].max()
            df_write.insert(0, 'ID', [max_id + 1], False)
            df_read = pd.concat([df_read, df_write], ignore_index=True)
            df_read.to_json(file_name, orient='index')
        else:
            print(df_write)
            df_write.insert(0, 'ID', [1], False)
            df_write.to_json(file_name, orient="index")
