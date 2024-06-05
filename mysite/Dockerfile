# 使用 Python 3.10 作为基础镜像
FROM python:3.10

# 设置 容器工作目录 为 /app
WORKDIR /app

# 复制 requirements.txt 文件到 容器工作目录 /app
COPY requirements.txt .

# 安装 Python 依赖项
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 复制当前目录下的所有文件到 容器工作目录 /app
COPY . .

# 运行数据库迁移
RUN python manage.py makemigrations
RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]