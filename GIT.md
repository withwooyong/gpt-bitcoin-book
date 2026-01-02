# 📚 Git 버전 관리 가이드

프로젝트 개발 시 유용한 Git 명령어 모음입니다.

## 📖 목차

- [저장소 초기화 및 원격 연결](#저장소-초기화-및-원격-연결)
- [브랜치 관리](#브랜치-관리)
- [변경사항 관리](#변경사항-관리)
- [동기화 작업](#동기화-작업)
- [히스토리 관리](#히스토리-관리)
- [실수 복구](#실수-복구)
- [유용한 명령어](#유용한-명령어)

## 저장소 초기화 및 원격 연결

```bash
# 새 Git 저장소 초기화
git init

# 원격 저장소 추가
git remote add origin <repository-url>

# 원격 저장소 확인
git remote -v

# 원격 저장소 변경
git remote set-url origin <new-repository-url>

# 원격 저장소 제거
git remote remove origin
```

## 브랜치 관리

```bash
# 현재 브랜치 확인
git branch

# 새 브랜치 생성
git branch <branch-name>

# 브랜치 전환
git checkout <branch-name>
# 또는 (Git 2.23+)
git switch <branch-name>

# 브랜치 생성 및 전환을 동시에
git checkout -b <branch-name>
# 또는
git switch -c <branch-name>

# 브랜치 삭제
git branch -d <branch-name>

# 브랜치 강제 삭제 (병합되지 않은 브랜치)
git branch -D <branch-name>

# 원격 브랜치 목록 확인
git branch -r

# 모든 브랜치 목록 확인 (로컬 + 원격)
git branch -a

# 원격 브랜치 삭제
git push origin --delete <branch-name>

# 브랜치 이름 변경
git branch -m <old-name> <new-name>
```

## 변경사항 관리

```bash
# 파일 상태 확인
git status

# 간단한 상태 확인
git status -s

# 변경사항 확인
git diff

# 스테이징된 변경사항 확인
git diff --staged

# 특정 파일의 변경사항 확인
git diff <file-name>

# 파일 스테이징 (커밋 준비)
git add <file-name>

# 모든 변경된 파일 스테이징
git add .

# 특정 확장자 파일만 스테이징
git add *.py

# 대화형으로 스테이징
git add -p

# 커밋 생성
git commit -m "커밋 메시지"

# 상세한 커밋 메시지 작성 (에디터 열림)
git commit

# 스테이징과 커밋을 동시에 (추적 중인 파일만)
git commit -am "커밋 메시지"

# 빈 커밋 생성 (CI/CD 재실행 등에 유용)
git commit --allow-empty -m "Empty commit"
```

## 동기화 작업

```bash
# 원격 저장소에서 최신 변경사항 가져오기 및 병합
git pull origin main

# 특정 브랜치에서 가져오기
git pull origin <branch-name>

# 리베이스 방식으로 가져오기
git pull --rebase origin main

# 로컬 변경사항을 원격 저장소에 푸시
git push origin main

# 처음 푸시할 때 (upstream 설정)
git push -u origin main

# 모든 브랜치 푸시
git push --all origin

# 모든 태그 푸시
git push --tags

# 강제 푸시 (주의! 협업 시 문제 발생 가능)
git push -f origin main

# 원격 저장소의 변경사항 확인 (병합 없이)
git fetch origin

# 모든 원격 브랜치 가져오기
git fetch --all

# 삭제된 원격 브랜치 정보 제거
git fetch --prune
```

## 히스토리 관리

```bash
# 커밋 히스토리 확인
git log

# 간단한 히스토리 확인
git log --oneline

# 그래프 형태로 히스토리 확인
git log --graph --oneline --all

# 상세한 그래프 히스토리
git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit

# 최근 n개의 커밋만 확인
git log -n 5

# 특정 파일의 히스토리 확인
git log -- <file-name>

# 특정 작성자의 커밋만 확인
git log --author="작성자명"

# 날짜 범위로 확인
git log --since="2024-01-01" --until="2024-12-31"

# 커밋 내용 검색
git log --grep="검색어"

# 특정 커밋의 상세 내용 확인
git show <commit-hash>

# 파일별 수정 이력 확인 (누가, 언제 수정했는지)
git blame <file-name>
```

## 실수 복구

```bash
# 스테이징 취소 (파일은 변경 상태 유지)
git reset HEAD <file-name>

# 모든 스테이징 취소
git reset HEAD

# 파일 변경사항 취소 (위험! 변경사항 영구 삭제)
git checkout -- <file-name>

# 모든 변경사항 취소
git checkout -- .

# 마지막 커밋 수정 (아직 푸시하지 않은 경우)
git commit --amend -m "수정된 커밋 메시지"

# 마지막 커밋에 파일 추가
git add <forgotten-file>
git commit --amend --no-edit

# 특정 커밋으로 되돌리기
git reset --soft HEAD^   # 커밋만 취소, 변경사항은 스테이징 상태로 유지
git reset --mixed HEAD^  # 커밋, 스테이징 취소 (기본값)
git reset --hard HEAD^   # 모든 변경사항 취소 (위험!)

# n개의 커밋 되돌리기
git reset --hard HEAD~3  # 최근 3개 커밋 취소

# 특정 커밋으로 되돌리기
git reset --hard <commit-hash>

# 커밋 취소 (새로운 커밋 생성)
git revert <commit-hash>

# 병합 취소
git merge --abort

# 리베이스 취소
git rebase --abort

# 삭제한 커밋 복구 (reflog 사용)
git reflog
git reset --hard <commit-hash>
```

## 유용한 명령어

### .gitignore 설정

```bash
# 특정 파일 무시하기
echo "파일명" >> .gitignore

# 패턴으로 무시하기
echo "*.log" >> .gitignore
echo "__pycache__/" >> .gitignore
echo ".env" >> .gitignore

# .gitignore가 적용되지 않을 때
git rm -r --cached .
git add .
git commit -m "Update .gitignore"
```

### Stash (임시 저장)

```bash
# 변경사항 임시 저장
git stash

# 메시지와 함께 임시 저장
git stash save "작업 내용"

# Untracked 파일도 포함하여 저장
git stash -u

# 임시 저장 목록 확인
git stash list

# 임시 저장한 변경사항 복원 (stash 삭제)
git stash pop

# 임시 저장한 변경사항 적용 (stash 유지)
git stash apply

# 특정 stash 적용
git stash apply stash@{1}

# 특정 stash 삭제
git stash drop stash@{0}

# 모든 stash 삭제
git stash clear
```

### Git 설정

```bash
# Git 설정 확인
git config --list

# 전역 설정 확인
git config --global --list

# 사용자 정보 설정
git config --global user.name "이름"
git config --global user.email "이메일"

# 에디터 설정
git config --global core.editor "code --wait"  # VS Code
git config --global core.editor "vim"           # Vim

# 줄바꿈 설정
git config --global core.autocrlf true   # Windows
git config --global core.autocrlf input  # Mac/Linux

# 별칭(Alias) 설정
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.cm commit
git config --global alias.lg "log --graph --oneline --all"
```

### 태그 관리

```bash
# 태그 목록 확인
git tag

# 새 태그 생성 (Lightweight)
git tag v1.0.0

# 주석이 있는 태그 생성 (Annotated)
git tag -a v1.0.0 -m "버전 1.0.0 릴리스"

# 특정 커밋에 태그 추가
git tag -a v1.0.0 <commit-hash> -m "메시지"

# 태그 정보 확인
git show v1.0.0

# 태그 푸시
git push origin v1.0.0

# 모든 태그 푸시
git push origin --tags

# 태그 삭제 (로컬)
git tag -d v1.0.0

# 태그 삭제 (원격)
git push origin :refs/tags/v1.0.0
# 또는
git push origin --delete v1.0.0
```

### 기타 유용한 명령어

```bash
# 특정 파일 무시하고 추적하지 않기 (이미 추적 중인 파일)
git update-index --assume-unchanged <file-name>

# 다시 추적하기
git update-index --no-assume-unchanged <file-name>

# 저장소 정리 및 최적화
git gc

# 손상된 저장소 복구
git fsck

# 특정 파일만 체크아웃
git checkout <branch-name> -- <file-name>

# 충돌 파일 확인
git diff --name-only --diff-filter=U

# 병합 충돌 해결 후
git add <resolved-file>
git commit

# 서브모듈 업데이트
git submodule update --init --recursive

# Cherry-pick (특정 커밋만 가져오기)
git cherry-pick <commit-hash>

# 이진 검색으로 버그 찾기
git bisect start
git bisect bad              # 현재 커밋은 버그 있음
git bisect good <commit>    # 이 커밋은 정상
# ... 반복하여 버그 커밋 찾기
git bisect reset            # 완료
```

## 📋 일반적인 워크플로우

### 새 기능 개발

```bash
# 1. 최신 main 브랜치 가져오기
git checkout main
git pull origin main

# 2. 새 기능 브랜치 생성
git checkout -b feature/new-feature

# 3. 작업 및 커밋
git add .
git commit -m "feat: 새 기능 구현"

# 4. 원격에 푸시
git push -u origin feature/new-feature

# 5. Pull Request 생성 (GitHub/GitLab에서)

# 6. 병합 후 브랜치 정리
git checkout main
git pull origin main
git branch -d feature/new-feature
git push origin --delete feature/new-feature
```

### 긴급 수정 (Hotfix)

```bash
# 1. main 브랜치에서 hotfix 브랜치 생성
git checkout main
git checkout -b hotfix/critical-bug

# 2. 수정 및 커밋
git add .
git commit -m "fix: 긴급 버그 수정"

# 3. main에 병합
git checkout main
git merge hotfix/critical-bug

# 4. 태그 생성 및 푸시
git tag -a v1.0.1 -m "버그 수정 릴리스"
git push origin main --tags

# 5. hotfix 브랜치 삭제
git branch -d hotfix/critical-bug
```

## 🔗 참고 자료

- [Git 공식 문서](https://git-scm.com/doc)
- [Git 치트시트](https://education.github.com/git-cheat-sheet-education.pdf)
- [Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials)

---

💡 **Tip**: Git 명령어에 익숙해지려면 자주 사용하는 명령어를 별칭(alias)으로 설정하면 편리합니다!
