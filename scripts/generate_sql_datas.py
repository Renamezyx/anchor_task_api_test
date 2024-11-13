import os.path
import sqlite3

from config import get_project_root


class GenerateSqlData:
    def __init__(self, db_path, db_name):
        self.db_name = db_name
        self.db_path = db_path

    def create_db(self):
        """Creates the database and the employees table."""
        # 确保数据库路径存在
        os.makedirs(self.db_path, exist_ok=True)
        db_full_path = os.path.join(self.db_path, f'{self.db_name}.db')

        try:
            # 使用上下文管理器自动关闭连接
            with sqlite3.connect(db_full_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS employees (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        age INTEGER,
                        department TEXT
                    )
                ''')
                print("Table created successfully.")

        except sqlite3.Error as e:
            print(f"An error occurred: {e}")


if __name__ == '__main__':
    GenerateSqlData(get_project_root(), 1).create_db()
