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

# Type annotation

1. 타입 주석의 목적
	•	코드 가독성 향상
→ 이 함수는 아무것도 반환하지 않는다(-> None), 이 인자는 불리언이어야 한다(stage_fear: bool) 같은 정보를 읽는 사람에게 명확히 알려줘요.
	•	정적 분석 도구와 연계
	•	mypy, pyright 같은 정적 타입체커가 타입을 검사해 줍니다.
	•	예를 들어 stage_fear: bool인데 문자열을 넘기면 에디터에서 경고 띄움.
	•	IDE 지원
	•	VS Code, PyCharm 같은 IDE에서 자동완성, 에러 감지, 함수 힌트 제공에 도움.

⸻

2. pytest와의 관계
	•	pytest는 타입 힌트를 무시합니다.
→ pytest는 단순히 test_* 함수들을 찾아서 실행할 뿐, 타입 주석을 검사하지 않아요.
	•	pytest와 어울리는 건 “어떤 인자를 fixture로 주입할 수 있는가”인데, 이때도 타입 주석은 필요 없음. 이름만 맞으면 fixture가 들어갑니다.

@pytest.fixture
def sample_data():
    return {"x": 1}

def test_something(sample_data):  # 타입 힌트 없어도 fixture 주입됨
    assert "x" in sample_data



⸻

3. 타입 주석이 정말 유용한 순간
	•	협업: 팀원들이 함수 시그니처만 보고도 무슨 값이 오가야 하는지 이해 가능.
	•	MLOps 맥락: 데이터 스키마 검증을 pydantic이나 dataclasses와 함께 쓰면 안정성이 커짐.
	•	CI/CD: GitHub Actions에서 mypy 단계 추가하면, PR 올릴 때 타입 체크 자동 실행 → 타입 불일치 빨리 잡음.

⸻

4. 결론
	•	타입 주석은 pytest와 직접 상호작용하지 않음.
	•	대신 IDE, 타입체커, 협업, CI 품질 보증에 도움을 줌.
	•	pytest는 타입 힌트 없이도 100% 잘 동작하지만, MLOps 같은 프로덕션급 프로젝트라면 타입 주석 + 정적 검사 도구를 붙이는 게 베스트 프랙티스.

