# Git Flow 전략
- Branch 간의 문제 없이 배포까지 안정적으로 할 수 있도록 관리하는 전략

## 자주 사용하는 Branch
- Main(Master)
  - 실제 운영환경에 나와있는 코드
  - 안정적인 코드만 있어야 한다.
- Dev
  - Main을 베이스로 생성한 Branch
  - 보통 다음 배포에 나갈 내용을 머지한다. 
- Feature
  - 기능 개발 
  - 기능 개발을 모두 commit한 뒤, Dev 브랜치에 머지함.
- Release
  - Dev를 베이스로 생성한 Branch
  - Snapshot을 쓰는 느낌으로 배포함
  - Release Branch로 배포한 순간 Dev보단 Release로 머지한다.
  - 예를 들면 QA나 테스트 후 수정할 경우
- Hotfix
  - 의도치 않는 장애상황이 벌어졌을 때

## 이번에 실습 시나리오
1. Release Branch 생성 후 추가 작업이 필요해질 경우
2. Release Branch 생성 후 추가 작업이 없는 경우
3. Hotfix가 나가야 할 경우

## 정기배포를 위한 GitFlow 전략
> 요구사항
- Login / Logout 기능 개발

### Dev에서 Release로 머지한 상황
1. 그런데 추가 비밀번호 변경 기능이 필요함
2. Dev -- Feature 브랜치가 아닌 Release -- Feature 브랜치를 땀.
3. 기능 개발 후 Feature 브랜치를 Release에 머지
4. Main에 Release 머지
5. Dev와 Main 머지하여 버전을 맞춤
   - Dev = Main + @ 여야함!
   - 그러나 Release에서 코드 수정 후 Main에 머지하면 Dev != Main + @임
   - Dev는 최신 상태를 유지해야 하는데, 그렇지 않게 되어버림
   - 이 과정이 없으면 충돌이 많이 난다.... 실제로도....흑흑

### Hotfix가 나가야 할 상황
1. Main 브랜치를 베이스로 Hotfix 브랜치를 땀.
2. 기능 개발 브랜치를 Hotfix 브랜치에 머지한 후
3. Main에 Hotfix 브랜치 머지
4. 역시 Main를 Dev에 머지한다.  