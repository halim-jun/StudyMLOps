poetry run pytest project/tests -v

# 로컬에서 poetry run pytest:
- 어디서: 내 컴퓨터
- 언제: 내가 직접 명령어 입력할 때
- 목적: 개발 중 테스트, 디버깅

# GitHub Actions에서 pytest:
- 어디서: GitHub 서버 (Ubuntu 가상머신)
- 언제: 코드 푸시/PR 할 때 자동으로
- 목적: 코드 검증, 팀 공유

*핵심: 같은 테스트지만 "내 환경에서만 되는 게 아니라 다른 환경에서도 되는지" 자동으로 확인해주는 게 GitHub Actions의 역할이에요!*

#Pytest
- test_*.py 파일들을 자동으로 스캔
- 그 안의 test_* 로 시작하는 함수들을 자동 실행
- assert 문으로 검증 → 실패하면 빨간불, 성공하면 녹색