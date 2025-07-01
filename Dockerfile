FROM python:3.10-slim

#불필요한 저장 없이 진행
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

#도커 내 워크 디렉토리
WORKDIR /app

#도커 내 패키지 업데이트
RUN apt-get update && apt-get install -y \
    --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


    #유저 그룹 및 유저 제작
RUN groupadd --gid 1000 appuser && \
    useradd --uid 1000 --gid appuser --shell /bin/bash --create-home appuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
    
COPY project/ ./project/
COPY pyproject.toml setup.py ./


RUN mkdir -p /app/models && \
    chown -R appuser:appuser /app

#보안을 위해 appuser 사용자로 전환
USER appuser

# Set the default command
CMD ["python", "project/src/main.py"]
